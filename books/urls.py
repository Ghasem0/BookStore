from django.urls import path
from . import views

urlpatterns = [
    path('', views.BooksListView.as_view(), name='books_list'),
    path('create/', views.BooksCreateView.as_view(), name = 'book_create'),
    path('<int:pk>/detail/', views.BooksDetailView.as_view(), name= 'book_detail'),
    path('<int:pk>/update/', views.BooksUpdateView.as_view(), name= 'book_update'),
    path('<int:pk>/delete/', views.BooksDeleteView.as_view(), name= 'book_delete'),

]