from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('cashier', 'Cashier'),
        # Add other user types as needed
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='cashier')

    def __str__(self):
        return self.user.username


class Unit(models.Model):
    FullName = models.CharField(max_length=100)
    ShortName = models.CharField(max_length=10)
    Status = models.BooleanField(default=True)  
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=1, blank=True, null=True)

    @classmethod
    def get_unit_choices(cls):
        return [(unit.ShortName, unit.ShortName) for unit in cls.objects.filter(Status=True)]

    def __str__(self):
        return self.FullName

class Product(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50, choices=Unit.get_unit_choices, default='pieces')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    opening_stock = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, blank=True, null=True)
    @classmethod
    def get_product_choices(cls):
        return [(product.name, product.name) for product in cls.objects.filter(status=True)]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        StockMovement.objects.update_or_create(
            opid=self.id,
            defaults={
                'name':self.name,
                'quantity': self.opening_stock,
                'unit': self.unit,
                'channel':"Opening",
            }
        )

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']  

class Stock(models.Model):
    product_name = models.CharField(max_length=255)  # Store the product name
    quantity = models.IntegerField()  # Store the stock quantity
    unit = models.CharField(max_length=50)  # Store the unit associated with the product
    status = models.BooleanField(default=True)  # Status field copied from product

    def __str__(self):
        return f"{self.product_name} - {self.quantity} {self.unit}"
    
class Vendor(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    vendor = models.CharField(max_length=255,)
    panno = models.CharField(max_length=255, blank=True, null=True)  # Changed to CharField
    address = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)  # Changed to CharField
    status = models.BooleanField(default=True)  
    
    @classmethod
    def get_vendor_choices(cls):
        return [(vendor.vendor, vendor.vendor) for vendor in cls.objects.filter(status=True)]

    def __str__(self):
        return f"{self.vendor} - {self.panno} - {self.address} - {self.contact}"

    class Meta:
        ordering = ['vendor']  


class StockMovement(models.Model):
    date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the record is first created
    name = models.CharField(max_length=255,choices=Product.get_product_choices)
    
    opid = models.IntegerField(null=True,blank=True)
    quantity = models.IntegerField()  # Store the stock quantity
    price=models.IntegerField(null=True,blank=True)
    unit = models.CharField(max_length=255,choices=Unit.get_unit_choices) # Store the unit associated with the product (e.g., pieces, kilograms)
    channel = models.CharField(max_length=20)  # Store the channel through which the stock movement occurred (e.g., online, in-store)
    invoice=models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, blank=True, null=True)
    vendor=models.CharField(max_length=255,choices=Vendor.get_vendor_choices, null=True,blank=True)
    pdate=models.DateField(null=True,blank=True)
    sdate=models.DateField(auto_now_add=True,null=True,blank=True)
    payment=models.CharField(max_length=20,null=True,blank=True)



    def __str__(self):
        return f"{self.name} - {self.quantity}{self.channel} {self.unit} on {self.date}"
    def save(self, *args, **kwargs):
       
        super().save(*args, **kwargs)


class Holdsale(models.Model):
    date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the record is first created
    name = models.CharField(max_length=255,choices=Product.get_product_choices)
    
    opid = models.IntegerField(null=True,blank=True)
    quantity = models.IntegerField()  # Store the stock quantity
    unit = models.CharField(max_length=255,choices=Unit.get_unit_choices) # Store the unit associated with the product (e.g., pieces, kilograms)
    channel = models.CharField(max_length=20,blank=True,null=True)  # Store the channel through which the stock movement occurred (e.g., online, in-store)
    invoice=models.IntegerField(blank=True, null=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=1, blank=True, null=True)
    vendor=models.CharField(max_length=255,choices=Vendor.get_vendor_choices, null=True,blank=True)
    pdate=models.DateField(null=True,blank=True)
    sdate=models.DateField(auto_now_add=True,null=True,blank=True)



    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit} on {self.date}"
    def save(self, *args, **kwargs):
       
        super().save(*args, **kwargs)


class Collectionsale(models.Model):
    date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the record is first created
    amount=models.FloatField()
    mode=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.date}"