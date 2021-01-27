python -m pip install --upgrade pip
pip install gunicorn
sudo cp -r /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -s reload
gunicorn -w 2 -b 0:8080 hello:wsgi_application