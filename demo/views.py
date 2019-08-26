from django.http import HttpResponse


def index(request):
    print(11)
    return HttpResponse("Hello, world. You're at the polls index.")