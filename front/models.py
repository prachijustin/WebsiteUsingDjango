from django.db import models
from django.utils import timezone

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering =["-date"]
