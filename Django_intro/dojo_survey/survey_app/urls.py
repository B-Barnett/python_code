from django.urls import path
from . import views

urlpatterns = [
	path('', views.index), #Route to show the form
    path('result', views.result), #Route to process the form
    path('display', views.display)
]