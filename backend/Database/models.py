from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    date_add = models.DateField(auto_now_add = True) 
    
    def __str__(self):
        return f'{self.name} | {self.price} | {self.stock} | {self.date_add}'
