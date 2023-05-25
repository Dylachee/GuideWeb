from django.contrib import admin
from .models import Category, TraditionalFood , Cart , Order , Favorite

admin.site.register([Category, 
                    TraditionalFood,
                    Cart, 
                    Order , 
                    Favorite])

# Ebal ya eto