from django.shortcuts import render, redirect
from django.views import View
from clothes.models import Thing
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from users.models import Profile
from django.http import HttpResponseRedirect


class WashesGroupsView(LoginRequiredMixin, View):

    def get(self, request):

        try:
            profile = get_object_or_404(Profile, id=self.request.session['profile_id'])
        except:
            return redirect('profiles')

        # colors_dict = list(Thing.objects.all().filter(owner=request.user).values('color'))
        # colors = []
        # for d in colors_dict:
        #     colors.append(d['color'])

        colors = [d['color'] for d in list(Thing.objects.all().filter(owner=request.user).values('color'))]

        # temperatures_dict = list(Thing.objects.all().filter(owner=request.user).values('temperature'))
        # temperatures = []
        # for t in temperatures_dict:
        #     temperatures.append(t['temperature'])

        temperatures = [t['temperature'] for t in list(Thing.objects.all().filter(owner=request.user).values('temperature'))]

        res = []
        ctx_mass = []
        for color_iter in set(colors):
            for temperature_iter in set(temperatures):
                queryset = Thing.objects.all().filter(color=color_iter,
                                                      owner=request.user,
                                                      temperature=temperature_iter,
                                                      condition=0)
                if queryset:
                    res.append(queryset)

                    res_mass = 0
                    for mass in queryset.values('mass'):
                        if mass['mass'] is not None:
                            res_mass += mass['mass']
                        else:
                            res_mass += 0
                    if res_mass > 0:
                        ctx_mass.append(res_mass)
                    else:
                        ctx_mass.append(0)

        ctx = zip(res, ctx_mass)

        context = {
            'object_list': ctx,
            'profile': profile,
        }
        return render(request, 'washes/washes_groups.html', context)

    def post(self, request):

        washed_color = request.POST.get('col')
        washed_temp = request.POST.get('tem')
        queryset = Thing.objects.all().filter(color=washed_color,
                                              owner=request.user,
                                              temperature=washed_temp,
                                              condition=0)

        for thing in queryset:
            thing.condition = 1
            thing.save()

        return redirect('washes:washes-groups')


class RemoveFromWash(LoginRequiredMixin, View):

    def get(self, request, **kwargs):

        thing = get_object_or_404(Thing, pk=kwargs['pk'], owner=self.request.user)
        thing.condition = 1
        thing.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
