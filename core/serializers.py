from rest_framework import serializers
from core.models import Species


class SpecieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Species
        fields = (
            'thumbnail', 'specie_name', 'sampling_method', 'latitude', 'longitude',
            'site_description', 'project_name', 'kinyarwanda_name')