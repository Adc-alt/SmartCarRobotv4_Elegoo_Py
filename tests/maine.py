#%% Load modules
import numpy as np
import cv2 as cv
from urllib.request import urlopen
import socket
import sys
import json
import re

#%% Capture image from camera
cmd_no = 0
def capture():
    global cmd_no
    cmd_no += 1
    print(str(cmd_no) + ': capture image')
    cam = urlopen('http://192.168.4.1/capture')
    img = cam.read()
    img = np.asarray(bytearray(img), dtype='uint8')
    img = cv.imdecode(img, cv.IMREAD_UNCHANGED)
    cv.imshow('Camera', img)
    cv.waitKey(1)
    return img

#%% Send a command and receive a response
def cmd(sock, do, what = '', where = '', at = ''):
    global cmd_no
    cmd_no += 1
    msg = {"N":str(cmd_no)}  # dictionary
    if do == 'move':
        msg["N"] = str(3)
        what = 'car'
        if where == 'forward':
            msg["D1"] = str(3)
        elif where == 'back':
            msg["D1"] = str(4)
        elif where == 'left':
            msg["D1"] = str(1)
        elif where == 'right':
            msg["D1"] = str(2)
        msg["D2"] = str(at)  # at is speed here
        where = ''
    elif do == 'stop':
        msg.update({"N":str(1),"D1":str(0),"D2":str(0),"D3":str(1)})
        what = 'car'
    elif do == 'rotate':
        msg.update({"N":str(5),"D1":str(1),"D2":str(at)})  # at is an angle here
        what = 'ultrasonic unit'
        where = ''
    elif do == 'measure':
        if what == 'distance':
            msg.update({"N":str(21),"D1":str(2)})
        elif what == 'motion':
            msg["N"] = str(6)
            what = ' ' + what
            where = ''
    elif do == 'check':
        msg["N"] = str(23)
        what = 'off the ground'
    
    msg_json = json.dumps(msg)
    print(str(cmd_no) + ': ' + do + ' ' + what + ' ' + where + str(at), end = ': ')
    print("DEBUG - Sending:", msg_json)  # Debug del mensaje enviado
    try:
        sock.send(msg_json.encode())
    except:
        print('Error: ', sys.exc_info()[0])
        sys.exit()

    while 1:
        res = sock.recv(1024).decode()
        print("DEBUG - Raw socket response:", res)  # Ver respuesta completa
        if '_' in res:
            break

    try:
        match = re.search('_(.*)}', res)
        if match:
            res = match.group(1)
            if msg.get("N") == "6":  # Debug para measure motion
                print("DEBUG - After regex:", res)
        else:
            print('received: ', res)
            print('Error: No match found')
            sys.exit()
    except:
        print('received: ', res)
        print('Error: ', sys.exc_info()[0])
        sys.exit()
    
    if res == 'ok' or res == 'true':
        res = 1
    elif res == 'false':
        res = 0
    elif msg.get("N") == "6":
        print("DEBUG - Processing MPU data")
        res = res.split(",")
        print("DEBUG - Split data:", res)
        res = [int(x)/16384 for x in res]  # convert to units of g
        print("DEBUG - Converted to g:", res)
    else:
        res = int(res)

    print(res)
    return res
#%% Connect to car's WiFi
ip = "192.168.4.1"
port = 100
print('Connect to {0}:{1}'.format(ip, port))
car = socket.socket()
try:
    car.connect((ip, port))
except:
    print('Error: ', sys.exc_info()[0])
    sys.exit()
print('Connected!')

#%% Read first data from socket
print('Receive from {0}:{1}'.format(ip, port))
try:
    data = car.recv(1024).decode()
except:
    print('Error: ', sys.exc_info()[0])
    sys.exit()
print('Received: ', data)

#%% Main
#%% Main
cmd(car, do = 'rotate', at = str(90))
cmd(car, do = 'measure', what = 'distance')
cmd(car, do = 'rotate', at = str(30))
cmd(car, do = 'measure', what = 'distance')
cmd(car, do = 'rotate', at = str(150))
cmd(car, do = 'measure', what = 'distance')
cmd(car, do = 'rotate', at = str(150))
cmd(car, do = 'measure', what = 'motion')

