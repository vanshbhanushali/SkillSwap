
from django.shortcuts import render, redirect

def fake_login(request):
    if request.method == 'POST':
        # Ignore input, just redirect to /home/
        return redirect('home')
    return render(request, 'registration/login.html')  # Your styled login page

def home(request):
    return render(request, 'skills/huhuah.html')  # Your home page

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # after registering, go to login
    else:
        form = UserCreationForm()
    return render(request, 'skills/register.html', {'form': form})
from django.shortcuts import render

def home(request):
    return render(request, 'skills/huhuah.html')

def browse(request):
    return render(request, 'skills/browse.html')

def my_swaps(request):
    return render(request, 'skills/my_swaps.html')

def messages(request):
    return render(request, 'skills/messages.html')

def my_swaps(request):
    return render(request, 'skills/myswap.html')

def profile(request):
    return render(request, 'skills/profile.html')

def browse(request):
    return render(request, 'skills/browse.html')
