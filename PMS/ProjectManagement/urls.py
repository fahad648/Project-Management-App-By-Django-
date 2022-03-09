from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='Emp_form'),
    path('show', views.show, name='Emp_show'),
    path('<int:id>/',views.add,name='Emp_update'),
    path('delete/<int:id>/',views.delete,name='Emp_delete'),
    path('showProject/', views.showProject, name='showProject'),

    #Employee SECTION
    path('EmpView', views.empView, name='EmpView'),
    path('EmpPortal/<int:id>', views.empPortal, name='EmpPortal'),
]