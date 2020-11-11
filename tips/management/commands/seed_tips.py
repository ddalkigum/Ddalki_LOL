import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from tips.models import Tip
from users.models import User
from champions.models import Champion


class Command(BaseCommand):

    help = "Create Tips"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, default=1, help="How many tips create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        nickname = User.objects.all()
        champion = Champion.objects.all()
        seeder.add_entity(
            Tip,
            number,
            {
                "nickname": lambda x: random.choice(nickname),
                "champion": lambda x: random.choice(champion),
                "recommand": lambda x: random.randint(7, 99),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} tips created"))
