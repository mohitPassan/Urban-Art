from django.urls import path

from main import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'paintings'),
    path('profile/<int:pk>', views.Profile.as_view(), name = 'view-profile'),
    path('artists', views.Artists.as_view(), name = 'artists')
]