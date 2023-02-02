from django.urls import path
from tasks.views import create_task, show_my_tasks, edit_task


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("<int:id>/edit/", edit_task, name="edit_task"),
]
