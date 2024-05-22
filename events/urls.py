from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:event_id>/', views.book_event, name='book_event'),
]