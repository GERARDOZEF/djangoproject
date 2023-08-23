
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h3>Hola mundo</h3>")
def about(request):
    return HttpResponse("about")
