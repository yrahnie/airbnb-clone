from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView

from . import models


class HomeView(ListView):
    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    """RoomDetail Definition"""

    model = models.Room
