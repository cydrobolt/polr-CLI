cp polr_cli.py /usr/bin/polr
export PATH=/usr/bin:$PATH
chmod 755 /usr/bin/polr
echo -e "\e[0;36mInstall Complete. \n\e[0;32mUse polr to access the cli. Otherwise, use polr [url] to quickly shorten a URL. \nIf errors were produced, you may need to run this script as superuser. "
echo -e "\e[0m"
