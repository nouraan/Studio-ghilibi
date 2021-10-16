from rest_framework import serializers


class MyMoviesSerilazier(serializers.Serializer):
    #the fields which will appear in the DRF
    id = serializers.CharField()
    title = serializers.CharField()
    people = serializers.ReadOnlyField()
   