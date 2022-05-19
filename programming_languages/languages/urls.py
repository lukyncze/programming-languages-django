from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.JazykyListView.as_view(), name='list'),
    path('detail/<int:pk>', views.JazykyDetailView.as_view(), name='detail'),
    path('jazyky/create/', views.JazykyCreate.as_view(), name='jazyky-create'),
    path('jazyky/<int:pk>/update/', views.JazykyUpdate.as_view(), name='jazyky-update'),
    path('jazyky/<int:pk>/delete/', views.JazykyDelete.as_view(), name='jazyky-delete'),

]