from django.db import models

class ProfilesModel(models.Model):
    user = models.OneToOneField('accounts.AccountsModel', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    
