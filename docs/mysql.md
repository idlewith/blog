# mysql

## 修改MySQL数据库的编码
  
```bash
alter database blog character set utf8 collate utf8_general_ci;
```

## install mysql in mac


install

```bash
brew install mysql-connector-c
brew install mysql
```

connect mysql

```bash
mysql -uroot
```

to have launchd start mysql now and restart at login:

```bash
brew services start mysql
```

Or, if you don't want/need a background service you can just run:

```bash
mysql.server start
```

modify password

```bash
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpass');
```


if mysql installed

```bash
brew link --overwrite mysql
```

if error happened

```bash
sudo chown -R '${username}' /usr/local
unset TMPDIR
bash mysql_install_db --verbose --user=root
--basedir="$(brew --prefix mysql)"--datadir=/usr/local/var/mysql --tmpdir=/tmp
```


unset auth

```bash
update mysql.user set authentication_string=null where User='tag';
ALTER USER 'tag'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'ms88888888';
```