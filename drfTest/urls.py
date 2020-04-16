
from django.urls import path
from . import views

app_name = 'drfTest'

urlpatterns = [
    path('test/',views.GetMessageView.as_view()),
]