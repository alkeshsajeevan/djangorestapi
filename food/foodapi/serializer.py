from rest_framework import serializers
from .models import Food


class Foofserializer(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields=('name','description')
