from rest_framework import serializers
from .models import Operations

class OperationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = [
            'x',
            'y', 
            'result', 
            'slackUsername',
            'operation_type'
        ]
        read_only_fields = ['result', 'slackUsername']
        extra_kwargs = {
            'x':{'write_only':True},
            'y':{'write_only':True} 
        }
        
        
    def create(self, validated_data):
        x = validated_data['x']
        y = validated_data['y']
        operation_type = validated_data['operation_type']
        if operation_type == 'addition':
            result = x + y
        elif operation_type == 'subtraction':
            if x > y:
                result = x - y
            else:
                result = y - x
        elif operation_type == 'multiplication':
            result = x * y
        else:
            result = 0
        operation = Operations.objects.create(x=x, y=y, operation_type = operation_type, result=result)
        return operation