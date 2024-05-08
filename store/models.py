from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    origina_price = models.DecimalField(max_digits=20, decimal_places=2)
    now_price = models.DecimalField(max_digits=20, decimal_places=2)
    link = models.CharField(max_length=1000)
    product_image = models.ImageField(upload_to='product')
    product_image2 = models.ImageField(upload_to='product', null=True, blank=True)
    product_image3 = models.ImageField(upload_to='product', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.product_name
    

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name
    
