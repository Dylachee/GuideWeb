from django.db import models

class TraditionalClothing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='food_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('objects.Category', on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
class TraditionalSouvenirs(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='food_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('objects.Category', on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name