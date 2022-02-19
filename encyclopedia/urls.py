from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:search_string>/", views.view_page, name="page"),
    path("search", views.search, name="search"),
    path("edit", views.edit, name="edit"),
    #path("save", views.save, name="save")

]
