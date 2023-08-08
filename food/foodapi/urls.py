from django.urls import path
from . import views



urlpatterns = [
    
    path('food/',views.FoodList.as_view(),name=''),
    path('food/<int:pk>',views.FoodDetail.as_view(),name='')
]