from django.http import HttpResponse

def index(request):
    return HttpResponse('This is the index page', content_type='text/plain')
