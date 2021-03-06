import random

from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed
from lists import models as list_models
from rooms import models as room_models
from users import models as user_models

NAME = "lists"


class Command(BaseCommand):
    help = f"This command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            list_models.List,
            number,
            {
                "user": lambda x: random.choice(users),
            },
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))

        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(
                *to_add
            )  # to_add 는 QuerySet 즉, array 가 될 것이기 때문에 * 을 붙여서 array 안의 요소가 들어가도록 함

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
