from django.contrib import admin
from django.urls import path
from Chat.views import chat_view

urlpatterns = [
    path('', chat_view, name='chat'),
    path("admin/", admin.site.urls),
]
