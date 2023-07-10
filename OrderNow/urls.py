from django.urls import path
from . import views

urlpatterns = [
    # path('example/', views.example_view, name='example'),
    path('register/', views.Register.as_view(), name='register' ),
    
]
