#!/bin/bash

# تحديث النظام وتثبيت pip
echo "Updating system and installing pip..."
sudo apt-get update -y
sudo apt-get install -y python3-pip

# تثبيت المكتبات المطلوبة بواسطة pip
echo "Installing required Python libraries..."
pip3 install requests builtwith python-nmap colorama

# تثبيت nmap إذا لم يكن مثبتًا
if ! command -v nmap &> /dev/null; then
    echo "nmap not found, installing nmap..."
    sudo apt-get install -y nmap
else
    echo "nmap is already installed."
fi

echo "All dependencies are installed successfully!"
