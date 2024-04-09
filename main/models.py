from django.db import models

class OrderModel(models.Model):
    """ 
    Модель для готовых товаров
    """
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='media/')
    price = models.IntegerField()
    size = models.CharField(max_length=20)
    mass = models.FloatField()
    description = models.TextField()
    
    # компания, которой принадлежит товар
    company = models.ForeignKey('accounts.AccountsModel', on_delete=models.CASCADE)
    
    # отвечает за находимость товара. Работает примерно как хештеги в запретграме)
    category = models.CharField(max_length=250)
    
    date = models.DateTimeField(auto_now_add=True)
    
    # склад, на котором находится этот товар
    warehouse = models.ForeignKey('accounts.Cities', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        
        
class UserCartModel(models.Model):
    user = models.OneToOneField('accounts.AccountsModel', related_name='user_cart', on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderModel, related_name='products', blank=True)
