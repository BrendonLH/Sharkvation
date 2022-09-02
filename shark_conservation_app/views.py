from django.views.generic import TemplateView
from .models import Shark
from rest_framework import generics
from .serializer import SharkSerializer

class HomePageView(TemplateView):
    template_name = 'home.html'

class SharkList(generics.ListAPIView):
    queryset = Shark.objects.all()
    serializer_class = SharkSerializer

class SharkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shark.objects.all()
    serializer_class = SharkSerializer
