from django import forms

from emp_details.models import Employee


class EmpForm(forms.ModelForm):

    class Meta:
        model= Employee
        fields=('name','employee_id','salary')