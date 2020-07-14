from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<html><body>Teste config setup</body></html>', content_type='text/html')
