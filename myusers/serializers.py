from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = "__all__" #['id','first_name','last_name','email']
        fields =["id","username", "first_name","last_name","email","is_staff","is_active","date_joined","groups","user_permissions","last_login", "is_superuser"]


from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password', ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model()(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user
