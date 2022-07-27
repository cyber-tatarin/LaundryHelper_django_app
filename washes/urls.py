from django.urls import path
from.views import WashesGroupsView, RemoveFromWash


app_name = 'washes'
urlpatterns = [

    path('', WashesGroupsView.as_view(), name='washes-groups'),
    path('remove/<int:pk>/', RemoveFromWash.as_view(), name='remove-from-wash')

]
