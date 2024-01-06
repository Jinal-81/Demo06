from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('register', SignUpView.as_view(), name="register"),
    path('change_fields', FieldsChangeView.as_view(), name="change_fields"),
]