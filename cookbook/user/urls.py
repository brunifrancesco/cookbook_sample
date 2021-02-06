from django.urls import path, include

urlpatterns = [
    path('users/', include('django.contrib.auth.urls')),
]