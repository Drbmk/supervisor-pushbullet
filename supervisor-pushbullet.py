#!/usr/bin/python
# -*- coding: utf-8 -*-
# supervisor-pushbullet - Receive notifications for Supervisor process events by pushbullet notifications
# Copyright 2019 Mathias Da Silva
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__version__ = "0.1.0"
import sys
import argparse
from supervisor.childutils import listener
from pushbullet import Pushbullet

def write_stdout(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def write_stderr(s):
    sys.stderr.write(s)
    sys.stderr.flush()


def main():
    parser = argparse.ArgumentParser(description="Supervisor event listener to notify on process events.")
    parser.add_argument("--apikey", help="Specify the pushbullet api key", required=True)
    args = parser.parse_args()

    pb_api_key = Pushbullet(args.apikey)

    while True:
        headers, body = listener.wait(sys.stdin, sys.stdout)
        body = dict([pair.split(":") for pair in body.split(" ")])

        write_stderr("Headers: %r\n" % repr(headers))
        write_stderr("Body: %r\n" % repr(body))

        #Check if the process is in "STOPPED STATE" and send a pushbullet notification
        if headers["eventname"] == "PROCESS_STATE_EXITED":
            write_stderr("Process state stopping...\n")
            process_name = body.get('processname')
            push = pb_api_key.push_note("Supervisord Alert","Process in stopped state: "+process_name)
            push
        #Supervisor acknowledge
        write_stdout("RESULT 2\nOK")

if __name__ == "__main__":
    main()
