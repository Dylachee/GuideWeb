from django.contrib import admin
from .models import Category, TraditionalFood , Cart , Order

admin.site.register([Category, TraditionalFood,
                    Cart, Order])