'''
Project models for app01
'''
from __future__ import unicode_literals
from django.db import models


class Question(models.Model):
    '''
    Question model
    '''
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    '''
    Choice model
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
