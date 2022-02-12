from django.urls import path
from . import views
urlpatterns = [
    path('', views.ind, name='index-page'),
    path('signup/', views.signup, name='signup-page'),
    path('prediction/', views.prediction, name='prediction-page'),
]
