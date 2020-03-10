#!/bin/sh

# apt-get
apt-get update

apt-get install vim --assume-yes
apt-get install exfat-fuse exfat-utils --assume-yes
apt-get install ntpdate
apt-get install i2c-tools

# Needed to initialize pigpio library
sudo pigpiod
