from rest_framework import serializers
from .models import Intake



class Intakeserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intake
        fields = ['id', 'intakename', 'enddate', 'startdate']



