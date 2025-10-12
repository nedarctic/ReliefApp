from rest_framework import serializers
from .models import Disaster, SafeZone, Update

class SafeZoneSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = SafeZone
        fields = ['id', 'name', 'latitude', 'longitude', 'capacity', 'description', 'image', 'image_url']
        
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
        
class UpdateSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Update
        fields = ['id', 'author', 'author_username', 'timestamp', 'message']
        read_only_fields = ['timestamp', 'author_username']
        
class DisasterSerializer(serializers.ModelSerializer):
    safe_zones = SafeZoneSerializer(many=True, read_only=True)
    updates = UpdateSerializer(many=True, read_only=True)
    created_by_username = serializers.ReadOnlyField(source='created_by.username')
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Disaster
        fields = ['id', 'name', 'disaster_type', 'description', 'location', 'date', 'created_by', 'created_by_username', 'safe_zones', 'updates', 'image', 'image_url']
        read_only_fields = ['created_by_username', 'safe_zones', 'updates']
        
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None