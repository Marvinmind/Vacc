__author__ = 'martin'
from enum import Enum

class TetanusStateEnum(Enum):
	Zero = 0
	G1 = 1
	G2 = 2
	G3 = 3
	G4 = 4

checkTetanusStatus():
	base = False
	eventList = getEventList()
	baseOffsetsDict = getBaseImmuOffsets()
	status = 0
	count = 0
	previousEventDate = getDateOfBirth()
	for event in eventList:
		#complete Base
		if not base:
			if age < 12:
				currentOffset = baseImmuOffsets['std'][count]
				try:
					if event.date - previousEventDate < currentOffset:
						raise Exception('stuff')
					else:
						status+=1
				except Exception as err:
					print(err)
			#Secondary schedule < 12 (p. 330)
			if (age < 12 and age > 2 and not eventList) or eventList[0].date - today
		#refresh
		else



