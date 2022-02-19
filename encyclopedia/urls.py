from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page_name>/", views.view_page, name="page"),
    path("wiki/<str:page_name>/edit", views.edit_page, name="edit"),
    path("search", views.search, name="search"),
]
