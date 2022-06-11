from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User

from miawwards.forms import UpdateUserForm, UpdateUserProfileForm



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


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
        else:
            user_form = UpdateUserForm(instance=request.user)
            prof_form = UpdateUserProfileForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'prof_form': prof_form
        }
        return render(request, 'edit.html', context)