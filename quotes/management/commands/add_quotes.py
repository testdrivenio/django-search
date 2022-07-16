from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Quote


class Command(BaseCommand):
    help = "Adds quotes to the database"

    def handle(self, *args, **options):
        fake = Faker()

        quotes_tuple = (Quote(name=fake.name(), quote=fake.text())
                        for _ in range(10_000))

        Quote.objects.bulk_create(quotes_tuple)

        print("Completed!!! Check your database.")
