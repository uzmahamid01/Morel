from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.URLField()
    brand = models.CharField(max_length=100)
    product_link = models.URLField()
    category = models.CharField(max_length=50, choices=[('Men', 'Men'), ('Women', 'Women'), ('Accessories', 'Accessories'), ('Shoe Wear', 'Shoe Wear'), ('Stoles', 'Stoles')], default='uncategorized')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name