from django.db import models

class OrderModel(models.Model):
    """ 
    Модель для готовых товаров
    """
    name = models.CharField(max_length=100)
    picture1 = models.ImageField(upload_to='media/', null=True, blank=True)
    picture2 = models.ImageField(upload_to='media/', null=True, blank=True)
    picture3 = models.ImageField(upload_to='media/', null=True, blank=True)
    price = models.IntegerField()
    size = models.CharField(max_length=20)
    mass = models.FloatField()
    description = models.CharField(max_length=250)
    number = models.CharField(max_length=14, null=True, blank=True)
    status = models.CharField(max_length=20, null=True)
    
    # компания, которой принадлежит товар
    company = models.ForeignKey('accounts.AccountsModel', on_delete=models.CASCADE, blank=True, null=True)
    
    # отвечает за находимость товара. Работает примерно как хештеги в запретграме)
    category = models.CharField(max_length=250)
    
    # склад, на котором находится этот товар
    list_warehouse = models.ManyToManyField('accounts.Cities', related_name='warehouse_order')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        
        
class UserCartModel(models.Model):
    user = models.OneToOneField('accounts.AccountsModel', related_name='user_cart', on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderModel, related_name='products', blank=True)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'