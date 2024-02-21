from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    # this will change the page to whatever is typed in after /wiki
    path("<str:page>/", views.page, name="page"),
    path("new_page", views.new_page, name="new_page"),
    path("<str:page>/edit_page/", views.edit_page, name="edit_page")
]
