from django.views.generic import TemplateView
from django.urls import path
from.import views


urlpatterns = [
    path('temp-extends/', TemplateView.as_view(template_name='child.html')),
    path('test/', )
    path('', views.index),
]
