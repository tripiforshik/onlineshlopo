from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import  UserForm,ProfileForm
from django.views import View
from .models import Profile

class ProfileView(View):
    def get(self,request,user_name):
        user=User.objects.get(username=user_name)
        user_form = UserForm(instance=user)
        profile = Profile.objects.get(user=user.pk)
        profile_form=ProfileForm(instance=profile)
        uploaded_image=profile.image
        return render(request, "accounts/profile.html", context={"userform": user_form, "profile_form": profile_form,"uploaded_image":uploaded_image})
    def post(self,request,user_name):

        user = User.objects.get(username=user_name)
        user_form = UserForm(request.POST,instance=user)
        profile = Profile.objects.get(user=user.pk)
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile)
        uploaded_image=profile.image
        print(88888888888)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("index")
        return render(request, "accounts/profile.html", context={"userform": user_form, "profile_form": profile_form, "uploaded_image": uploaded_image})

# def profile(request):
#     user_form = UserForm()
#     profile_form=ProfileForm()
#     return render(request,"accounts/profile.html",context={"userform":user_form, "profile_form":profile_form})
