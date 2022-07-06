from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This command creates amenities"

    def handle(self, *args, **options):
        amenities = [
            "Wifi",
            "Kitchen",
            "Air conditioning",
            "Washing machine",
            "Iron",
            "Free parking",
            "Dryer",
            "Heating",
            "Dedicated workspace",
            "TV",
            "Hair dryer",
            "Pool",
            "Hot tub",
            "EV charger",
            "Cot",
            "Gym",
            "BBQ grill",
            "Breakfast",
            "Indoor fireplace",
            "Smoking allowed",
            "Beachfront",
            "Waterfront",
            "Ski-in/ski-out",
            "Smoke alarm",
            "Carbon monoxide alarm",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
