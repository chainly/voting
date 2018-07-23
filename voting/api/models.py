# coding: utf-8
from django.db import models

class RadioQuestion(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)


class Answer(models.Model):
    question = models.ForeignKey(RadioQuestion, related_name='answer', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    

class Vote(models.Model):
    answer = models.ForeignKey(Answer, related_name='answer', on_delete=models.CASCADE)
    owner =  models.ForeignKey('auth.User', related_name='vote', on_delete=models.CASCADE, blank=True,)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    
    class Meta:   
        ordering = ('-updated',)