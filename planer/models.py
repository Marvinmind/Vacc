from django.db import models

class Person(models.Model):
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	dateOfBirth = models.DateField()

class BaseImmu(models.Model):
	sign = models.CharField(max_length=50)
	offset = models.DurationField()
	predecessor = models.ForeignKey('self', null=True, blank=True)

class Disease(models.Model):
	name = models.CharField(max_length=50)
	baseImmus = models.ManyToManyField(BaseImmu)

class Vaccine(models.Model):
	name = models.CharField(max_length=50)
	coveredDiseases = models.ManyToManyField(Disease)


class Visit(models.Model):
	date = models.DateField()
	appliedVaccines = models.ManyToManyField(Vaccine)

