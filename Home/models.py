from django.db import models

# Recipient Model: Stores users with unique email
class Recipient(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Category Model: Groups different types of games
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Game Model: Represents a specific game under a category
class Game(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='games')
    name = models.CharField(max_length=100, unique=True)
    background_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# Team Model: Represents teams competing in a game
class Team(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=100, unique=True)
    points = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)
    lost = models.PositiveIntegerField(default=0)
    image = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-points', '-won']  # Sort teams by highest points, then most wins

    def __str__(self):
        return f"{self.game} - {self.name} " 
