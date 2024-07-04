from . import views
from django.urls import path

urlpatterns = [
    path('', views.IdeaList.as_view(), name='home'),
    path('share-idea/', views.idea_form, name='idea_form'),
    path('<slug:slug>/edit_idea/<int:idea_id>',
         views.idea_edit, name='idea_edit'),
    path('<slug:slug>/delete_idea/<int:idea_id>',
         views.idea_delete, name='idea_delete'),
    path('<slug:slug>/', views.idea_detail, name='idea_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
