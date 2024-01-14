from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>/', views.details, name='details'),  # Add a trailing slash
    path('members/salon/<str:identifiant>/<int:score>/', views.salon, name='salon'),
    path('members/SLOT/<str:identifiant>/<int:score>/', views.SLOT, name='SLOT'),
    path('members/roulette/<str:identifiant>/<int:score>/', views.roulette, name='roulette'),
    path('members/cards/<str:identifiant>/<int:score>/', views.cards, name='cards'),
    path('members/account/', views.account, name='account'),
    path('members/authenticate/', views.authenticate_user, name='authenticate_user'),
    path('members/register/', views.register_user, name='register_user'),
    
]



