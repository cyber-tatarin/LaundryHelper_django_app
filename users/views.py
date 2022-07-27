from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .forms import UserCreateForm, ProfileCreateForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden

User = get_user_model()


class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):

        context = {
            'form': UserCreateForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):

        form = UserCreateForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profiles')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ProfilesListView(LoginRequiredMixin, View):

    def get(self, request):

        profiles = request.user.profiles.all()
        print(profiles)
        return render(request, 'profiles/profiles-list.html', context={'profiles': profiles})


class CreateProfileView(LoginRequiredMixin, View):
    template_name = 'profiles/profiles-create.html'

    def get(self, request):

        form = ProfileCreateForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):

        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            profile = form.save()
            obj = get_object_or_404(User, id=request.user.id)
            obj.profiles.add(profile)
            return redirect('profiles')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class SetProfileIdView(LoginRequiredMixin, View):

    def get(self, request, **kwargs):

        profile = get_object_or_404(Profile, id=kwargs['pk'])

        if profile in request.user.profiles.all():
            request.session['profile_id'] = profile.id
            print(request.session['profile_id'])
            return redirect('clothes:thing-list')

        return HttpResponseForbidden
