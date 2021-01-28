from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def advertiser_management1(request):
    return HttpResponse("Thie is advertiser_management")


def show_message(request):
    render(request,"advertiser_management/ads.html")


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
