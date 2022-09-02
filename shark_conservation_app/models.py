from django.contrib.auth import get_user_model
from django.db import models

class Shark(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default=" ")
    location = models.CharField(max_length=50, default=" ")
    avg_length = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    diet = models.CharField(max_length=100, default=" ", blank=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.name}"