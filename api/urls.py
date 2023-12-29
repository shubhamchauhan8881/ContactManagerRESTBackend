from django.urls import path,include
from . import views

urlpatterns = [
    path('api/v1/contacts/', views.showContacts.as_view()),
    path('api/v1/contacts/<int:pk>/', views.showContacts.as_view()),
    path('api/v1/contacts/new/', views.AddNewContact.as_view()),
    path('api/v1/contacts/delete/<int:pk>/', views.DeleteContact.as_view()),
    path('api/v1/contacts/mark-fav/<int:pk>/', views.MarkFav.as_view()),
    path('api/v1/contacts/search/<str:search_string>/', views.Search.as_view()),
]
