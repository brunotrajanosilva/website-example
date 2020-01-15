from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('bedrooms/', views.BedroomsView.as_view(), name="bedrooms"),
    path('bedrooms/<int:pk>', views.BedroomDetail.as_view(), name="bedroom"),
]

