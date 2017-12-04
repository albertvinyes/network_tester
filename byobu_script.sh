#!/bin/bash
dir_path=$(pwd)

byobu new-session -d -s $USER

byobu rename-window -t $USER:0 'Server'
byobu send-keys "cd "$dir_path" && source venv/bin/activate && python run.py" C-m

byobu new-window -t $USER:1 -n 'Scheduler'
byobu send-keys "cd "$dir_path" && source venv/bin/activate && python scheduler.py" C-m
