from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('123', include('hello.urls')),
    path('hello2/', include('hello2.urls')),
    path('admin/', admin.site.urls),
]
