from bridger import serializers
from bridger.serializers import (CharField, IntegerField, Serializer,
                                 TextField, register_resource)

from .models import Religion, Student


class ActionButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "age"]
        
        
class ReligionRepresentationSerializer(serializers.RepresentationSerializer):

    _detail = serializers.HyperlinkField(reverse_name="religion-detail")

    class Meta:
        model = Religion
        fields = ("id", "name", "_detail")


class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = ["id", "name", "_additional_resources"]
        

class StudentSerializer(serializers.ModelSerializer):
    _religion = ReligionRepresentationSerializer(source="religion")
    
    class Meta:
        model = Student
        fields = ['id','name', 'student_details', 'age','religion','_religion']
