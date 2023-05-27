from django.contrib import admin
from .models import Tour, Review, Like, Category

admin.site.register([Tour, Review, Like, Category])

