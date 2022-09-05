from time import sleep
from mysql.connector import connect
from os import system
system('')

# Global Cursor Object
pwd = '123456789'
db = 'chatrooms'
db = connect(host="localhost", user="root", password=pwd,
             database=db, autocommit=True)
cur = db.cursor(buffered=True)


def main():
    cmd = 'SELECT * FROM chat'
    cur.execute(cmd)
    msg, prev_msg, msgs = None, None, cur.fetchall()
    msgs = msgs[:len(msgs) - 1]
    '''
    while True:
        print('\033[?1049h', end='')
        username = input("Username: ")
        if not (len(username) >= 13):
            break
    '''
    print('\033[?1049l', end='')
    print('\n'.join([str(_) for _ in msgs]))

    while True:
        try:
            cur.execute(cmd)
            entry = cur.fetchall()[-1]
            id, user, msg = entry
            if msg != prev_msg:
                print(f'{user} | {msg}')
                prev_msg = msg
            sleep(1)
        except KeyboardInterrupt:
            sendmsg = input('> ')
            cur.execute(f"insert into chat values({id+1}, 'testuser', '{sendmsg}')")


main()
