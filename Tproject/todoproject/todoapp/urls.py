
from . import views
from django.urls import path


urlpatterns = [

    path('',views.add,name='add'),
    #path('details/',views.details,name='details'),
    path('delete/<int:taskid>/',views.delete, name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('cbvhome/', views.TodoListview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TodoDetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TodoUpdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TodoDeleteview.as_view(), name='cbvdelete'),

]
