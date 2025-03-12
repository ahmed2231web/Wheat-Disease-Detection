from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.UploadImageView.as_view(), name='upload-image'),
    path('chat/', views.ChatWithGeminiView.as_view(), name='chat'),
]