from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

urlpatterns = [
    path('account/', views.UserAccount.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)