from django.urls import path
from django.contrib.auth.decorators import login_required

from main import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'paintings'),
    path('painting/<int:pk>', views.Painting.as_view(), name = 'view-painting'),
    path('profile/<int:pk>', views.ArtistProfile.as_view(), name = 'view-profile'),
    path('artists', views.Artists.as_view(), name = 'artists'),
    path('artists/<int:artist_id>/add-painting', views.AddPainting.as_view(), name = 'add-painting'),
    path('buy-painting/<int:user_id>/<int:artist_id>/<int:painting_id>/', views.Payment.as_view(), name = 'buy-painting'),
    path('thankyou/', views.Success.as_view()),
    path('current-user/', views.CurrentProfile, name = 'current-profile')
]