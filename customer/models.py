from django.db import models
from users.models import User
from wallet.models import Wallet
from users.serializers import UserSerializer

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'customer',primary_key=True,db_column='account_number')
    # wallet_balance = models.OneToOneField(Wallet, on_delete=models.CASCADE,related_name='customer_wallet',)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.user.account_number}"

# Create your models here.
