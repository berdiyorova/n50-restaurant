from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    # phone_number = serializers.CharField(
    #     max_length=13,
    #     validators=[UniqueValidator(queryset=User.objects.all(), message="This phone number already registered")]
    # )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        try:
            validate_password(password=password)
        except Exception as e:
            raise serializers.ValidationError(str(e))

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
