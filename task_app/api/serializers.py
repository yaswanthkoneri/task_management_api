from rest_framework import serializers
from task_app.models import Task


def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError('Name should be at least 2 characters long')
    return value
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=100, validators=[name_length])
    # description = serializers.CharField()
    # completed = serializers.BooleanField(default=False)
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)

    # def create(self, validated_data):
    #     return Task.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.completed = validated_data.get('completed', instance.completed)
    #     instance.created_at = validated_data.get('created_at', instance.created_at)
    #     instance.updated_at = validated_data.get('updated_at', instance.updated_at)
    #     instance.save()
    #     return instance
    
    # def delete(self, validated_data):
    #     return Task.objects.delete(**validated_data)
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description should not be same')
        return data
    
