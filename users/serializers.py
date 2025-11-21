from . import models
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True)
    class Meta:
        model = models.User
        fields = [  
            'username',
            'email',
            'role',
            'mobile_no',
            'is_active',
            'password',
            'account_number',
            # 'balance',
            'created_at',]
        #exclude = ['account_number', 'balance','created_at']
        read_only_fields = ['account_number','created_at','is_active',] # account number automatically generated, balance managed by system
    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
        