from django.urls import path
from django.contrib.auth.decorators import login_required

from main import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'paintings'),
    path('profile/<int:pk>', login_required(views.Profile.as_view()), name = 'view-profile'),
    path('artists', login_required(views.Artists.as_view()), name = 'artists'),
    path('artists/<int:artist_id>/add-painting', login_required(views.AddPainting.as_view()), name = 'add-painting')
]