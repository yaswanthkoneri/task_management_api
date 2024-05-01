from django.urls import path,include
from task_app.api.views import task_list, task_detail

urlpatterns = [
    path('list/', task_list, name='task_list'),
    path('<int:pk>', task_detail, name='task_detail'),
]
