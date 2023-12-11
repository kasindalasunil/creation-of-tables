from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)
    def __str__(self):
        return str(self.deptno)+self.dname
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    deptno=models.OneToOneField(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.deptno)+self.ename

class Bonus(models.Model):
    empno=models.OneToOneField(Emp,on_delete=models.CASCADE)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()
    def __str__(self):
        return self.job

class Salgrade(models.Model):
    grade=models.CharField(max_length=100)
    losal=models.PositiveIntegerField()
    hisal=models.PositiveIntegerField()
    def __str__(self):
        return self.grade




