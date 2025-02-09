from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send-otp/', views.send_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('acem/', views.acem, name='acem'),
    path('social/', views.social, name='social'),
    path('upcoming/', views.upcoming, name='upcoming'),
    path('videos/', views.videos, name='videos'),
    path('gallery/', views.gallery, name='gallery'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('category/<int:category_id>/', views.category_games, name='category_games'),
    path('game/<int:game_id>/', views.game_leaderboard, name='game_leaderboard'),
    path('game/<int:game_id>/add-team/', views.add_team, name='add_team'),  # Updated route
    path('game/<int:game_id>/update-team/', views.update_team, name='update_team'),
]
