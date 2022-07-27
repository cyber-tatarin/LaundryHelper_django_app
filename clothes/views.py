from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateThingForm, CreateColorForm
from .models import Thing, Colors
from users.models import Profile
from django.views import View
from django.db.models import Q


class CreateThingView(LoginRequiredMixin, View):
    template_name = 'clothes/create_thing.html'

    def define_choices_list(self):
        choices_list = []
        colors = Colors.objects.all().filter(Q(id__in=[4, 5, 6, 7]) | Q(owner=self.request.user))
        for choice in colors:
            choices_list.append((choice.id, choice.color))
        return choices_list

    def get(self, request, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        try:
            profile = get_object_or_404(Profile, id=self.request.session['profile_id'])
        except:
            return redirect('profiles')

        form = CreateThingForm(self.define_choices_list())

        context = {
            'form': form,
            'profile': profile,
        }
        return render(request, self.template_name, context)

    def post(self, request):

        form = CreateThingForm(colorChoices=self.define_choices_list(), data=request.POST, files=request.FILES)

        profile = get_object_or_404(Profile, id=request.session['profile_id'])

        if form.is_valid():
            data = form.cleaned_data
            color_id = data['color']
            data['color'] = Colors.objects.get(id=color_id)
            thing = Thing(**data)
            thing.owner = request.user
            thing.profile = profile
            thing.save()
            return redirect('clothes:thing-list')

        form = CreateThingForm(self.define_choices_list())

        context = {
            'form': form,
            'profile': profile
        }
        return render(request, self.template_name, context)


class ThingListView(View):
    template_name = 'clothes/list_things.html'

    def get(self, request, **kwargs):

        try:
            profile = get_object_or_404(Profile, id=self.request.session['profile_id'])
        except:
            return redirect('profiles')

        search_req = self.request.GET.get('search', '')

        if search_req:
            queryset = Thing.objects.all().filter(owner=self.request.user, title__icontains=search_req,
                                                  profile=profile)
        else:
            queryset = Thing.objects.all().filter(owner=self.request.user, profile=profile)

        context = {
            'thing_list': queryset,
            'profile': profile
        }
        return render(request, self.template_name, context)

    def post(self, request):
        switch_thing = get_object_or_404(Thing, pk=request.POST.get('switch_id'))
        if switch_thing.condition == 0:
            switch_thing.condition = 1
        else:
            switch_thing.condition = 0
        switch_thing.save()

        return redirect('clothes:thing-list')


class ThingUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'clothes/edit_thing.html'

    def define_choices_list(self):
        choices_list = []
        colors = Colors.objects.all().filter(Q(id__in=[4, 5, 6, 7]) | Q(owner=self.request.user))
        for choice in colors:
            choices_list.append((choice.id, choice.color))
        return choices_list

    def get(self, request, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        try:
            profile = get_object_or_404(Profile, id=self.request.session['profile_id'])
        except:
            return redirect('profiles')

        obj = self.get_object()
        form = CreateThingForm(self.define_choices_list(), initial={'title': obj.title,
                                                                    'temperature': obj.temperature,
                                                                    'color': obj.color,
                                                                    'mass': obj.mass})

        context = {
            'form': form,
            'profile': profile,
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):

        form = CreateThingForm(colorChoices=self.define_choices_list(), data=request.POST, files=request.FILES)

        obj = self.get_object()
        profile = get_object_or_404(Profile, id=request.session['profile_id'])

        if form.is_valid():
            data = form.cleaned_data
            color_id = data['color']
            data['color'] = Colors.objects.get(id=color_id)
            obj.title = data['title']
            obj.temperature = data['temperature']
            obj.color = data['color']
            obj.save()
            return redirect('clothes:thing-list')

        form = CreateThingForm(self.define_choices_list())

        context = {
            'form': form,
            'profile': profile
        }
        return render(request, self.template_name, context)

    def get_object(self):
        return get_object_or_404(Thing, pk=self.kwargs.get('pk'))


class ThingDeleteView(DeleteView):

    def get_queryset(self):
        queryset = Thing.objects.all().filter(id=self.kwargs.get('pk'), owner=self.request.user)
        print(queryset)
        return queryset

    def get_success_url(self):
        return reverse('clothes:thing-list')


class ColorCreateView(LoginRequiredMixin, View):
    template_name = 'colors/create-color.html'

    def get(self, request, **kwargs):

        try:
            profile = get_object_or_404(Profile, id=self.request.session['profile_id'])
        except:
            return redirect('profiles')

        context = {
            'form': CreateColorForm(),
            'profile': profile
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):

        form = CreateColorForm(request.POST, request.FILES)

        if form.is_valid():
            color = form.save(commit=False)
            color.owner = request.user
            color.save()
            return redirect('clothes:create')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ColorDeleteView(DeleteView):

    def get_queryset(self):
        queryset = Colors.objects.all().filter(id=self.kwargs.get('pk'), owner=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse('clothes:colors-list')


class ColorsListView(ListView):
    template_name = 'colors/list-colors.html'

    def get_queryset(self):
        queryset = Colors.objects.all().filter(Q(id__in=[4, 5, 6, 7]) | Q(owner=self.request.user))
        return queryset
