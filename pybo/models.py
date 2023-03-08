from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
    subject = models.CharField(max_length=200)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField()
    def __str__(self):
        return str(self.content)
    
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateField() 
    
        
    
    