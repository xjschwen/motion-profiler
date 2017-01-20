#!/usr/bin/python

from motionProfiler import MotionProfiler
import datetime
import os
import time
import logger
#from os import times

MAX_SPEED= 75.0
class cmdDriveWithProfile():
    """A robot drive command to simulate java drive commands"""

    def __init__(self, distance=0.0, cruiseSpeed = 0.0):
        """
        given distance (inches) and cruiseSpeed (inches/sec)
        drive with nice profile
        """

        self.kpThottleJuice = .0003
        self.distance = distance
        self.finished = False
        self.acceleration = 75.0 # inches/sec/sec
        self.mp = MotionProfiler(distance, 0.0, cruiseSpeed, self.acceleration)
        self.logger=logger.Logger("cmdMotion.txt")
        self.startTime=time.time() * 1000
        print "%s\t%s\t%s\t%s" % (self.mp.accelTime, self.mp.cruiseTime, self.mp.deccelTime, self.mp.stopTime)


    def __del__ (self):
        self.logger.write()
        self.logger = None


    def average_encoders(self) :
        """
        Read the encoder values and average them together in to inches traveled
        """
        return 0

    def execute(self):
        """execute the drive """
        #deltaTime = os.times()[4] - self.startTime
        deltaTime = ((time.time()*1000) - self.startTime)/1000
        #print deltaTime

        profileVelocity = self.mp.getProfileCurrVelocity(deltaTime)
        # are are in the accel time segment of the motion
        msg="throttle-pos=%3.3f" % (profileVelocity / MAX_SPEED)
        self.logger.makeEntry([msg, "%3.3f" % deltaTime, "%3.3f" % profileVelocity,
                                    "%3.3f" % self.mp.getTotalDistanceTraveled()])

        # Read encoders and if we are too slow or fast for the profile adjust it

        #deltaDT = difference in distance traveled between the robot and the motion profiler
        deltaDT = self.mp.getTotalDistanceTraveled() - self.average_encoders ()

        throttleJuice = self.kpThottleJuice * deltaDT
        thottlePoition = (profileVelocity / MAX_SPEED) + throttleJuice


        #time saftey... stop if running too long
        if (deltaTime > self.mp.stopTime):
            self.finished = True
            self.end

        #distance saftey... stop if running too far
        if (self.mp.getTotalDistanceTraveled() > self.distance):
            self.finished = True
            self.end


    def isFinished(self):
        """are we done yet"""
        return self.finished

    def end(self):
        """stop things that need to be stopped"""
        self.finished = True
        print "%s.end" % __name__
        print "%s\t%s\t%s" % (self.mp.accelTime, self.mp.cruiseTime, self.mp.deccelTime)
        self.logger.write()
