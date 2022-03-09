from django.db import models

# Create your models here.
class Projects(models.Model):
    project_title = models.CharField(max_length=50)

    def __str__(self):
        return self.project_title



class Employees_new(models.Model):
    Employee_name = models.CharField(max_length=50)
    Employee_id = models.CharField(max_length=50)
    Employee_contact = models.CharField(max_length=50)
    emp_status = models.CharField(max_length=50, null=True)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.Employee_name