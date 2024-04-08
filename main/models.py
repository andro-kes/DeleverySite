from django.db import models

class OrderModel(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='media/')
    price = models.IntegerField()
    size = models.CharField(max_length=20)
    mass = models.FloatField()
    description = models.TextField()
    company = models.ForeignKey('accounts.AccountsModel', on_delete=models.CASCADE)
    category = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    warehouse = models.ForeignKey('accounts.Cities', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
