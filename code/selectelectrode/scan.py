#!/usr/bin/python

import maxlab
import maxlab.system
import maxlab.chip
import maxlab.util
import maxlab.saving
import time
import datetime

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

    # offset 必要かどうか　FIXME
    print("offset")
    maxlab.util.offset()
    time.sleep(4)

    # 計測開始
    start_time = datetime.datetime.now()
    print("start recording [{}]".format(start_time.ctime()))
    print("plz wait: {0[0]}m {0[1]}s".format(divmod(length,60)))
    s = maxlab.saving.Saving()
    if isOnlySpike:
        s.start_spikes_only(output_path)
    else:
        s.start(output_path)

    time.sleep(length)

    # 計測終了
    s.stop()
    end_time = datetime.datetime.now()
    elasped = end_time - start_time
    print('\007')  # beep
    print("end recording [{}]".format(end_time.ctime()))
    print("elasped time[min]: {0[0]}m {0[1]}s".format(divmod(elasped.seconds,60)))


