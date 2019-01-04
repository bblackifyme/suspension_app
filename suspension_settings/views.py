from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required

from .models import Setting
from .forms import SettingForm

@login_required
def index(request):
    settings = Setting.objects.all()
    context = {'settings': settings}
    return render(request, 'index.html', context)

class bikeSettings(ListView):
    model = Setting

    template_name = 'bike_setting_list.html'

    def get_queryset(self):
        return Setting.objects.filter(Bike=self.kwargs['bike_id'])

def addFromLast(request):
    last_setting = Setting.objects.latest('pk')
    if request.method == 'POST':
        form = SettingForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('index')) 
    else:
        form = SettingForm(initial=last_setting.__dict__)
        return render(request, 'add_from_form.html', {'form':form})
        

 
class SettingCreateView(CreateView):
    model = Setting
    fields = ('Bike', 'SpringRate', 'FrontCompression', 'FrontRebound', 'RearHighSpeedCompression',
              'RearLowSpeedCompression', 'RearRebound', 'Sag', 'Notes',
                )
    template_name = 'setting_form.html'

class SettingUpdate(UpdateView):
    model = Setting
    fields = ('Bike', 'SpringRate', 'FrontCompression', 'FrontRebound', 'RearHighSpeedCompression',
              'RearLowSpeedCompression', 'RearRebound', 'Sag', 'Notes',
                )
    template_name = 'setting_form.html'

class SettingDelete(DeleteView):
    model = Setting
    template_name = 'setting_confirm_delete.html'
    success_url=''