from django.urls import path
from . import views

app_name = "series"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:serieId>/', views.detail, name='detail'),
]