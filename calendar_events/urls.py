from django.urls import path
from .views import calendar_view, fetch_facts

urlpatterns = [
    path('', calendar_view, name='calendar_view'),
    path('fetch_facts/', fetch_facts, name='fetch_facts'),
]