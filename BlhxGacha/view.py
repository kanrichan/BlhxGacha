from django.http import HttpResponse, HttpRequest
from BlhxGacha.BlhxGacha.build import build_ten

pool = {
    "/blhx/light": "轻型池",
    "/blhx/heavy": "重型池",
    "/blhx/special": "特型池",
    "/blhx/up": "活动池"
}


def Gacha(request):
    file = build_ten(pool[request.path], request.GET["seed"])
    picture = open(file, "rb")
    return HttpResponse(picture.read(), content_type='image/jpg')
