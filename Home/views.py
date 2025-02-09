# filepath: /Z:/Django/College Project/Event/Home/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import default_storage
import random
import json
import os
import logging
from dotenv import load_dotenv
from .models import Recipient, Category, Game, Team
from .forms import TeamForm

# Load environment variables
load_dotenv()

# Set up logging
logger = logging.getLogger(__name__)

# Store OTPs in a dictionary (For production, use a database)
otp_storage = {}

# Home page
def home(request):
    return render(request, 'index.html')

# ✅ Send OTP via email
@csrf_exempt
def send_otp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get("email")

            if not email:
                return JsonResponse({'error': 'Email is required'}, status=400)

            otp = random.randint(1000, 9999)  # Generate OTP
            otp_storage[email] = otp
            print(f"Generated OTP for {email}: {otp}")

            # Email settings
            subject = "Your OTP Code"
            message = f"Hello,\n\nYour OTP for login is: {otp}\n\nDo not share this code with anyone."
            from_email = os.getenv('DEFAULT_FROM_EMAIL')
            recipient_list = [email]

            # Send OTP via email
            try:
                send_mail(subject, message, from_email, recipient_list)
                return JsonResponse({'message': 'OTP sent successfully!'})
            except Exception as e:
                logger.error(f"Error sending email: {e}")
                return JsonResponse({'error': 'Error sending email'}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# ✅ Verify OTP and register user
@csrf_exempt
def verify_otp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_email = data.get("email")
            user_otp = data.get("otp")
            user_name = data.get("name")

            if not user_email or not user_otp:
                return JsonResponse({'error': 'Email and OTP are required'}, status=400)

            if user_email in otp_storage and otp_storage[user_email] == int(user_otp):
                del otp_storage[user_email]  # OTP verified, remove it

                # Check if user already exists
                recipient, created = Recipient.objects.get_or_create(email=user_email, defaults={'name': user_name})
                
                return JsonResponse({'message': 'OTP verified successfully!'})
            else:
                return JsonResponse({'error': 'Invalid OTP'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# ✅ Pages rendering
def acem(request):
    email = request.POST.get('email')
    return render(request, 'acem.html', {'email': email})

def social(request):
    return render(request, 'social.html')

def upcoming(request):
    return render(request, 'upcoming.html')

def videos(request):    
    return render(request, 'video.html')

def gallery(request):
    return render(request, 'gallery.html')

# ✅ Fetch games under a category
def category_games(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    games = category.games.all()
    context = {
        'category': category,
        'games': games,
    }
    return render(request, 'category_games.html', context)

# ✅ Fetch teams for a game
def game_leaderboard(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    teams = game.teams.order_by('-points')
    context = {
        'game': game,
        'teams': teams,
    }
    return render(request, 'game_leaderboard.html', context)

def leaderboard(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category', categories.first().name)
    games = Game.objects.filter(category__name=selected_category)
    selected_game = request.GET.get('game', games.first().name if games.exists() else None)
    leaderboard = Team.objects.filter(game__name=selected_game).order_by('-points') if selected_game else []

    context = {
        'categories': categories,
        'selected_category': selected_category,
        'games': games,
        'selected_game': selected_game,
        'leaderboard': leaderboard,
    }
    return render(request, 'leaderboard.html', context)

def add_team(request, game_id):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            team = form.save(commit=False)
            team.game_id = game_id
            team.save()
            return redirect('game_leaderboard', game_id=game_id)
    else:
        form = TeamForm()
    return render(request, 'add_team.html', {'form': form, 'game_id': game_id})

def update_team(request, game_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        for team_data in data['teams']:
            team = get_object_or_404(Team, id=team_data['id'])
            team.points = team_data['points']
            team.won = team_data['won']
            team.lost = team_data['lost']
            team.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
