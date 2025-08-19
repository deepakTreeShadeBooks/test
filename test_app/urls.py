from django.urls import path
from .views import paragraph_form_view

urlpatterns = [
    path('submit/', paragraph_form_view, name='paragraph_form'),
]
