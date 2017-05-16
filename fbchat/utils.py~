import re
import json
from time import time
from random import random
USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
]

def now():
    return int(time()*1000)

def get_json(text):
    return json.loads(re.sub(r"^[^{]*", '', text, 1))

def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)

def generateMessageID(client_id=None):
    k = now()
    l = int(random() * 4294967295)
    return ("<%s:%s-%s@mail.projektitan.com>" % (k, l, client_id));

def getSignatureID():
    return hex(int(random() * 2147483648))

def generateOfflineThreadingID() :
    ret = now()
    value = int(random() * 4294967295);
    string = ("0000000000000000000000" + bin(value))[-22:]
    msgs = bin(ret) + string
    return str(int(msgs,2))

