from django.shortcuts import render,redirect
from django.views import View
from employeeApp.models import Employee
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'index.html')
    
class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    
    def post(self,request):
        name=request.POST.get('name')
        salary=request.POST.get('salary')
        desig=request.POST.get('desig')
        email=request.POST.get('email')
        Employee.objects.create(name=name,salary=salary,designation=desig,email=email)
        return redirect('home_view')
    

class EmployeeList(View):
    def get(self,request):
        emp=Employee.objects.all()
        return render(request,'emp_list.html',{'data':emp})
    
class DeleteEmployee(View):
    def get(self,request,*args,**kwargs):  #kwargs formil aane id kittuka -kwrrgs{id:3}
        id=kwargs.get('id')   # this step shows we take the id from the keyword dictionary
        emp=Employee.objects.get(id=id)  #now we wanted to get the datas related to the id from the database,which is shows in this step
        emp.delete()
        return redirect('list_view')
class UpdateEmployee(View):
    def get(self,request,*args,**kwargs):
         id=kwargs.get('id') 
         emp=Employee.objects.get(id=id)
         return render(request,'edit.html',{'data':emp})
    def post(self,request,*args,**kwargs):
        id=kwargs.get('id')
        employee=Employee.objects.get(id=id)
        name=request.POST.get('name')
        salary=request.POST.get('salary')
        desig=request.POST.get('desig')
        email=request.POST.get('email')
        employee.name=name
        employee.salary=salary
        employee.designation=desig
        employee.email=email
        employee.save()
        return redirect('list_view')
        
    
