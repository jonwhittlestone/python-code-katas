from io import StringIO
import pprint
print('Chapter 05 - Exercise 19')
print('/etc/passwd to dict')


fakefile = StringIO('''
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
jon:x:1000:1000:Jon Whittlestone,,,:/home/jon:/usr/bin/zsh
systemd-coredump:x:998:998:systemd Core Dumper:/:/sbin/nologin
vboxadd:x:999:1::/var/run/vboxadd:/bin/false
postgres:x:124:130:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
rabbitmq:x:125:132:RabbitMQ messaging server,,,:/var/lib/rabbitmq:/usr/sbin/nologin
taiga:x:1001:1001:,,,:/home/taiga:/bin/bash
''')

def passwd_to_dict():
    users = []
    idx_username = 0
    idx_user_id = 2
    for current_line in fakefile:
        if not current_line.startswith(('\n', '#')):
            parts = current_line.split(':')
            users.append({
                parts[idx_username]:int(parts[idx_user_id].strip())
            })
    return users

if __name__ == '__main__':
    pprint.pprint(passwd_to_dict())
