from django.db import models

# Create your models here.

class student (models.Model):
    student_name=models.CharField( 'Student name',max_length=30,null=False)
    dept=(
        ('CSE','Computer Science'),
        ('MH','Mech'),
        ('CV','Civil')
    )

    department=models.CharField('Departmrnt',choices=dept,blank=True,null=True,max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name

class library(models.Model):
    lib_name=models.CharField( 'library name',max_length=30,null=True)
    book=models.CharField( 'book',max_length=30,null=False)
    def __str__(self):
        return self.lib_name

class section(models.Model):
        advisor=models.OneToOneField('teacher',on_delete=models.SET_NULL,null=True)
        students=models.ManyToManyField('student',null=False)
        def __str__(self):
            return self.advisor


class teacher(models.Model):
        teacher=models.CharField( 'Teacher name',max_length=30,null=False)
        timestamp=models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return self.teacher

class book(models.Model):
        book=models.CharField( 'book name',max_length=30,null=False)
        def __str__(self):
            return self.book

