#!/usr/bin/env python
from argparse import ArgumentParser
import time
import six
from sksurgerynditracker.nditracker import NDITracker

def process():
    settings_vega = {
        "tracker type": "vega",
        "ip address" : "169.254.59.33",
        "port" : 8765,
        "romfiles" : [
            "../data/8700340.rom",
            "../data/EngWoodenBox4Markers.rom"]
        }
    tracker = NDITracker(settings_vega)
    
    experiments = [1,2,3]
    marker_number = 0

    while marker_number not in experiments:
        marker_number = int(input("Enter the point tracked:"))
        if marker_number not in experiments:
            print("This point is not defined! Please try again!\n")

    saved = [marker_number]
    tracker.start_tracking()

    six.print_(tracker.get_tool_descriptions())

    for i in range(3):
        input(f"Please press the Enter key when you have marked point {marker_number}!")
        saved.append(tracker.get_frame())
        print(f"You have just recorded value #{i+1}")

    tracker.stop_tracking()
    tracker.close()

    return saved

if __name__ == "__main__":
  tracked_marker = process()
  print(tracked_marker)
