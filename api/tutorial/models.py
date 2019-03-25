from django.db import models

# Create your models here.
class Myclass(models.Model):
    ban = models.ForeignKey('Usnclass',on_delete=models.CASCADE)
    student = models.CharField(max_length=30)
    teacher = models.CharField(max_length=30)

    def __str__(self):
        return self.student

class Usnclass(models.Model):
    ban = models.IntegerField(default=1)

    def __str__(self):
        return str(self.ban)
