from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    
    path('login',views.login_admin,name="login"),
    path('logout',views.logout,name="logout"),

    path('book',views.BookList.as_view(),name='book-list'),
    path('book/create', views.BookCreateView.as_view(),
         name='book-create'),
    path('book/<int:pk>', views.BookDetailView.as_view(),
         name='book-detail'),
    path('book/<int:pk>/update', views.BookUpdateView.as_view(),
         name='book-update'),
    path('book/<int:pk>/delete', views.BookDeleteView.as_view(),
         name='book-delete'),
    path('create/admin', views.register_admin,
         name='admin-register'),

]
