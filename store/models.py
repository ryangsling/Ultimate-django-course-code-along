from django.db import models

# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=100)
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    

class Customer(models.Model):
    BRONZE = 'B'
    SILVER = 'S'
    GOLD = 'G'
    
    MEMBERSHIP_CHOICES = [
        (BRONZE, 'Bronze'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=BRONZE)
    
class Order(models.Model):
    PENDING = 'P'
    COMPLETE = 'C'
    FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETE, 'Complete'),
        (FAILED, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    