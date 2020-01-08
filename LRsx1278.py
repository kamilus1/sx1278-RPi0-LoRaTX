from SX127x.LoRa import LoRa2, BW, MODE
from SX127x.board_config import BOARD2
import RPi.GPIO as GPIO
import numpy as np
from time import time, sleep
class sx1278(LoRa2):
  def __init__(self, freq=434.0, bandwidth_khz=125.0, pa_boost = 1, max_power = 2 , output_power=8, sf=8, verbose=False):
    GPIO.setwarnings(False)
    BOARD2.setup()
    BOARD2.reset()
    self.bw  = {7.8: 0, 10.4: 1, 15.6: 2, 20.8: 3, 31.25: 4, 41.7:5, 62.5: 6, 125.0:7, 250.0:8, 500: 9}
    super(sx1278, self).__init__(verbose)
    self.set_mode(MODE.SLEEP)
    self.set_dio_mapping([1, 0 ,0 ,0 ,0 ,0])
    self.set_freq(freq)
    self.set_pa_config(pa_boost, max_power, output_power)
    self.set_bw(self.bw[bandwidth_khz])
    self.set_modem_config_2(sf)
    self.set_rx_crc(True)
  def send_message(self, msg, timeout=1):
    word_array = [ord(i) for i in msg]
    self.write_payload(word_array)
    self.set_mode(MODE.TX)
    sleep(1) 
  def close(self):
    self.set_mode(MODE.SLEEP)
    BOARD2.teardown()
