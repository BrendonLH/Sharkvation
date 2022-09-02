from django.urls import path

from .views import HomePageView, SharkList, SharkDetail

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sharks/', SharkList.as_view(), name="sharks"),
    path('<int:pk>', SharkDetail.as_view(), name='shark_detail'),
]