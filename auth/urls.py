from django.urls import path

from auth import views

urlpatterns = [
    path('', views.Login.as_view(), name = 'home-page'),
    path('artistsignup', views.ArtistSignUp.as_view(), name = "aSignUp"),
    path('usersignup', views.UserSignUp.as_view(), name = "uSignUp"),
    path('logout', views.Logout.as_view(), name = 'logout'),
    path('delete-user/<int:pk>', views.DeleteUser.as_view(), name = 'delete-user'),
    path('delete-artist/<int:pk>', views.DeleteArtist.as_view(), name = 'delete-artist')
]