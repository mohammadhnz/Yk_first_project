from django.http import HttpResponse
from django.shortcuts import render


def advertiser_management1(request):
    return HttpResponse("Thie is advertiser_management")


def show_message(request):
    context = {
        "advertisers": [
            {
                "name": "ali",
                "ads": [
                    {
                        "title": "sth",
                        "id": 12,
                        "image": "https://static.farakav.com/files/pictures/thumb/01567010.jpg"
                    },
                ]
            }
        ]
    }
    return render(request, "advertiser_management/ads.html", context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id, )
