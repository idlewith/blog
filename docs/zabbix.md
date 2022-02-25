# zabbix

## Install Zabbix repository

```
rpm -Uvh https://repo.zabbix.com/zabbix/5.4/rhel/8/x86_64/zabbix-release-5.4-1.el8.noarch.rpm
dnf clean all
```

## Install Zabbix server, frontend, agent

```
dnf install zabbix-server-mysql zabbix-web-mysql zabbix-apache-conf zabbix-sql-scripts zabbix-agent
```

## Create initial database

```
dnf install mariadb -y
systemctl start mariadb
```

Make sure you have database server up and running.

Run the following on your database host.


```
mysql
mysql> create database zabbix character set utf8 collate utf8_bin;
mysql> create user zabbix@localhost identified by 'password';
mysql> grant all privileges on zabbix.* to zabbix@localhost;
mysql> quit;
```

On Zabbix server host import initial schema and data. You will be prompted to enter your newly created password.

```
zcat /usr/share/doc/zabbix-sql-scripts/mysql/create.sql.gz | mysql -uzabbix -p zabbix
```

## Configure the database for Zabbix server

Edit file /etc/zabbix/zabbix_server.conf
```
DBPassword=password
```

## Start Zabbix server and agent processes

Start Zabbix server and agent processes and make it start at system boot.

```
systemctl restart zabbix-server zabbix-agent httpd php-fpm
systemctl enable zabbix-server zabbix-agent httpd php-fpm
```

## Configure Zabbix frontend

Connect to your newly installed Zabbix frontend: http://server_ip_or_name/zabbix
Follow steps described in Zabbix documentation: Installing frontend