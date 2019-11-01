#!/usr/bin/python

import maxlab
import maxlab.system
import maxlab.chip
import maxlab.util
import maxlab.saving

import os
import sys
import time
import argparse
import numpy as np

GAIN = 512

def scan(config_path,output_path,length=None,isOnlySpike=False):
    if length is None:
        length = 60  # record time[s]

    # 0. Initialize system into a defined state
    maxlab.util.initialize()
    #maxlab.send(maxlab.chip.Core().enable_stimulation_power(False))
    maxlab.send(maxlab.chip.Amplifier().set_gain(GAIN))

    # 1. Load configuration
    array = maxlab.chip.Array('recording')
    array.reset()
    array.clear_selected_electrodes()
    array.load_config(config_path)

    # Download the prepared array configuration to the chip
    array.download()

    print("SEND: OFFSET CMD")
    print("WAITING")
    maxlab.util.offset()
    time.sleep(4)

    # 計測開始
    start_time = time.time()
    s = maxlab.saving.Saving()
    if isOnlySpike:
        s.start_spikes_only(output_path)
    else:
        s.start(output_path)

    print("NOW RECORDING")
    time.sleep(length)

    # 計測終了
    s.stop()
    end_time = time.time()
    elasped = end_time - start_time

    print('\007')  # beep
    print("elasped time[min]:" + str(elasped / 60))


def scan_sak(config_path,output_path,length=None,isOnlySpike=False):

    if length is None:
        length = 60  # record time[s]

    # 0. Initialize system into a defined state
    maxlab.util.initialize()
    #maxlab.send(maxlab.chip.Core().enable_stimulation_power(False))
    maxlab.send(maxlab.chip.Amplifier().set_gain(GAIN))

    # 1. Load configuration
    array = maxlab.chip.Array('recording')
    array.reset()
    array.clear_selected_electrodes()
    array.load_config(config_path)

    # Download the prepared array configuration to the chip
    array.download()

    # 計測開始
    start_time = time.time()
    s = maxlab.saving.Saving()
    if isOnlySpike:
        s.start_spikes_only(output_path)
    else:
        s.start(output_path)
    print("start time: " + time.ctime(start_time))
    print("plz wait:" + str(length) + "[s]")

    # 待機
    time.sleep(length)

    # 計測終了
    s.stop()
    end_time = time.time()
    elasped = end_time - start_time

    print('\007')  # beep
    print("elasped time[min]:" + str(elasped / 60))

