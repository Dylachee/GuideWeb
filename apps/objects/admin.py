from django.contrib import admin
from .models import Category, TraditionalFood

admin.site.register([Category, TraditionalFood])