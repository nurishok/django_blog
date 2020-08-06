from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import RegisterView, SigninView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', SigninView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]