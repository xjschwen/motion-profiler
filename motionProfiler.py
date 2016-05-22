#!/usr/bin/python
#http://plaza.obu.edu/corneliusk/ps/phys/kelm.pdf
import sys
import math
import logger
class MotionProfiler():

  def __init__ (self, distance=0.0, initVelocity=0.0, cruiseVelocity=0.0, accelleration=0.0):

    #Total distance to move
    self.distance=distance
    #Max speed that we wish to move at
    self.cruiseVelocity = cruiseVelocity
    #Our starting velocity...Normally is zero
    self.initVelocity = initVelocity

    #Our assumed constant accelleration.
    self.accelleration = accelleration

    self.accelTime=self.getProfileAccellTimes()
    self.cruiseDistance= self.distance - (2 * self.getProfileDeltaX())
    self.cruiseTime = self.cruiseDistance / self.cruiseVelocity
    self.deccelTime = self.accelTime + self.cruiseTime
    self.stopTime  = self.deccelTime + self.accelTime
    self.logger=logger.Logger("motionProfiler.txt")

    self.xa = 0
    self.xc = 0
    self.xd = 0


  def __del__(self):
    self.logger.write()

  def getProfileAccellTimes (self):
    """Given a velocity determine the accel times"""
    retvalue = 0.0
    try:
      retvalue = (self.cruiseVelocity - self.initVelocity) /self.accelleration
    except ZeroDivisionError:
      pass

    return retvalue

  def getProfileDeltaX (self):
    """returns the deltaX to change the velocity """
    # (vfinal*vfinal) = (vinit*vinit) + 2ax

    return ((self.cruiseVelocity * self.cruiseVelocity)-(self.initVelocity * self.initVelocity)) / 2 / self.accelleration

  def getProfileCurrVelocity(self, time):
    """given a time calculate the current Velocity"""
    #Vf = Vi + at
    currVel= 0
    #we have not started moving yet...
    if time < 0:
        currVel = 0
    #we are accellerating
    elif (time < self.accelTime):
        msg = "accellerating"
        currVel =self.initVelocity + (self.accelleration * time)
        self.xa = .5 * (self.accelleration) * time * time
    #we are cruising at speed
    elif (time > self.accelTime) and (time < self.deccelTime):
        msg = "cruising"
        currVel = self.cruiseVelocity
        self.xc = (self.cruiseVelocity) * (time -self.accelTime)
    #we are slowing down
    elif(time > self.deccelTime) and (time < self.stopTime):
        msg = "slowing"
        currVel = self.cruiseVelocity - (self.accelleration * (time-self.deccelTime))
        self.xd = (self.cruiseVelocity * (time-self.deccelTime)) - \
         (.5 * (self.accelleration) * (time-self.deccelTime) * (time-self.deccelTime))
    #we are past when we should stop
    else:
        msg="stopped"
        currVel = 0

    xtotal = self.xa + self.xc + self.xd

    self.logger.makeEntry([msg, "%3.3f" % time, "%3.3f" % currVel, "%3.3f" % xtotal])

    return currVel

  def getTotalDistanceTraveled(self):
      return self.xa + self.xc + self.xd


  def getProfileAccellerationSign(self):
    """Returnt the sign of the acceleration for this motion"""
    retValue = 0

    if (self.cruiseVelocity > self.initVelocity):
      retValue = 1

    if(self.initVelocity > self.cruiseVelocity):
      retValue = -1

    return retValue
