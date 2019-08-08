from django.urls import path

from auth import views

urlpatterns = [
    path('', views.Login.as_view()),
    path('artistsignup', views.ArtistSignUp.as_view(), name = "aSignUp"),
    path('usersignup', views.UserSignUp.as_view(), name = "uSignUp")

]