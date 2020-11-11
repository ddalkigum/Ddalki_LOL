from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command create many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, default=2, help="How many users create?"
        )

    def handle(self, *args, **options):
        number = options.get(
            "number",
        )
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            number,
            {
                "is_superuser": False,
                "is_staff": False,
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created"))