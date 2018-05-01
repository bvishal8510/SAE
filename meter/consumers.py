import json
import serial
import requests
from channels import Group, Channel
from channels.auth import channel_session_user, channel_session_user_from_http
from django.contrib.auth.models import User
from django.core import serializers
from time import sleep
import serial


# @channel_session_user_from_http
# def ws_connect(message):
def ws_connect():
    pass
    # sermain = serial.Serial('/dev/tty.usbmodem1d11', 9600)
    # sermain.write(0)                                               #to turn meter on
    # user = User.objects.get(pk = 1)
    # d = {'email': user.email}
    # r = requests.get('http://5e620c2d.ngrok.io/get_bal/', params = d)
    # dat = r.json()
    # bal = dat['balance']
    # ser1 = serial.Serial('/dev/tty.usbmodem1d11', 9600)
    # ser2 = serial.Serial('/dev/tty.usbmodem1d11', 9600)
    # while True:
    #     d = {}
    #     if bal > 0:
    #         current = ser1.readline()      #multiply by 1000 or whatever needed
    #         voltage = ser2.readline()      #multiply by 1000 or whatever needed
    #         inst_power  = current * voltage
    #         bal = bal - inst_power
    #         d['current'] = current
    #         d['voltage'] = voltage
    #         d['inst_power'] = inst_power
    #         d['left_power'] = bal
    #         if bal < 150:                              #give some value
    #             d['status'] = 0
    #         else:
    #             d['status'] = 1
    #         message.reply_channel.send(d)
    #         sleep(1)


# @channel_session_user
def ws_disconnect():       #send left out energy as argument
    # pass

    # sermain = serial.Serial('/dev/tty.usbmodem1d11', 9600)
    # sermain.write(0)                                               #to turn meter on
    user = User.objects.get(pk = 1)
    d = {'email': user.email}
    d['energy'] = message.energy
    r = requests.put('http://5e620c2d.ngrok.io/get_bal/', data = d)
    
    #         room.websocket_group.discard(message.reply_channel)

def ws_receive(message):
    pass
    # print(6)
    # payload = json.loads(message['text'])
    # payload['reply_channel'] = message.content['reply_channel']
    # Channel("chat.receive").send(payload)


# @catch_client_error
# @channel_session_user
# def chat_join(message):
#     print(7)
#     l1=[]
#     l2=[]
#     room = get_room_or_error(message["room"], message.user)
#     if NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
#         room.send_message(None, message.user, MSG_TYPE_ENTER)
#     log = Comments.objects.filter(room=message["room"])
#     for l in log:
#         l1.append(l.comment)
#         l1.append(str(l.user))
#         l2.extend([l1])
#         l1=[]
#     # log1 = serializers.serialize('json', log)
#     # print("----",log1)
#     # for i in log1:
#     #     print(i)
#     # print("=========",log1)
#     room.websocket_group.add(message.reply_channel)
#     message.channel_session['rooms'] = list(set(message.channel_session['rooms']).union([room.id]))
#     message.reply_channel.send({
#         "text": json.dumps({
#             "join": str(room.id),
#             "title": room.title,
#             "d":l2,
#         }),
#     })


# @channel_session_user
# @catch_client_error
# def chat_leave(message):
#     print(9)
#     room = get_room_or_error(message["room"], message.user)
#     if NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
#         room.send_message(None, message.user, MSG_TYPE_LEAVE)

#     room.websocket_group.discard(message.reply_channel)
#     message.channel_session['rooms'] = list(set(message.channel_session['rooms']).difference([room.id]))
#     message.reply_channel.send({
#         "text": json.dumps({
#             "leave": str(room.id),
#         }),
#     })


# @catch_client_error
# @channel_session_user
# def chat_send(message):
#     print(10)
#     if int(message['room']) not in message.channel_session['rooms']:
#         raise ClientError("ROOM_ACCESS_DENIED")
#     room = get_room_or_error(message["room"], message.user)
#     Comments.objects.create(room = message["room"],user=message.user, comment=message["message"])
#     room.send_message(message["message"], message.user)