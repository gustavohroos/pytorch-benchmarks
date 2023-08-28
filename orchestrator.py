import os
import subprocess
import threading
import time
import argparse
import pandas as pd

def watch_file(filename, consumption, stop_event):
    try:
        while not stop_event.is_set():
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    content = file.read()
                    consumption.append(int(content))
            time.sleep(0.5)
    except Exception as e:
        print("Error in watch_file:", e)
    finally:
        stop_event.set()

def main(args):
    consumption = []
    # According to: https://forums.developer.nvidia.com/t/power-consumption-monitoring/73608/5#:~:text=The%20file-,/sys/bus/i2c/devices/6%2D0040/iio_device/in_power0_input,-is%20current%20POM_5V_IN
    filename = "/sys/bus/i2c/devices/6-0040/iio:device0/in_power0_input" # Jetson Nano
    filename = 'test'
    process = subprocess.Popen(['python3', 'benchmarks.py', '--index', args.index, '--batch-size', args.batch_size], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stop_event = threading.Event()
    watch_thread = threading.Thread(target=watch_file, args=(filename, consumption, stop_event))
    watch_thread.start()

    while True:
        if process.poll() is not None:
            stop_event.set()
            watch_thread.join()
            break
        time.sleep(0.5)
    
    time.sleep(3)


    average = sum(consumption) / len(consumption)

    df = pd.read_csv('results.csv')
    df.iloc[-1, -1] = average
    df.to_csv('results.csv', index=False)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--index', type=str, required=True)
    argparser.add_argument('--batch-size', type=str, required=True)
    args = argparser.parse_args()

    main(args)
