__author__ = 'martin'
from enum import Enum
from datetime import timedelta, date

class Schedule(Enum):
	regular = 0
	smaller12m = 1
	TwelveMToFiveY = 2
	FiveYTo11Y = 3
	ElevenYToEighteenY = 4
	greaterEighteenY = 5

class VaccType(Enum):
	BaseVacc = 0;
	RefreshVacc = 1

def checkTetanusStatus(eventList, dateOfBirth):
	count = 1
	#set schedule
	if not eventList:
		#set schedule directly according to age
	else:
		for event in eventList:
			ageAtEvent = getAgeAtEvent(dateOfBirth, event)
			if count == 1:
				if ageAtEvent < 3:
					schedule = Schedule.regular
				elif ageAtEvent >=3 and ageAtEvent < 12:
					schedule = Schedule.smaller12m
				elif ageAtEvent >= 12 and ageAtEvent < 60:
					schedule = Schedule.TwelveMToFiveY
				elif ageAtEvent >= 60 and ageAtEvent < 11*12:
					schedule = Schedule.FiveYTo11Y
				elif ageAtEvent >= 11*12 and ageAtEvent < 18*12:
					schedule = Schedule.ElevenYToEighteenY
				elif ageAtEvent >= 18*12:
					schedule = Schedule.greaterEighteenY

			if count >= 2 and schedule == Schedule.regular:
				if ageAtEvent > 3 and count == 2:
					schedule = Schedule.smaller12m
				if ageAtEvent > 4 and count == 3:
					schedule = Schedule.smaller12m
				if ageAtEvent > 14 and count == 4:
					schedule = Schedule.smaller12m

	countPreviousVaccs = len(eventList)
	if schedule==Schedule.regular:

		if countPreviousVaccs == 0:
			return Suggestion(dateOfBirth, Schedule.regular, 'G1')
		elif countPreviousVaccs == 1:
			return Suggestion(dateOfBirth, Schedule.regular, 'G2')
		elif countPreviousVaccs == 2:
			return Suggestion(dateOfBirth, Schedule.regular, 'G3')
		elif countPreviousVaccs == 3:
			return Suggestion(dateOfBirth, Schedule.regular, 'G4')


class Suggestion():
	def __init__(self, dateOfBirth, schedule, eventList):
		lastEventDate = eventList[-1:].date
		if schedule == Schedule.regular:
			if len(eventList) == 0:
				self.type = 'BaseImmu'
				self.minDate = dateOfBirth + timedelta(month=2)
				self.maxDate = dateOfBirth + timedelta(month=3)
			if len(eventList) == 1:
				self.type = 'BaseImmu'
				self.minDate = dateOfBirth + timedelta(month=3)
				self.maxDate = dateOfBirth + timedelta(month=4)
			if len(eventList) == 2:
				self.type = 'BaseImmu'
				self.minDate = dateOfBirth + timedelta(month=4)
				self.maxDate = dateOfBirth + timedelta(month=5)
			if len(eventList) == 3:
				self.type = 'BaseImmu'
				self.minDate = dateOfBirth + timedelta(month=11)
				self.maxDate = dateOfBirth + timedelta(month=14)

			if len(eventList) == 4:
				self.type == 'Refresh'
				self.minDate = dateOfBirth + timedelta(years=5)
				self.minDate = dateOfBirth + timedelta(years=6)

			if len(eventList) > 5:
				self.type == 'Refresh'
				self.minDate = eventList[-1].date + timedelta(years=10)


		elif schedule == Schedule.smaller12m:
			if len(eventList) == 0:
				self.type == 'BaseImmu'
				self.minDate = date.today()
				self.maxDate = date.today()
			elif len(eventList) in [1, 2]:
				self.type == 'BaseImmu'
				self.minDate = lastEventDate + timedelta(month=1)
				self.maxDate = lastEventDate + timedelta(month=2)
			elif len(eventList) == 4:
				self.type = VaccType.RefreshVacc
				self.minDate = lastEventDate + timedelta(year=5)
				self.maxDate = lastEventDate + timedelta(year=8)
			elif len(eventList) > 5:
				self.type = VaccType.RefreshVacc
				self.minDate = lastEventDate + timedelta(year=10)
				self.maxDate = lastEventDate + timedelata(year=11)

		elif schedule == Schedule.TwelveMToFiveY:
			if len(eventList) == 0:
				self.type = VaccType.BaseVacc
				self.minDate = date.today()
				self.maxDate = date.today()
			elif len(eventList) == 1:
				self.type = VaccType.BaseVacc
				self.minDate = lastEventDate + timedelta(month=1)
				self.maxDate = lastEventDate + timedelta(month=2)
			elif len(eventList) == 1:
				self.type = VaccType.BaseVacc
				self.minDate = lastEventDate + timedelta(month=1)
				self.maxDate = lastEventDate + timedelta(month=2)
			elif len(eventList) == 2:
				self.type = VaccType.BaseVacc
				self.minDate = lastEventDate + timedelta(month=6)
				self.minDate = lastEventDate + timedelta(month=7)
			elif len(eventList) in [3, 4]:
				self.type = VaccType.RefreshVacc
				self.minDate = lastEventDate + timedelta(years=5)
				self.minDate = lastEventDate + timedelta(years=10)
			elif len(eventList) >= 5:
				self.type = VaccType.RefreshVacc
				self.minDate = lastEventDate + timedelta(years=10)
				self.minDate = lastEventDate + timedelta(years=11)
		elif schedule == Schedule.FiveYTo11Y:
			if len(eventList) == 0:
				self.type = VaccType.BaseVacc
				self.minDate = date.today()
				self.maxDate = date.today()
			elif len(eventList) == 1:
				self.type = VaccType.BaseVacc
				self.minDate = lastEventDate + timedelta(month=1)
				self.maxDate = lastEventDate + timedelta(month=2)
			elif len(eventList) == 1:
				self.type = VaccType.BaseVacc
				self.minDate = lastEventDate + timedelta(month=1)
				self.maxDate = lastEventDate + timedelta(month=2)
			elif len(eventList) == 2:
				self.type = VaccType.BaseVacc
				self.minDate = lastEventDate + timedelta(month=6)
				self.minDate = lastEventDate + timedelta(month=7)
			elif len(eventList) == 3:
				self.type = VaccType.RefreshVacc
				self.minDate = lastEventDate + timedelta(years=5)
				self.maxDate = lastEventDate + timedelta(years=6)
			elif len(eventList) >= 4:
				self.type = VaccType.RefreshVacc
				self.minDate = lastEventDate + timedelta(years=10)
				self.minDate = lastEventDate + timedelta(years=11)
		elif schedule == Schedule.ElevenYToEighteenY:
			if len(eventList) == 0:
				self.type = VaccType.BaseVacc
				self.minDate = date.today()
				self.maxDate = date.today()
			elif len(eventList) == 1:
				self.type = VaccType.BaseVacc
				self.minDate = lastEventDate + timedelta(month=1)
				self.maxDate = lastEventDate + timedelta(month=2)
			elif len(eventList) == 1:
				self.type = VaccType.BaseVacc
				self.minDate = lastEventDate + timedelta(month=1)
				self.maxDate = lastEventDate + timedelta(month=2)
			elif len(eventList) == 2:
				self.type = VaccType.BaseVacc
				self.minDate = lastEventDate + timedelta(month=6)
				self.minDate = lastEventDate + timedelta(month=7)
			elif len(eventList) == 3:
				self.type = VaccType.RefreshVacc
				self.minDate = lastEventDate + timedelta(years=5)
				self.maxDate = lastEventDate + timedelta(years=10)
			elif len(eventList) >= 4:
				self.type = VaccType.RefreshVacc
				self.minDate = lastEventDate + timedelta(years=10)
				self.maxDate = lastEventDate + timedelta(years=11)
		elif schedule == Schedule.greaterEighteenY:
			if len(eventList) == 0:
				self.type = VaccType.BaseVacc
				self.minDate = date.today()
				self.maxDate = date.today()
			elif len(eventList) == 1:
				self.type = VaccType.BaseVacc
				self.minDate = lastEventDate + timedelta(month=1)
				self.maxDate = lastEventDate + timedelta(month=2)
			elif len(eventList) == 1:
				self.type = VaccType.BaseVacc
				self.minDate = lastEventDate + timedelta(month=1)
				self.maxDate = lastEventDate + timedelta(month=2)
			elif len(eventList) == 2:
				self.type = VaccType.BaseVacc
				self.minDate = lastEventDate + timedelta(month=6)
				self.minDate = lastEventDate + timedelta(month=7)
			elif len(eventList) >=3:
				self.type = VaccType.RefreshVacc
				self.minDate = lastEventDate + timedelta(years=10)
				self.maxDate = lastEventDate + timedelta(years=11)

	def __str__(self):
		return 'Your next Vaccination should be between %s and %s' % (self.minDate, self.maxDate)


def getAgeAtEvent(dateOfBirth, event):
	eventDate = event.date
	distance = event.date - dateOfBirth


















