from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class RecipeStep(models.Model):
    description = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=80)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    cook_time = models.IntegerField()
    cook_time_units = models.CharField(max_length=80)
    servings = models.IntegerField()
    cover_image = models.ImageField(upload_to="recipes/cover_image/%Y/%m/%d", null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name