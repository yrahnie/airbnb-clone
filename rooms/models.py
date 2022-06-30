from core import models as core_models
from django.db import models
from django_countries.fields import CountryField
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """RoomType Object Definition"""

    class Meta:
        verbose_name_plural = "Room Types"
        ordering = ["name"]


class Amenity(AbstractItem):
    """Amenity Object Definition"""

    class Meta:
        verbose_name_plural = "Amenities"

    pass


class Facility(AbstractItem):
    """Facility Object Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """HouseRule Object Definition"""

    class Meta:
        verbose_name_plural = "House Rules"


class Photo(core_models.TimeStampedModel):
    """Photo Object Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):
    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

    # ForeignKey - room type 은 여러 개 중에 하나만 선택 가능.
    # models.SET_NULL - room type 을 삭제하더라도 ROOM 은 삭제되지 않도록.
    # null=True - db 에 값이 비어있어도 OK
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):  # admin 에서 클래스명을 다른 것으로 표시하고자 할 때.
        return self.name