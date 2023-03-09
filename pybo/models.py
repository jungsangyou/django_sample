from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quthor_question')
    objects = models.Manager()
    subject = models.CharField(max_length=200)
    content = models.TextField()
    votor = models.ManyToManyField(User, related_name='votor_question')
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField()
    def __str__(self):
        return str(self.content)
    
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quthor_answer')
    objects = models.Manager()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    votor = models.ManyToManyField(User, related_name='votor_answer')
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateField() 
    
        
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateField()
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    