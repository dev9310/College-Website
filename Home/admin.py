# filepath: /Z:/Django/College Project/Event/Home/admin.py
from django.contrib import admin
from .models import Recipient, Category, Game, Team

@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'joined_at')
    search_fields = ('name', 'email')

admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Team)
