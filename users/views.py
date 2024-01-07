from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from users.helpers import get_users_settings
from users.constants import LOGIN_SUCCESS_MSG
from users.forms import SignUpForm, UserLoginForm, RegistrationSettingsForm
from django.contrib.admin.views.decorators import user_passes_test
from django.shortcuts import render
from django
# Create your views here.

class FieldsChangeView(CreateView):
    form_class = RegistrationSettingsForm
    success_url = reverse_lazy('login')
    template_name = 'user_field_settings.html'

    @staticmethod
    def is_admin(user):
        return user.is_authenticated and user.is_staff

    @user_passes_test(is_admin)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @user_passes_test(is_admin)
    def post(self, request, *args, **kwargs):
        if form.is_valid():
            form.save()
        return render(request, self.template_name)


class DashboardView(TemplateView):
    """class for dashboard page"""
    template_name = 'dashboard.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_settings = get_users_settings(self.request.user)
        form = self.form_class()
        for field_name, field_value in user_settings.items():
            if field_name in form.fields:
                form.fields[field_name].required = field_value['required']
                form.fields[field_name].widget = forms.HiddenInput() if field_value['hidden'] else None
        if self.request.POST:
            context['form'] = form(self.request.POST)
        else:
            context['form'] = form(self.request.GET)

        return context


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class LoginView(SuccessMessageMixin, LoginView):
    """Login View"""
    template_name ='login.html'
    authentication_form = UserLoginForm
    success_message = LOGIN_SUCCESS_MSG


class LogoutView(LoginRequiredMixin, LogoutView):
    """Logout View"""
