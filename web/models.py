from django.db import models

# Create your models here.
class Bank(models.Model):
    branch              =   models.CharField(max_length=40,verbose_name="نام شعبه")
    account_number      =   models.CharField(max_length=40,verbose_name="شماره حساب")
    card_number         =   models.CharField(max_length=16,verbose_name="شماره کارت",null=True,blank=True)
    shaba_number        =   models.CharField(max_length=26,verbose_name="شماره شبا",null=True,blank=True)
    description         =   models.CharField(max_length=100,verbose_name="توضیحات",null=True,blank=True)

    def __str__(self):
        return "{}-{}".format(self.branch,self.account_number)