#!/usr/bin/python

import time


import cmdDriveWithProfile

if __name__ == "__main__":

    #cmdDrive= cmdDriveWithProfile.cmdDriveWithProfile(40,10 )

    #sleepTime = 0.040
    #while (cmdDrive.isFinished() == False):
    #    cmdDrive.execute()
    #    time.sleep (sleepTime)
    #cmdDrive = None

    cmdDrive= cmdDriveWithProfile.cmdDriveWithProfile(120,120)

    sleepTime = 0.040
    while (cmdDrive.isFinished() == False):
        cmdDrive.execute()
        time.sleep (sleepTime)
    cmdDrive = None
