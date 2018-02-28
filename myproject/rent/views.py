from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import PersonForm,RentCarForm
from .models import Person,Car,Rent


# Create your views here.
def home(request):
    return (HttpResponse('Hello world'))

def success(request):
    return (HttpResponse('Sucess!!'))

class CreatePersonView(CreateView):
	queryset = Person()
	template_name='create.html'
	form_class = PersonForm
	success_url = '/rentcar'

class ListCarView(ListView):
    model = Car
    template_name='listcar.html'


class RentCar(CreateView):
    template_name='rentcar.html'
    form_class = RentCarForm
    success_url = '/success'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(RentCar,self).form_valid(form)

class SuccessRent(ListView):
    queryset = Rent()
    template_name='success.html'
