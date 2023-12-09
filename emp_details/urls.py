from django.urls import path

from emp_details import views

urlpatterns = [
    path('', views.read, name="read"),
    path('delt/<int:id>/', views.delete, name="delt"),
    path('add1', views.add1, name="create"),
    path("update/<int:id>/",views.update,name="update")
]