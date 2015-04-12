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

def checkTetanusStatus():
	eventList = getEventList()
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
				self.minDate == date.today()
				self.maxDate == date.today()
			if len(eventList) in [1,2]:
				self.type == 'BaseImmu'
				self.minDate == eventList[-1:].date + timedelta(month=1)
				self.maxDate == eventList[-1:].date + timedelta(month=2)





















