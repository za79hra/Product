from rest_framework import serializers
from .models import User
from bcrypt import hashpw, gensalt

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         hashed_password = hashpw(password.encode('utf-8'), gensalt())
#         user = User.objects.create(password=hashed_password, **validated_data)
#         return user

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password')



from rest_framework import serializers
from django.contrib.auth import get_user_model
import re
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        if not re.match("^[a-zA-Z]+$", value):
            raise serializers.ValidationError('Username can only contain English letters.')
        if value.isnumeric():
            raise serializers.ValidationError("Username should not contain numbers.")
        return value

    def validate_password(self, value):
        special_characters = ['%', '$', '&', '...']
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        if not any(char in value for char in special_characters):
            raise serializers.ValidationError('Password must contain at least one of the following characters: %, $, &, ...')
        return value

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user











# from django.contrib.auth import authenticate
# from django.contrib.auth.password_validation import validate_password
# from django.core import exceptions
# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, hashers


# class LoginSerializer(serializers.Serializer):

#     username = serializers.CharField(
#         max_length=100,
#         validators=[UniqueValidator(queryset=User.objects.all(), message="Username already exists.")]
#     )
#     password = serializers.CharField(max_length=100)

#     def validate_username(self, value):
#         if value.isnumeric():
#             raise serializers.ValidationError("Username should not contain numbers.")
#         if not value.isalpha():
#             raise serializers.ValidationError("Username should only contain English letters.")
#         return value

#     def validate_password(self, value):
#         if len(value) < 8:
#             raise serializers.ValidationError("Password should be at least 8 characters long.")
#         try:
#             validate_password(value)
#         except exceptions.ValidationError as e:
#             raise serializers.ValidationError(str(e))
#         return value
   
    # def validate(self, data):
    #     username = data.get('username')
    #     password = data.get('password')
    #     user = authenticate(username=data['username'], password=data['password'])
    #     if not user:
    #         raise serializers.ValidationError("Invalid username or password.")
    #     data['user'] = user
    #     return data
