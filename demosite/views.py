from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello from Django</h1>')

def about(request):
    return HttpResponse('<h1>This is about page</h1>')

def contact(request):
    return HttpResponse('<h1>This is contact page</h1>')

def address(request):
    return HttpResponse('<h1>This is address page</h1>')

def technology(request):
    return HttpResponse('<h1>This is technology page</h1>')

def web(request):
    return HttpResponse('<h1>This is web page</h1>')

def mobile(request):
    return HttpResponse('<h1>This is mobile page</h1>')

def desktop(request):
    return HttpResponse('<h1>This is desktop page</h1>')
