from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import ETMInfoForm

from .models import ETMInfo

# views.py

@login_required
def etm_info(request):
    if request.method == 'POST':
        form = ETMInfoForm(request.POST)
        if form.is_valid():
            etm_info_instance = form.save(commit=False)
            etm_info_instance.user = request.user
            etm_info_instance.save()
            return redirect('dashboard')
    else:
        form = ETMInfoForm()
    return render(request, 'etm_info.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # this assigns a value to the 'user' variable
            user.phone_number = form.cleaned_data.get('phone_number')
            user.save()
            send_mail(
                'New User Registration',
                f'A new user has signed up!\n with username: {user.username}\n Password: {user.password}',
                'amirmoghadamkhoshpour@gmail.com',
                ['amirezamoghadam@gmail.com'],
                fail_silently=False,
            )
            # Send email notification to admin          
            return redirect('login')
        
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})





@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user': user})

@login_required
def personal_info(request):
    user = request.user
    etm_info_exists = ETMInfo.objects.filter(user=user).exists()
    print(etm_info_exists)  # This should print 'True' if ETMInfo exists for the user.

    context = {
        'user': user,
        'etm_info_exists': etm_info_exists
    }
    return render(request, 'personal_info.html', context)

from django.shortcuts import render

# ... other views ...

def schedule_view(request):
    return render(request, 'schedule.html')
