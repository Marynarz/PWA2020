from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *


def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return HttpResponse(user)