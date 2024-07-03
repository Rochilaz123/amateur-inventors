from . import views
from django.urls import path

urlpatterns = [
    path('', views.IdeaList.as_view(), name='home'),
    path('share-idea/', views.idea_form, name='idea_form'),
    path('edit_idea/<slug:slug>',
        views.idea_edit, name='idea_edit'),
    path('<slug:slug>/', views.idea_detail, name='idea_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
]