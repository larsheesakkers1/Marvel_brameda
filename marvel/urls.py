from django.urls import path

from . import views

app_name = 'marvel'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:comicId>/', views.detail, name='detail'),
]