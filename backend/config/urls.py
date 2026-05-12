from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        'message': 'Backend running successfully'
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]