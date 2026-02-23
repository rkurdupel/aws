from django.shortcuts import render, redirect
from authentication.models import CustomUser
from .forms import PersonalInfoForm
from django.http import HttpResponse


def users(request):
    context = {}
    if request.method == "POST":
        form = PersonalInfoForm(request.POST)
        context['form'] = form
        return render(request, "users/edit_data.html", context)
    else:
        all_users = CustomUser.objects.all()
        #context = {'users': all_users}
        context['users'] =  all_users
        return render(request, 'users/users.html', context)

def edit_specific_user(request, user_id):
    context = {}
    user = CustomUser.get_by_id(user_id)

    if request.method == "POST":
        form = PersonalInfoForm(request.POST, instance = user)  # get post form with data from user
        if form.is_valid(): # if email is free
            form.save()    # save data in form
            return redirect('users')    # redirect to the page with all users
        else:   # if email is taken
            return HttpResponse('<h1>Email address is already in use</h1>') # return webpage response
    else:
        form = PersonalInfoForm(instance = user)
        context['form'] = form
        context['user_id'] = user_id
        return render(request, 'users/edit_specific_user.html', context)

def edit_data(request):
    if request.method == "POST":
        user_id = request.user.id
        user = CustomUser.objects.get(id = user_id) 

        form = PersonalInfoForm(request.POST, instance = user)  # return form with user data from instance argument
        if form.is_valid():
            form.save()
            return redirect('personal_info')
        
        else:
            return HttpResponse('<h1> Email address is already in use </h1>')   # return a html page with h1 tag
    else:
        return render(request, 'users/edit_data.html')

def personal_info(request):
    context = {}
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        context['form'] = form
        return render(request, 'users/edit_data.html', context)
    
    else:

        user_id = request.user.id
        personal_data = CustomUser.get_by_id(user_id)   # 'id': 18, 'first_name': '1', 'middle_name': '1', 'last_name': '1', 'email': 'test3@gmail.com', 'created_at': 1697139889, 'updated_at': 1697139889, 'role': 1, 'is_active': True
        
        context['personal_data'] = personal_data
    
    return render(request, 'users/personal_info.html', context)


def get_user(request, first_name):

    user = CustomUser.objects.get(first_name=first_name)
    user_role = ''
    if user.role == 0:
        user_role = 'visitor'
    elif user.role == 1:
        user_role = 'librarian'

    context = {'user': user, 'user_role': user_role}
    return render(request, 'users/user.html', context)
