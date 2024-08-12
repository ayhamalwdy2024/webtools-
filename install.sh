#!/bin/bash

# اسم المستودع على GitHub
GITHUB_REPO="https://github.com/YourUsername/YourRepository.git"

# مجلد مؤقت للتنزيل
TEMP_DIR=$(mktemp -d)

# تنزيل المشروع من GitHub
echo "Cloning the GitHub repository..."
git clone $GITHUB_REPO $TEMP_DIR

# الانتقال إلى مجلد المشروع
cd $TEMP_DIR

# تثبيت المكتبات المطلوبة
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

# تثبيت nmap إذا لم يكن مثبتًا
if ! command -v nmap &> /dev/null; then
    echo "nmap not found, installing nmap..."
    sudo apt-get install -y nmap
else
    echo "nmap is already installed."
fi

echo "Installation complete! The tool is ready to use."
