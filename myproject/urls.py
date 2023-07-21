from django.urls import path
from chat import views

urlpatterns = [
    path('login/', views.login),
    path('send_message/', views.send_message),
    # 其他URL模式...
]
