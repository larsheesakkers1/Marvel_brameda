from django.urls import path
from . import views

app_name = "characters"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:characterId>/', views.detail, name='detail'),
]