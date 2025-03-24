from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_nfactorial, name='hello_nfactorial'),
    path('<int:first>/add/<int:second>/', views.add_numbers, name='add_numbers'),
    path('transform/<str:text>/', views.upper_case, name='upper_case'),
    path('check/<str:word>/', views.check_palindrome, name='check_palindrome'),
    path('calc/<int:first>/<str:operation>/<int:second>/', views.calculator, name='calculator'),
]

