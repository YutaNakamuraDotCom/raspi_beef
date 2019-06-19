import subprocess
import time
import RPi.GPIO as GPIO
import glob
from time import sleep

subprocess.run("modprobe w1-gpio", shell=True)
subprocess.run("modprobe w1-therm", shell=True)
GPIO.setmode(GPIO.BCM)

base_dir = '/sys/bus/w1/devices/'
each_dir = glob.glob(base_dir+'28*')[0]
dvc_file = each_dir+'/w1_slave'

_cmd = subprocess.run(["cat" , dvc_file],stdout = subprocess.PIPE)
print(_cmd.stdout.decode('utf-8'))

