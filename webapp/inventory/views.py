from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Inventory WebApp is running.')


