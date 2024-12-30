from django.urls import path
from .views import UserLoginView, PanelView, UserListView, UserCreateView, UserUpdateView
from django.contrib.auth import views as auth_views

app_name = "app_login"

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('panel/', PanelView.as_view(), name='panel'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app_login/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app_login/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app_login/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='app_login/password_reset_complete.html'), name='password_reset_complete'),
]