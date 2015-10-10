#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive

apt-get update -qq

curl --silent --location https://deb.nodesource.com/setup_4.x | sudo bash -

apt-get install -y nginx libevent-dev nodejs python-dev libjpeg-dev language-pack-ru-base libtiff5-dev libjpeg8-dev zlib1g-dev \
 libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk binutils libproj-dev

npm install -g phantomjs
 
echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true" | debconf-set-selections
apt-get install -y ttf-mscorefonts-installer

touch /etc/apt/sources.list.d/pgdg.list
echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
  sudo apt-key add -
sudo apt-get update
apt-get install -y postgresql-9.4 postgresql-server-dev-9.4 postgresql-contrib freetds-dev

sudo -u postgres psql -q <<EOF
CREATE DATABASE instagram ENCODING 'UTF-8' LC_COLLATE 'en_US.UTF-8' LC_CTYPE 'en_US.UTF-8';
CREATE DATABASE instagram_test ENCODING 'UTF-8' LC_COLLATE 'en_US.UTF-8' LC_CTYPE 'en_US.UTF-8';
CREATE USER test PASSWORD 'test';
ALTER USER test CREATEDB SUPERUSER;
GRANT ALL PRIVILEGES ON DATABASE instagram to test;
GRANT ALL PRIVILEGES ON DATABASE instagram_test to test;
CREATE EXTENSION adminpack;
EOF

sudo -u postgres psql -q -d instagram <<EOF
CREATE EXTENSION adminpack;
EOF

sudo -u postgres psql -q -d instagram_test <<EOF
CREATE EXTENSION adminpack;
EOF

sed -i "s/# TYPE/local   all             test                               md5\n\n# TYPE/g" /etc/postgresql/9.4/main/pg_hba.conf
service postgresql restart

apt-get install -y python-pip
pip install virtualenv

virtualenv /home/vagrant/env
source /home/vagrant/env/bin/activate
pip install -r /vagrant/requirements.txt
pip install -r /vagrant/requirements-staging.txt
chown -R vagrant:vagrant /home/vagrant/env

ln -s /vagrant/nginx.conf /etc/nginx/sites-enabled/instagram.conf
rm /etc/nginx/sites-enabled/default
sed -i "s/sendfile\([[:space:]]\)on;/sendfile\1off;/g" /etc/nginx/nginx.conf
service nginx restart

sed -i 's/#force_color_prompt=yes/force_color_prompt=yes/g' /home/vagrant/.bashrc
echo "export LC_ALL=\"en_US.UTF-8\"" >> /home/vagrant/.bashrc
cp /vagrant/bash_profile /home/vagrant/.bash_profile
chown vagrant:vagrant /home/vagrant/.bash_profile
