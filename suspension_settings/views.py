from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required

from .models import Setting, Bike
from .forms import SettingForm

@login_required
def index(request):
    bikes = Bike.objects.all().filter(User=request.user)
    context = {'bikes': bikes}
    return render(request, 'index.html', context)

def addFromLast(request, bike_id):
    last_setting = Setting.objects.filter(Bike=bike_id).order_by('-id')[0]
    bike = last_setting.Bike
    if request.method == 'POST':
        form = SettingForm(request.POST)
        form.save()
        return HttpResponseRedirect('/settings/%s' % bike_id) 
    else:
        defaults = last_setting.__dict__
        defaults.update({'Bike':bike})
        form = SettingForm(initial=defaults)
        return render(request, 'add_from_form.html', {'form':form})
        
class SettingCreateView(CreateView):
    model = Setting
    fields = ('SpringRate', 'FrontCompression', 'FrontRebound', 'RearHighSpeedCompression',
              'RearLowSpeedCompression', 'RearRebound', 'Sag', 'Notes',
                )
    template_name = 'setting_form.html'

    def form_valid(self, form):
        form.instance.Bike = Bike.objects.get(pk=self.kwargs['bike_id'])
        return super().form_valid(form)

class SettingUpdate(UpdateView):
    model = Setting
    fields = ('SpringRate', 'FrontCompression', 'FrontRebound', 'RearHighSpeedCompression',
              'RearLowSpeedCompression', 'RearRebound', 'Sag', 'Notes',
                )
    template_name = 'setting_form.html'

class SettingDelete(DeleteView):
    model = Setting
    template_name = 'setting_confirm_delete.html'

    def get_success_url(self):
        return '/settings/%s' % self.object.Bike.id

# BEGIN BIKE VIEW

class bikeSettings(ListView):
    model = Setting

    template_name = 'bike_setting_list.html'

    def get_queryset(self):
        return Setting.objects.filter(Bike=self.kwargs['bike_id']).filter(Bike__User=self.request.user)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['bike'] = self.kwargs['bike_id']
        return context

class BikeCreateView(CreateView):
    model = Bike
    fields = ('Make', 'Model', 'Year', 'Fork', 'Shock', 'LastMaintence',)
    template_name = 'bike_create_form.html'

    def form_valid(self, form):
        form.instance.User = self.request.user
        return super().form_valid(form)