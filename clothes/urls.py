from django.urls import path
from .views import CreateThingView, ThingListView, ThingUpdateView, \
    ThingDeleteView, ColorCreateView, ColorDeleteView, ColorsListView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'clothes'
urlpatterns = [

    path('create/', CreateThingView.as_view(), name='create'),
    path('all/', ThingListView.as_view(), name='thing-list'),
    path('edit/<int:pk>/', ThingUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ThingDeleteView.as_view(), name='delete'),
    path('colors/create', ColorCreateView.as_view(), name='create-color'),
    path('colors/delete/<int:pk>/', ColorDeleteView.as_view(), name='delete-color'),
    path('colors/all/', ColorsListView.as_view(), name='colors-list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
