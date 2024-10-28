from rest_framework import serializers
from django.contrib.auth.models import User



# user serializer start
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User,
        fields = '__all__'
    
