from . import views
from django.urls import path

urlpatterns = [
    path('', views.IdeaList.as_view(), name='home'),
    path('<slug:slug>/', views.idea_detail, name='idea_detail'),
]