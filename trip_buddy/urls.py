from django.urls import path, include

urlpatterns = [
	path('', include('trip_buddy_app.urls')),
]