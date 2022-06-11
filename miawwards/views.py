from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    return render(request, 'index.html')



def profile(request, username):
    return render(request, 'profile.html', username)

def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request == user_prof:
        return redirect('profile', username=username)
    context = {
        'user_prof':user_prof

    }
    return render(request, 'userprofile.html', context)
    