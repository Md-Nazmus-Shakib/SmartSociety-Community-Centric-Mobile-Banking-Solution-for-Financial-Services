from . import views
from django.urls import path

urlpatterns = [
    path('wallet/', views.get_wallet, name='get_wallet'),
]