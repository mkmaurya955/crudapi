from django.shortcuts import render
from django.views.generic import View
from crudapp.models import Employee
from django.http import HttpResponse
import json
from django.core.serializers import serialize
# Create your views here.

class EmployeeDetailsCBV(View):
    def get(self, request, id, *args, **kargs):
        emp=Employee.objects.get(id=id)
        #emp_data={
        #'eno':emp.eno,
        #'ename':emp.ename,
        #'esal':emp.esal,
        #'eaddr':emp.eaddr,
        #}
        #json_data=json.dumps(emp_data)
        json_data=serialize('json',[emp,], fields=('eno','ename','esal'))
        return HttpResponse(json_data,content_type='application/json')
