from django.contrib import admin
from django.urls import path
from todos.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("cadastrar", TodoCreateView.as_view(), name="todo_create"),
    path("atualizar/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("excluir/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("concluir/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
]
