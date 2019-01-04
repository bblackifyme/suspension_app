from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/<int:bike_id>', views.bikeSettings.as_view(), name='bike-settings'),
    path('/add', views.SettingCreateView.as_view(), name='setting-add'),
    path('/add_from_last', views.addFromLast, name='add-from-last'),
    path('/update/<pk>', views.SettingUpdate.as_view(), name='setting-update'),
    path('/delete/<pk>', views.SettingDelete.as_view(), name='setting-delete'),
]