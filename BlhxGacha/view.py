from django.http import HttpResponse, HttpRequest
from BlhxGacha.BlhxGacha.build import build_ten

pool = {"light": "轻型池", "heavy": "重型池", "special": "特型池", "activity": "活动池"}


def Gacha(request):
    file = build_ten(pool[request.GET["type"]], request.GET["seed"])
    picture = open(file, "rb")
    return HttpResponse(picture.read(), content_type='image/jpg')
