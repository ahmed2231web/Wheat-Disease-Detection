from django.urls import include, path

urlpatterns = [
    path('disease/', include('disease_detection.urls')),
]