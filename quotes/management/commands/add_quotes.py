from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Quote


class Command(BaseCommand):
    help = "Adds quotes to the database"

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(10000):
            Quote.objects.create(name=fake.name(), quote=fake.text())

        print("Completed!!! Check your database.")
