from django import forms
from .models import *



class Emp_new(forms.ModelForm):

    class Meta:
        model = Employees_new
        fields = ['Employee_name', 'Employee_id', 'Employee_contact', 'emp_status','project_id']
        label = {
            'Employee_name' : 'First Employee',
            'Employee_id' : 'Employee Id',
            'Employee_contact' : 'Contact', 
            'emp_status' : 'Status', 
            'project_id' : 'Project'
        }