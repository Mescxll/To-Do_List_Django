from django.contrib import admin
from django.urls import path
from todos.views import TodoListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view()),
]
