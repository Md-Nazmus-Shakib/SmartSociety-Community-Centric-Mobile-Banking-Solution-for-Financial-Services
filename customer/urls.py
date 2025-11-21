from django.urls import path
from .import views
urlpatterns = [
    path('profile/', views.customer_profile_view, name='customer-profile'),
    path('send-money/', views.send_money_view, name='customer-send-money'),
    # path('edit/', views.edit_view, name='customer-edit'),
]