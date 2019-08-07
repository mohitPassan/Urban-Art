from django.urls import path

from main import views

urlpatterns = [
    path('', views.HomePage.as_view()),
    path('paintings/', views.Index.as_view(), name = 'paintings')
]