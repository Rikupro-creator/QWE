from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import routeForm

from .models import route as Routes

# Create your views here.
def index(request):
	return render(request, 'website/index.html', {'route':Routes.objects.all()
		})

def view_routes(request, id):
	route=Routes.objects.get(pk=id)
	return render(reverse('index'))
def add(request):
    if request.method =='POST':
        form = routeForm(request.POST)
        if form.is_valid():
            new_route_id = form.cleaned_data['routeID']
            new_starting_location = form.cleaned_data['starting_location']
            new_destination = form.cleaned_data['destination']
            new_distance = form.cleaned_data['distance']
            new_estimated_arrival_time = form.cleaned_data['estimated_arrival_time']
            new_actual_arrival_time = form.cleaned_data['actual_arrival_time']
            new_security_team = form.cleaned_data['security_team']
            new_van_number = form.cleaned_data['van_number']
            new_status=form.cleaned_data['status']

            new_route = Routes.objects.create(
                routeID=new_route_id,
                starting_location=new_starting_location,
                destination=new_destination,
                distance=new_distance,
                estimated_arrival_time=new_estimated_arrival_time,
                actual_arrival_time=new_actual_arrival_time,
                security_team=new_security_team,
                van_number=new_van_number,
                status=new_status
            )
            new_route.save()
            return render(request, 'website/add.html', {'form': routeForm(), 'success': True})
    else:
        form = routeForm()
    return render(request, 'website/add.html', {'form': routeForm()})

def edit(request,id):
	if request.method=='POST':
		route=Routes.objects.get(pk=id)
		form=routeForm(request.POST, instance=route)
		if form.is_valid():
			form.save()
			return render(request, 'website/edit.html',{
				'form':form,
				'success':True
				})
	else:
		route=Routes.objects.get(pk=id)
		form=routeForm(instance=route)
	return render(request, 'website/edit.html',{
				'form':form
				})
def delete(request, id):
	if request.method =='POST':
		route=Routes.objects.get(pk=id)
		route.delete()
	return HttpResponseRedirect(reverse('index'))


