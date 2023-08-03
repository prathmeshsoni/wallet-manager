from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_attempt, name="register_attempt"),
    path('token', views.token_send, name="token_send"),
    path('verify/<auth_token>', views.verify, name="verify"),
]
