#!/usr/bin/python3

# Copyright (C) 2017 Infineon Technologies & pmdtechnologies ag
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY
# KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
# PARTICULAR PURPOSE.

"""This sample opens a camera and displays information about the connected camera."""

import argparse
import roypy
from roypy_platform_utils import PlatformHelper

def main ():
    platformhelper = PlatformHelper()
    # Support a '--help' command-line option
    parser = argparse.ArgumentParser(usage = __doc__)
    parser.parse_args()

    # The rest of this function opens the first camera found
    c = roypy.CameraManager()
    l = c.getConnectedCameraList()

    print("Number of cameras connected: ", l.size())
    if l.size() == 0:
        raise RuntimeError ("No cameras connected")

    id = l[0]
    cam = c.createCamera(id)
    cam.initialize()
    print_camera_info (cam, id)


def print_camera_info (cam, id=None):
    """Display some details of the camera.

    This method can also be used from other Python scripts, and it works with .rrf recordings in
    addition to working with hardware.
    """
    print("====================================")
    print("        Camera information")
    print("====================================")

    # cam. , getCameraName , getId
    # getFrameRate , getMaxFrameRate
    # setExposureTimes , setCalibrationData ,

    if id:
        print("Id:              " + id)
    print("Name:            " + cam.getCameraName())
    print("ID:              " + cam.getId())
    #print("Info:            " + cam.getCameraInfo())
    print("Width:           " + str(cam.getMaxSensorWidth()))
    print("Height:          " + str(cam.getMaxSensorHeight()))
    print("Operation modes: " + str(cam.getUseCases().size()))

    listIndent = "    "
    noteIndent = "      "

    useCases = cam.getUseCases()
    for u in range(useCases.size()):
        print(listIndent + useCases[u])
        numStreams = cam.getNumberOfStreams(useCases[u])
        if (numStreams > 1):
            print(noteIndent + "( " + str(numStreams) + " streams ) ")
    use = ['MODE_9_5FPS_2000','MODE_9_10FPS_1000', 'MODE_5_45FPS_500']
    print('setting use case ', use[0], ' : ', cam.setUseCase(use[0]) )
    print('\n###### currently #####')
    print(' use case :     ', cam.getCurrentUseCase() )
    print(' frame rate :   ', cam.getFrameRate() )
    # print(' lens ctr :     ', cam.getLensCenter() )
    # print(' exposure : ', cam.getExposureMode('',0) )


    camInfo = cam.getCameraInfo()

    print("\nCameraInfo items: " + str(camInfo.size()))
    for u in range(camInfo.size()):
        print(listIndent + str(camInfo[u]))

if (__name__ == "__main__"):
    main()
