import re
import urllib2 as ulib
import time
import fbchat
import requests

mail = raw_input("enter username")
password = raw_input("enter password")
client = fbchat.Client(mail, password)

def weather_report(text):
    text = text.replace(" ","+")
    req = ulib.Request('https://google.com/search?q='+text, headers={'User-Agent' : "Mozilla/5.0","Accept-Language": "en-US,en;q=0.5"})
    dumpdata=ulib.urlopen(req)
    l=dumpdata.read()
    cont = re.findall('<b>(.*?)</b>',l)
    cont1 = re.findall('<span class="wob_t" style="display:inline">(.*?)</span>',l)
    cont1[0]= cont1[0].replace('\xc2\xb0', ' ')
    cont2 = re.findall('<td style="white-space:nowrap;padding-right:15px;color:#666">(.*?)</td>',l)
    cont3 = re.findall('<td style="white-space:nowrap;padding-right:15px;color:#666">.*?<span class="wob_t" style="display:inline">(.*?)</span></td>',l)
    cont4 = re.findall('<td style="white-space:nowrap;padding-right:0px;vertical-align:top;color:#666">(.*?)</td>',l)
    k=cont[1],cont1[0],cont2[0],"wind: " + cont3[0],cont4[0]
    return k

valid = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_? ')
def test(s):
    return set(s).issubset(valid)


def query(q):
    sess = requests.Session()
    r = sess.get("http://www.yourbot.com/index.php?mode=ask")
    r = sess.post(
            "http://www.yourbot.com/index.php?mode=ask",
            data={
                "question": q
            }
    )
    l=r.content
    cont = re.findall('</strong>(.*?)</p>',l)
    if len(cont)!=0:
        return cont[0]
    else:
        return "dont know!!"

def reply(friend_name):
    count = 0
    while True:
        friend = client.getUsers(friend_name)[0]
        last_messages = client.getThreadInfo(friend.uid, 0)
        #print last_messages[0].is_unread,last_messages[0].body

        #print client.getUserInfo(friend.uid,0)
        #print last_messages[0].is_unread
        if not last_messages[0].is_unread :
            count = count+1
        if count >= 3:
            break
        #print client.getUnread()

        if (not test(last_messages[0].body.lower())):
            print "invalid"
            client.send(friend.uid, " ")
            client.markAsRead(friend.uid)
            break
        if (last_messages[0].is_unread):
            recv_msg = last_messages[0].body.lower()
            print recv_msg
            if ("weather" in recv_msg):

                try:
                    send_msg = weather_report(recv_msg)
                    for msg in send_msg:
                        client.send(friend.uid, msg)
                except:
                    client.send(friend.uid, "enter place and query properly")
                    client.markAsRead(friend.uid)
                    break

                client.markAsRead(friend.uid)
            elif recv_msg == "wassup":
                client.send(friend.uid, "sky")
                client.markAsRead(friend.uid)
            else:
                client.markAsRead(friend.uid)
                send_msg = query(recv_msg)
                client.send(friend.uid, send_msg)
            client.markAsRead(friend.uid)
friend_list = ['sinchan','vikas kotana','kamineni ramakrishna','sai raghu kokkiligadda']
i=0
while True:
    if(i<len(friend_list)):
        print friend_list[i]
        reply(friend_list[i])
        i=i+1
    else:
        i=0
