from django.db import models

# Create your models here.
class college(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=200)
    clocation=models.CharField(max_length=50)
    cusn=models.CharField(max_length=10)
    cdepartment=models.CharField(max_length=200)

    def __str__(self) :
        return self.cname
