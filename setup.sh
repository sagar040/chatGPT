#!/bin/bash
#
# Author: Sagar Biswas (sagar040)
#
# https://github.com/sagar040/chatGPT
#
# Setup file

dir_api="./api"
api_conf="$dir_api/conf.py"

date_path=$(which date)
DAT=$($date_path)

if [ -f $api_conf ]; then
    echo -e "\033[33m(!)\033[0m '$api_conf' already exists.\n"
    echo -n "Do you want to remove it ? (y/n) : "
    read purge;
    if [ $purge = 'y' ]; then
        backup=$(cat "$dir_api/.backup")
        rm -rf $dir_api
        echo -e "\n-- $dir_api removed"
        mkdir $dir_api
        echo "-- backing up old api key"
        echo -e "$backup\n" > "$dir_api/.backup"
        echo "-- old api keys are stored at '$dir_api/.backup'"
        echo -e "-- creating $api_conf\n"
        touch $api_conf
        echo -e -n "\033[35mEnter your api key:\033[33;5m "
        read key;
        echo -e -n "\033[0m"
        echo -n "IyBhcGkgY29uZmlndXJhdGlvbgojIGFkZCB5b3VyIGFwaSBrZXkgaGVyZQojIGtleSA9ICcnCg==" | base64 -d > $api_conf
        echo "key = '$key'" >> $api_conf
        echo -e "$DAT\n" >> "$dir_api/.backup"
        echo -e "$key\n" >> "$dir_api/.backup"
        echo -e "\033[32mdone..\033[0m"
    else
        echo -e "\nyou can change your api key at '$api_conf'"
        exit
    fi
else
    mkdir $dir_api
    touch $api_conf
    echo -e -n "\033[35mEnter your api key:\033[33;5m "
    read key;
    echo -e -n "\033[0m"
    echo -n "IyBhcGkgY29uZmlndXJhdGlvbgojIGFkZCB5b3VyIGFwaSBrZXkgaGVyZQojIGtleSA9ICcnCg==" | base64 -d > $api_conf
    echo "key = '$key'" >> $api_conf
    echo -e "$DAT\n" > "$dir_api/.backup"
    echo -e "$key\n" >> "$dir_api/.backup"
    echo -e "\033[32mdone..\033[0m"
fi