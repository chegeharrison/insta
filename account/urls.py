from django.urls import path
from account.views import SignUpView

urlpatterns=[
    path('sign_up/', SignUpView.as_view(), name='signup'),
]