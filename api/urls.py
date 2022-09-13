from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= "index"),
    path('task-list/',views.taskList,name='task-list'),
    path('task-list/<int:pk>',views.taskSingle,name='task-single'),
    path('task-create/',views.taskCreate,name='task-create'),
    path('task-update/<int:pk>',views.taskUpdate,name='task-update'),
    path('task-delete/<int:pk>',views.taskDelete,name='task-delete'),
    
]
