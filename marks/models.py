from django.db import models

class Marks(models.Model):
    student_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    module_code = models.CharField(max_length=20)
    classwork1 = models.IntegerField()
    classwork2 = models.IntegerField()
    classwork3 = models.IntegerField()

    def __str__(self):
        return f"{self.student_name} - {self.module_code}"