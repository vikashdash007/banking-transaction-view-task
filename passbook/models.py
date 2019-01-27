from django.db import models


from django.conf import settings
User= settings.AUTH_USER_MODEL

# Create your models here.

class Passbook(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    txDate=models.DateTimeField( auto_now_add=True)
    txId=models.CharField(max_length=100,null=False,blank=False)
    txType= models.CharField(max_length=10,null=False,blank=False)
    txAmount=models.DecimalField(decimal_places=3,max_digits=50,null=False,blank=False)

    def __str__(self):
        return self.txId

    @property
    def title(self):
       return self.txId