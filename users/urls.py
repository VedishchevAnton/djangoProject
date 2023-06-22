from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import ProfileView, RegisterDoneView, VerifyEmailView, RegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('verify/<int:pk>/', VerifyEmailView.as_view(), name='verify_email'),
]
