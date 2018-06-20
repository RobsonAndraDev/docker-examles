import sys
import time
import requests
while True:
  r = requests.get('http://172.17.0.1/node')
  sys.stderr.write(r.text)
  sys.stderr.write(' From Python\n')
  r = requests.get('http://172.17.0.1/php')
  sys.stderr.write(r.text)
  sys.stderr.write(' From Python\n')
  time.sleep(15)