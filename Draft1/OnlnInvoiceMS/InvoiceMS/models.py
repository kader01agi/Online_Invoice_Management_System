from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator

class Client(models.Model):
    ClientUserID = models.CharField(max_length=50, unique=True)
    ClientName = models.CharField(max_length=100)
    ClientEmail = models.EmailField()
    ClientPhone = models.CharField(max_length=20)
    ClientAddress = models.TextField()

class Item(models.Model):
    ItemName = models.CharField(max_length=100)
    ItemBrand = models.CharField(max_length=50)
    ItemDescription = models.TextField()
    ItemUnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ItemQuantity_in_stock = models.IntegerField()

class Salesman(models.Model):
    SalesmanName = models.CharField(max_length=100)
    SalesmanEmail = models.EmailField()
    SalesmanPhone = models.CharField(max_length=20)
    Password = models.CharField(max_length=50)

class Order(models.Model):
    ClientID = models.ForeignKey(Client, on_delete=models.CASCADE)
    ItemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    SalesmanID = models.ForeignKey(Salesman, on_delete=models.CASCADE)

class Invoice(models.Model):
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    Date = models.DateField()
    Total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentStatus = models.CharField(max_length=20)
    DueDate = models.DateField()

class InvoiceItem(models.Model):
    InvoiceID = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    ItemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    Subtotal = models.DecimalField(max_digits=10, decimal_places=2)

class Payment(models.Model):
    InvoiceID = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    PaymentDate = models.DateField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    PaymentMethod = models.CharField(max_length=50)

class User(models.Model):
    UserName = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=50)
    Role = models.CharField(max_length=20)

    