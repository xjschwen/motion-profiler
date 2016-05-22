#!/usr/bin/python

from motionProfiler import MotionProfiler

class MotionProfilerTester():

  def test_getProfileAccellTimes(self):
    """tests the ProfileAccellTimes function"""
    retValue = 0

    dist=30.0
    initVel = 1.0
    cruiseVel = 18.0
    accel = 3.0
    retValue = 0
    mp=MotionProfiler(dist, initVel, cruiseVel, accel)

    if (fpIsEqual (mp.getProfileAccellTimes(),  (17/3), 100)):
      retValue =1
      print "getProfileAccellTimes1: Fail"

    initVel = 0.0
    cruiseVel = 25.0
    accel = 5.0
    mp=MotionProfiler(dist, initVel, cruiseVel, accel)
    #print mp.getProfileAccellTimes()
    if not fpIsEqual (mp.getProfileAccellTimes(), 5.0, 100):
      retValue =1
      print "getProfileAccellTimes2: Fail"


    if retValue == 0:
      print "getProfileAccellTimes: PASS"





  def test_getProfileDeltaX(self):
    """Test if the math is correct for getProfileDeltaX"""
    dist=30.0
    initVel = 1.0
    cruiseVel = 18.0
    accel = 3.0
    retValue = 0


    mp=MotionProfiler(dist, initVel, cruiseVel, accel)
    if not fpIsEqual (mp.getProfileDeltaX(), 53.833, 100) :
      retValue = 1
      print "getProfileDeltaX1: Fail"

    dist=30.0
    initVel = 1.0
    cruiseVel = 18.0
    accel = 300.0
    retValue = 0

    mp=MotionProfiler(dist, initVel, cruiseVel, accel)
    if not fpIsEqual (mp.getProfileDeltaX(), 0.538, 100) :
      retValue = 1
      print "getProfileDeltaX2: Fail"

    if retValue == 0:
      print "getProfileDeltaX: PASS"


  def test_getProfileCurrVelocity(self):
    """Tests if the math is correct for the getcurrentVelocity"""
    dist=30.0
    initVel = 1.0
    cruiseVel = 18.0
    accel = 3.0
    retValue = 0

    mp=MotionProfiler(dist, initVel, cruiseVel, accel)
    if mp.getProfileCurrVelocity(0.5) != 2.5:
      retValue=1
      print "getProfileCurrVelocity1: Fail"

    if mp.getProfileCurrVelocity(0.0) != 1.0:
      retValue=1
      print "getProfileCurrVelocity2: Fail"

    if mp.getProfileCurrVelocity(1.0) != 4.0:
      retValue=1
      print "getProfileCurrVelocity3: Fail"

    if mp.getProfileCurrVelocity(5.0) != 16.0:
      retValue=1
      print "getProfileCurrVelocity4: Fail"

    if mp.getProfileCurrVelocity(1.5) != 5.5:
      retValue=1
      print "getProfileCurrVelocity5: Fail"

    dist=30.0
    initVel = 15.0
    cruiseVel = 15.0
    accel = 3.0
    retValue = 0

    mp=MotionProfiler(dist, initVel, cruiseVel, accel)
    if mp.getProfileCurrVelocity(1.5) != 15.0:
      retValue=1
      print "getProfileCurrVelocity6: Fail"

    if mp.getProfileCurrVelocity(-5.0) != 0.0:
      retValue=1
      print "getProfileCurrVelocity7: Fail"

    if mp.getProfileCurrVelocity(10.0) != -0.0:
      retValue=1
      print "getProfileCurrVelocity8: Fail"



    if retValue == 0:
      print "getProfileCurrVelocity: PASS"


  def test_getProfileAccellerationSign(self):
    """tests the method getProfileAccellerationSign"""
    dist=30.0
    initVel = 1.0
    cruiseVel = 18.0
    accel = 3.0
    retValue = 0

    mp=MotionProfiler(dist, initVel, cruiseVel, accel)
    if mp.getProfileAccellerationSign() != 1:
      print "getProfileAccellerationSignPos: Fail"
      retValue = 1


    mp=None
    initVel=18.0
    cruiseVel = 18.0
    mp=MotionProfiler(dist, initVel, cruiseVel, accel)
    if mp.getProfileAccellerationSign() != 0:
      print "getProfileAccellerationSignZero: Fail"
      retValue = 1

    if retValue == 0:
      print "getProfileAccellerationSign: PASS"

def fpIsEqual(fp1, fp2, tol):

  ip1 = int(fp1 * tol )
  ip2 = int(fp2 * tol )
  #print "ip1 = %s, ip2 = %s, %s" % (ip1, ip2, ip1 == ip2)
  return (ip1 == ip2)

def test_fpIsEqual():
  """ Tests if fpIsEqual returns good results"""

  retValue = 0
  if not fpIsEqual(3.14, 3.15, 1):
    print "fpIsEqual1: Fail"
    retValue =1

  if not fpIsEqual(3.14, 3.15, 10):
    print "fpIsEqual1: Fail"
    retValue =1


  if fpIsEqual(3.14, 3.15, 100):
    print "fpIsEqual2: Fail"
    retValue =1

  if fpIsEqual(3.141, 3.142, 1000):
    print "fpIsEqual3: Fail"
    retValue =1

  if retValue == 0:
    print "fpIsEqual: PASS"

if __name__ == "__main__":
  test_fpIsEqual()
  mpt = MotionProfilerTester()
  mpt.test_getProfileAccellerationSign()
  mpt.test_getProfileCurrVelocity()
  mpt.test_getProfileDeltaX()
  mpt.test_getProfileAccellTimes()
