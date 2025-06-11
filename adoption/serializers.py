from rest_framework import serializers

from adoption.models import Pet


class PetSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Pet
        fields = ['id', 'name', 'age', 'species', 'breed', 'description', 'image', 'owner_name', 'owner_email', 'owner_phone']
