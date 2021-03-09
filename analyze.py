import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetAngles_Back_Leg = numpy.load("data/targetAngles_Back_Leg.npy")
targetAngles_Front_Leg = numpy.load("data/targetAngles_Front_Leg.npy")
#print(backLegSensorValues)


plt.plot(targetAngles_Back_Leg, color='red', linewidth=1)
plt.plot(targetAngles_Front_Leg, color='green', linewidth=1)
# plt.plot(backLegSensorValues,color='red',linewidth=2)
# plt.plot(frontLegSensorValues, color='blue',linewidth=2)
plt.legend(('Back Leg','Front Leg'))
plt.show()
