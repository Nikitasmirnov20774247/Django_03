from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.TextField()
    date_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'customer name: {self.name}, email: {self.email}, phone: {self.phone}, address: {self.address}, date of registration: {self.date_reg}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'product name: {self.name}, description: {self.description}, price: {self.price}, product quantity: {self.product_quantity}, date of addition: {self.date_add}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'order: {self.customer}, product: {self.product.all()}, total price: {self.total_price}, order date: {self.order_date}'