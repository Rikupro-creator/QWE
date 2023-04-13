from django import forms
from .models import route


class routeForm(forms.ModelForm):
	class Meta:
 		model= route
 		fields=['routeID', 'starting_location','destination','distance', 'estimated_arrival_time', 'actual_arrival_time','security_team', 'van_number', 'status']
 		labels={'routeID':'routeID', 'starting_location':'starting_location','destination':'destination','distance':'distance', 'estimated_arrival_time':'estimated_arrival_time',
 		 'actual_arrival_time':'actual_arrival_time', 'security_team':'security_team','van_number':'van_number', 'status':'status'}

 		widgets={

 		'routeID':forms.NumberInput(attrs={'class':'form-control'}), 
 		'starting_location':forms.TextInput(attrs={'class':'form-control'}),
 		'destination':forms.TextInput(attrs={'class':'form-control'}),
 		'distance':forms.NumberInput(attrs={'class':'form-control'}), 
 		'estimated_arrival_time':forms.DateInput(attrs={'type': 'date'}), 
 		'actual_arrival_time':forms.DateInput(attrs={'type': 'date'}),
 		'security_team':forms.NumberInput(attrs={'class':'form-control'}),
 		'van_number':forms.NumberInput(attrs={'class':'form-control'}),
 		'status':forms.TextInput(attrs={'class':'form-control'})
 		}