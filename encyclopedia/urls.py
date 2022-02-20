from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page_name>/", views.view_entry, name="page"),
    path("wiki/<str:page_name>/edit", views.edit_page, name="edit"),
    path("wiki/<str:page_name>/save", views.save_page, name="save"),
    path("new", views.new_page, name="new"),
    path("new/save", views.save_new_page, name="save_new"),
    path("search", views.search, name="search"),
    path("random", views.arbitrary, name="random"),
]
