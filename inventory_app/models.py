from django.db import models
from rest_framework import serializers

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()

    def __str__(self):
    	return self.title

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'amount')
