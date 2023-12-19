from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Customer


class Command(BaseCommand):
    help = "Creates customer"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help='Customer name')
        parser.add_argument('email', type=str, help='Customer email')
        parser.add_argument('phone', type=str, help='Customer phone')
        parser.add_argument('address', type=str, help='Customer address')

    def handle(self, *args, **kwargs):
        # customer = Customer(name='John', email='john1111@gmail.com', phone='88005553535', address='Moskovskaya street 37')
        # customer = Customer(name='Neo', email='neo2222@gmail.com', phone='89996667575', address='Vladimirskaya street 12')
        # customer = Customer(name='Max', email='max3333@gmail.com', phone='87874446080', address='Ivanovskaya street 56')
        name, email, phone, address = kwargs['name'], kwargs['email'], kwargs['phone'], kwargs['address']
        customer = Customer(name=name, email=email, phone=phone, address=address)
        customer.save()
        self.stdout.write(f'{customer}')