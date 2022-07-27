from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from users.models import Profile


class HomeView(TemplateView):
    template_name = 'lh/home.html'

    def get_context_data(self, **kwargs):
        try:
            profile = get_object_or_404(Profile, id=self.request.session['profile_id'])

            context = {
                'profile': profile
            }
            return context

        except:
            return None
