from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def advertiser_mangement1(request):
    return HttpResponse("Thie is advertiser_management")


def show_message(request):
    return JsonResponse({"name": "محمدعلی"})
