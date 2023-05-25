from django.db import models

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

    def __str__(self):
        return self.name
    
