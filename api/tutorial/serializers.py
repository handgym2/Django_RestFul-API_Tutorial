from tutorial.models import Myclass, Usnclass
from rest_framework import serializers


class MyclassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Myclass
        fields = ('ban','student', 'teacher',)

class UsnclassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usnclass
        fields = ('ban',)
