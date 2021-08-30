from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось задеплоить на боевой сервер!')


def second_page(request):
    return HttpResponse('А это вторая страница')
