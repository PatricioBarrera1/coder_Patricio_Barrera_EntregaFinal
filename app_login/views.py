from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

class UserLoginView(LoginView):
    template_name = 'app_login/login.html'
    authentication_form = AuthenticationForm
    
class PanelView(LoginRequiredMixin, TemplateView):
    template_name = 'app_login/panel.html'
    
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'app_login/user_list.html'
    context_object_name = "users"

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "app_login/user_create.html"
    success_url = reverse_lazy('app_login:user_list')
    
    def form_valid(self, form):
        form.instance.username = form.instance.email  # Asegura que el username sea igual al email
        return super().form_valid(form)

    def form_valid(self, form):
        messages.success(self.request, "User created successfully!")
        return super().form_valid(form)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'app_login/user_edit.html'
    success_url = reverse_lazy('app_login:user_list')
    
    def form_valid(self, form):
        form.instance.username = form.instance.email  # Asegura que el username sea igual al email
        return super().form_valid(form)