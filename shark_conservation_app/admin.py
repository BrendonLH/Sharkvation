from django.contrib import admin
from .models import Shark


my_models = [Shark]
admin.site.register(Shark)

