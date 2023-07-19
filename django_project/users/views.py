from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib import messages #mesages.debug/info/success/warning/error
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)#IF post request there then it instantiate form with post data
        if form.is_valid():
            form.save()#save form info
            username = form.cleaned_data.get('username')#if form is valid data in cleaned_data dictionary
            messages.success(request, f'Account created for {username}!. You can now Login.')#display this mesage
            return redirect('login')#redirect to login page
    else:
        form = UserRegisterForm()#create user reg form/instantiate empty form
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)#populated with data to be submitted
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated!')#display this mesage
            return redirect('profile')#redirect to login page
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html',context)