from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path("", views.notes_home, name="notes_home"),
    path("all/", views.all_notes, name="all_notes"),
    path("category/", views.category_list, name="category_list"),
    path("category/<str:category>/", views.category_notes, name="category_notes"),
    path("note/<int:note_id>/", views.note_detail, name="note_detail"),
]
