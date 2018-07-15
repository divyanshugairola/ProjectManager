from django.shortcuts import render,redirect
from app1.forms import UserForm,HeadForm,EmployeeForm
from app1.models import Head,User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'app1/index.html', )


def register(request):
    registered=False
    if not(request.user.is_authenticated):
            
        if request.method=="POST":
            user_form=UserForm(data=request.POST)
            head_form=HeadForm(data=request.POST)



            if user_form.is_valid() and head_form.is_valid():
                user=user_form.save()
                user.set_password(user.password)
                user.save()
                

                head=head_form.save(commit=False)
                head.user=user
                head.save()
                registered=True
                return redirect('login')
            
            else:
                print(user_form.errors and head_form.errors)
        
        else:
            user_form=UserForm()
            head_form=HeadForm()
    

        return render(request,'app1/red.html',
                                        { 'user_form':user_form,
                                            'head_form': head_form, 
                                        'registered':registered })
        
    else:
        return redirect('index')



def empreg(request):
    registered=False
    if not(request.user.is_authenticated):    
        if request.method=="POST":
            user_form=UserForm(data=request.POST)
            emp_form=EmployeeForm(data=request.POST)



            if user_form.is_valid() and emp_form.is_valid():
                user=user_form.save()
                user.set_password(user.password)
                user.save()
                

                emp=emp_form.save(commit=False)
                emp.user=user
                emp.save()
                registered=True
                return redirect('login')
            
            else:
                print(user_form.errors and emp_form.errors)
        
        else:
            user_form=UserForm()
            emp_form=EmployeeForm()
    

        return render(request,'app1/emp.html',
                                        { 'user_form':user_form,
                                            'emp_form': emp_form, 
                                        'registered':registered })
    else:
        return redirect('index')


@login_required
def dashboard(request,pk):
    user=User.objects.get(pk=pk)
    if user in Head():
        a="head"
    if user in Employee():
        a="employee"

    return render(request,'app1/dash.html',{ 'a':a })




# def register(request):
#     registered=False
#     if request.method=="POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         department = request.POST.get('department')

#         us = User()
#         he = Head()
#         us.username=username
#         us.email=email
#         us.password=password
#         he.department=department
#         us.save()
#         he.user=us
#         head= he.save()
#         he.user=us

        # user_form.username=username
        # user_form.email=email
        # user_form.password=password
        # head_form = HeadForm()
        # head_form.department=department

        # user=user_form.save()
        # user.set_password(user.password)
        # user.save()

        # if user_form.is_valid():
        #     user=user_form.save()
        #     user.set_password(user.password)
        #     user.save()
        #     head=head_form.save()





    # return render(request, 'app1/register.html', )

