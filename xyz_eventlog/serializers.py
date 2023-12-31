# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from xyz_restful.mixins import IDAndStrFieldSerializerMixin
from rest_framework import serializers
from . import models

class EventSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Event
        exclude = ()
