import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

def upload_to_func(instance, filename):
    return f'uploads/{str(instance.semester)}/user_{instance.user.username}/{filename}'

class User(AbstractUser):
    pass

class Semester(models.Model):
    year_interval = models.CharField(max_length=9)
    period_name = models.CharField(max_length=6)
    active = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['active'],
                condition=models.Q(active=True), name='unique_active')
        ]

    def __str__(self):
        return self.year_interval + " " + self.period_name

class ProgramOutcome(models.Model):
    code = models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return self.code

class Course(models.Model):
    code = models.CharField(max_length=9)
    name = models.CharField(max_length=120)
    program_outcomes = models.ManyToManyField(ProgramOutcome)

    def __str__(self):
        return self.code

class ProgramOutcomeFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    pc_file = models.FileField(upload_to=upload_to_func)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return os.path.basename(self.pc_file.name) + " - " + self.user.username
    
    def filename(self):
        return os.path.basename(self.pc_file.name)

class Student(models.Model):
    no = models.CharField(max_length=11)
    name = models.CharField(max_length=60)
    transfer_student = models.BooleanField(default=False)
    double_major_student = models.BooleanField(default=False)
    graduated_on = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class ProgramOutcomeResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    program_outcome = models.ForeignKey(ProgramOutcome, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    satisfaction = models.IntegerField()

    def __str__(self):
        return self.student.name + " - " + self.course.code + " - [" + \
            self.program_outcome.code + "] - " + str(self.semester) + " - " + \
                str(self.satisfaction)