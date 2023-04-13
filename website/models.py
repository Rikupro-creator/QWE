from django.db import models

# Create your models here.
class route(models.Model):
	routeID=models.PositiveIntegerField()
	starting_location=models.CharField(max_length=50)
	destination=models.CharField(max_length=50)
	distance=models.FloatField()
	estimated_arrival_time=models.TimeField()
	actual_arrival_time=models.TimeField()
	security_team=models.PositiveIntegerField()
	van_number=models.PositiveIntegerField()
	status=models.CharField(max_length=20)
	def __str___(self):
		return f"route:{self.routeID} {self.starting_location} {self.destination}"