from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Product


class Command(BaseCommand):
    help = "Creates product"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('product_quantity', type=int, help='Product quantity')

    def handle(self, *args, **kwargs):
        name, description, price, product_quantity = kwargs['name'], kwargs['description'], kwargs['price'], kwargs['product_quantity']
        product = Product(name=name, description=description, price=price, product_quantity=product_quantity)
        product.save()
        self.stdout.write(f'{product}')