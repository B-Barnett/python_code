from django.urls import path, include

urlpatterns = [
	path('', include('number_app.urls')),
]