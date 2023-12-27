from rest_framework import serializers
from .models import User, Preference, Generation, SavedProject


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email']


class PreferenceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Preference
        fields = ['id', 'user', 'projectinterests', 'toolsknown', 'toolsdesiredtolearn', 'topicinterests']


class GenerationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Generation
        fields = ['id', 'user', 'title', 'description', 'tools', 'difficulty', 'time']


class SavedProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    project = GenerationSerializer()
    class Meta:
        model = SavedProject
        fields = ['id', 'user', 'project']