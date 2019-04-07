# supervisor-pushbullet
[![License](https://img.shields.io/pypi/l/supervisor-alert.svg)](https://github.com/drmbk/supervisor-pushbullet/blob/master/LICENSE.txt)

Are you using [Supervisor](http://supervisord.org) to manage processes on a
server? With supervisor-pushbullet you can receive a pushbullet notification when the state of your
processes change. Be the first to know when your services die!

# Manual Configuration

Create the file `/etc/supervisor/conf.d/supervisor_pushbullet.conf` as root:
``` shell
[eventlistener:pushbullet]
command=/opt/tools/supervisor-pushbullet.py --apikey [PushBullet_API_KEY]
process_name=%(program_name)s_%(process_num)s
numprocs=1
events=PROCESS_STATE
autorestart=true
```
Then enable the configuration
``` shell
sudo supervisorctl reread
sudo supervisorctl update
```

[ntfy]: https://github.com/dschep/ntfy
[events]: http://supervisord.org/events.html#event-types
