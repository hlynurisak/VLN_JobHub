from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            return redirect('login')

    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })