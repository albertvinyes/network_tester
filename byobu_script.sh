#!/usr/bin/env bash

byobu new-session -d -s $USER

byobu rename-window -t $USER:0 'Server'
byobu send-keys "cd /home/pi/git/network_tester && source venv/bin/activate && python run.py" C-m

byobu new-window -t $USER:1 -n 'OAM S'
byobu send-keys "cd /home/pi/git/network_tester && source venv/bin/activate && python schedulery" C-m
