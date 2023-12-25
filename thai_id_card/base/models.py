from django.db import models

# Create your models here.
class ID_Image(models.Model):
    name = models.CharField(max_length = 50)
    id_img = models.ImageField(null=True ,blank=True, upload_to='images/')

    def __str__(self):
        return self.name
    
class ID_CARD(models.Model):
    identification_number = models.CharField(max_length = 50,null = True,blank = True)
    name = models.CharField(max_length = 50,null = True,blank = True)
    last_name = models.CharField(max_length = 50,null = True,blank = True)
    date_of_birth = models.DateField(null = True,blank=True)
    date_of_issue = models.DateField(null = True,blank = True)
    date_of_expiry = models.DateField(null = True,blank = True)
    id_card_img = models.ForeignKey(ID_Image,on_delete = models.CASCADE)

    def __str__(self):
        return self.identification_number
