from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/<int:pk>', views.BlogDetailView.as_view(), name='detalhe-post'),
    path('post/new/', views.BlogCreateView.as_view(), name='new-post'),
    path('post/update/<int:pk>', views.BlogUpdateView.as_view(), name='update-post'),
    path('post/delete/<int:pk>', views.BlogDeleteView.as_view(), name='delete-post'),
]