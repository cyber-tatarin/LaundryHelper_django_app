from django.urls import path, include
from .views import RegisterView, CreateProfileView, ProfilesListView, SetProfileIdView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('profiles/', ProfilesListView.as_view(), name='profiles'),
    path('profiles/create/', CreateProfileView.as_view(), name='create-profile'),
    path('profile/id/<int:pk>/', SetProfileIdView.as_view(), name='set-profile-id')
]
