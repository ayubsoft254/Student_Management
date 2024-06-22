from django.db import models

CHOICES = [
    ('BIT','BIT'),
    ('BBIT','BBIT'),
    ('BCOM','BCOM'),
    ('BED','BED'),
]

class Student(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    course=models.CharField(max_length=20,choices=CHOICES)

    def __str__(self):
        return f'{self.fname} {self.lname}'        