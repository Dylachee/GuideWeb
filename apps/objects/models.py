from django.db import models
from django.contrib.auth import get_user_model
from apps.clothes.models import TraditionalClothing
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class TraditionalFood(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='food_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.OneToOneField(TraditionalFood, on_delete=models.CASCADE, null=True, blank=True)
    clothing = models.OneToOneField(TraditionalClothing, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        food_name = self.food.name if self.food else "No food selected"
        clothing_name = self.clothing.name if self.clothing else "No clothing selected"
        return f"{self.user.username} - Food: {food_name} - Clothing: {clothing_name}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.OneToOneField(TraditionalFood, on_delete=models.CASCADE, null=True, blank=True)
    clothing = models.OneToOneField(TraditionalClothing, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk}"

    def clean(self):
        if not (self.food or self.clothing):
            raise ValidationError("Either food or clothing must be selected.")

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.OneToOneField(TraditionalFood, on_delete=models.CASCADE, null=True, blank=True)
    clothing = models.OneToOneField(TraditionalClothing, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def clean(self):
        if not (self.food or self.clothing):
            raise ValidationError("Either food or clothing must be selected.")