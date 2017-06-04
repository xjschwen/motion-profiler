#!/usr/bin/python
#http://plaza.obu.edu/corneliusk/ps/phys/kelm.pdf
import sys
import math
import logger
class PIDControl():

  def __init__ (self, KP=0.0, KI=0.0, KD=0.0, lo=-1, hi=1):

      self.KP=KP
      self.KI=KI
      self.KD=KD
      self.lo = lo
      self.hi = hi
      self.prevError = 0.0
      self.cumlativeError = 0.0


  def calc(self, setpoint, measurepoint):
      """
      Calculate the PID value for the given error.
      """

      error = setpoint - measurepoint
      pValue =self.KP * error

      self.cumlativeError = self.cumlativeError + error
      iValue = self.KI * self.cumlativeError

      dValue = self.KD * (error - self.prevError)
      self.prevError = error

      PIDValue = (pValue + iValue + dValue)

      if (PIDValue < self.lo):
          PIDValue = self.lo

      if (PIDValue > self.hi):
          PIDValue = self.hi

      return PIDValue
