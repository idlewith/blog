

# aria2c

## download

https://github.com/aria2/aria2/releases/tag/release-1.36.0


## run

touch `aria2.conf` and `aria2.session`

aria2c.exe --conf-path=./aria2c.conf

open url below

notice: not `https`

http://aria2c.com



# conf for `aria2.conf`


```
## '#'开头为注释内容, 选项都有相应的注释说明, 根据需要修改 ##
## 被注释的选项填写的是默认值, 建议在需要修改时再取消注释  ##

## 文件保存相关 ##

# 文件的保存路径(可使用绝对路径或相对路径), 默认: 当前启动位置
dir=\\Mac\Home\Movies\downloads
# 启用磁盘缓存, 0为禁用缓存, 需1.16以上版本, 默认:16M
disk-cache=32M
# 文件预分配方式, 能有效降低磁盘碎片, 默认:prealloc
# 预分配所需时间: none < falloc ? trunc < prealloc
# falloc和trunc则需要文件系统和内核支持
# NTFS建议使用falloc, EXT3/4建议trunc, MAC 下需要注释此项
file-allocation=falloc
# 断点续传
continue=true

## 下载连接相关 ##

# 最大同时下载任务数, 运行时可修改, 默认:5
max-concurrent-downloads=5
# 同一服务器连接数, 添加时可指定, 最大:16
max-connection-per-server=16
# 最小文件分片大小, 添加时可指定, 取值范围1M -1024M, 默认:20M
# 假定size=10M, 文件为20MiB 则使用两个来源下载; 文件为15MiB 则使用一个来源下载
#min-split-size=10M
# 单个任务最大线程数, 添加时可指定, 默认:5
split=32
# 整体下载速度限制, 运行时可修改, 默认:0
#max-overall-download-limit=0
# 单个任务下载速度限制, 默认:0
#max-download-limit=0
# 整体上传速度限制, 运行时可修改, 默认:0
#max-overall-upload-limit=0
# 单个任务上传速度限制, 默认:0
#max-upload-limit=0
# 禁用IPv6, 默认:false
disable-ipv6=true

## 进度保存相关 ##

# 从会话文件中读取下载任务
input-file=aria2.session
# 在Aria2退出时保存`错误/未完成`的下载任务到会话文件
save-session=aria2.session
# 定时保存会话, 0为退出时才保存（此处需要设置，否则失去自动保存）, 需1.16.1以上版本, 默认:0
save-session-interval=60

## RPC相关设置 ##

# 启用RPC, 默认:false
enable-rpc=true
# 允许所有来源, 默认:false
rpc-allow-origin-all=true
# 允许非外部访问, 默认:false
rpc-listen-all=true
# 事件轮询方式, 取值:[epoll, kqueue, port, poll, select], 不同系统默认值不同
#event-poll=select
# RPC监听端口, 端口被占用时可以修改, 默认:6800
#rpc-listen-port=6800

## BT/PT下载相关 ##

# 当下载的是一个种子(以.torrent结尾)时, 自动开始BT任务, 默认:true
#follow-torrent=true
# BT监听端口, 当端口被屏蔽时使用, 默认:6881-6999
listen-port=51413
# 单个种子最大连接数, 默认:55
#bt-max-peers=55
# 打开DHT功能, PT需要禁用, 默认:true
#enable-dht=false
# 打开IPv6 DHT功能, PT需要禁用
#enable-dht6=false
# DHT网络监听端口, 默认:6881-6999
#dht-listen-port=6881-6999
# 本地节点查找, PT需要禁用, 默认:false
#bt-enable-lpd=false
# 种子交换, PT需要禁用, 默认:true
#enable-peer-exchange=false
# 每个种子限速, 对少种的PT很有用, 默认:50K
#bt-request-peer-speed-limit=50K
# 客户端伪装, PT需要
peer-id-prefix=-TR2770-
user-agent=Transmission/2.77
# 当种子的分享率达到这个数时, 自动停止做种, 0为一直做种, 默认:1.0
#seed-ratio=0
# 强制保存会话, 即使任务已经完成, 默认:false
# 较新的版本开启后会在任务完成后依然保留.aria2文件
#force-save=true
# BT校验相关, 默认:true
#bt-hash-check-seed=true
# 继续之前的BT任务时, 无需再次校验, 默认:false
bt-seed-unverified=true
# 保存磁力链接元数据为种子文件(.torrent文件), 默认:false
bt-save-metadata=true

# bt-tracker 更新，解决Aria2 BT下载速度慢没速度的问题
# https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt
# https://github.com/XIU2/TrackersListCollection/blob/master/best_aria2.txt
bt-tracker=http://1337.abcvg.info:80/announce,http://bt.okmp3.ru:2710/announce,http://nyaa.tracker.wf:7777/announce,http://open.acgnxtracker.com:80/announce,http://p2p.0g.cx:6969/announce,http://share.camoe.cn:8080/announce,http://torrentsmd.com:8080/announce,http://tr.cili001.com:8070/announce,http://tracker.bt4g.com:2095/announce,http://tracker.files.fm:6969/announce,http://tracker.gbitt.info:80/announce,http://tracker.ipv6tracker.ru:80/announce,http://tracker.mywaifu.best:6969/announce,http://tracker.tfile.co:80/announce,http://trackme.theom.nz:80/announce,http://v6-tracker.0g.cx:6969/announce,http://vps02.net.orel.ru:80/announce,http://web.open-tracker.cf:6969/announce,http://www.all4nothin.net:80/announce.php,http://www.wareztorrent.com:80/announce,https://1337.abcvg.info:443/announce,https://opentracker.i2p.rocks:443/announce,https://tr.abiir.top:443/announce,https://tr.burnabyhighstar.com:443/announce,https://tracker.foreverpirates.co:443/announce,https://tracker.gbitt.info:443/announce,https://tracker.imgoingto.icu:443/announce,https://tracker.kuroy.me:443/announce,https://tracker.lilithraws.cf:443/announce,https://tracker.loligirl.cn:443/announce,https://tracker.tamersunion.org:443/announce,https://tracker1.520.jp:443/announce,https://trackme.theom.nz:443/announce,udp://9.rarbg.com:2810/announce,udp://aarsen.me:6969/announce,udp://acxx.de:6969/announce,udp://aegir.sexy:6969/announce,udp://astrr.ru:6969/announce,udp://bedro.cloud:6969/announce,udp://bt.ktrackers.com:6666/announce,udp://bt1.archive.org:6969/announce,udp://epider.me:6969/announce,udp://exodus.desync.com:6969/announce,udp://htz3.noho.st:6969/announce,udp://ipv4.tracker.harry.lu:80/announce,udp://ipv6.tracker.monitorit4.me:6969/announce,udp://laze.cc:6969/announce,udp://mail.artixlinux.org:6969/announce,udp://mirror.aptus.co.tz:6969/announce,udp://moonburrow.club:6969/announce,udp://movies.zsw.ca:6969/announce,udp://open.demonii.com:1337/announce,udp://open.dstud.io:6969/announce,udp://open.publictracker.xyz:6969/announce,udp://open.stealth.si:80/announce,udp://open.tracker.ink:6969/announce,udp://opentor.org:2710/announce,udp://opentracker.i2p.rocks:6969/announce,udp://p4p.arenabg.com:1337/announce,udp://private.anonseed.com:6969/announce,udp://public.publictracker.xyz:6969/announce,udp://retracker01-msk-virt.corbina.net:80/announce,udp://run.publictracker.xyz:6969/announce,udp://slicie.icon256.com:8000/announce,udp://static.54.161.216.95.clients.your-server.de:6969/announce,udp://t.133335.xyz:6969/announce,udp://thagoat.rocks:6969/announce,udp://thetracker.org:80/announce,udp://torrents.artixlinux.org:6969/announce,udp://tracker-udp.gbitt.info:80/announce,udp://tracker.4.babico.name.tr:3131/announce,udp://tracker.altrosky.nl:6969/announce,udp://tracker.arcbox.cc:6969/announce,udp://tracker.artixlinux.org:6969/announce,udp://tracker.auctor.tv:6969/announce,udp://tracker.beeimg.com:6969/announce,udp://tracker.birkenwald.de:6969/announce,udp://tracker.ccp.ovh:6969/announce,udp://tracker.cyberia.is:6969/announce,udp://tracker.dler.com:6969/announce,udp://tracker.doko.moe:6969/announce,udp://tracker.joybomb.tw:6969/announce,udp://tracker.leech.ie:1337/announce,udp://tracker.moeking.me:6969/announce,udp://tracker.monitorit4.me:6969/announce,udp://tracker.openbittorrent.com:6969/announce,udp://tracker.opentrackr.org:1337/announce,udp://tracker.pimpmyworld.to:6969/announce,udp://tracker.renfei.net:8080/announce,udp://tracker.skynetcloud.site:6969/announce,udp://tracker.skyts.net:6969/announce,udp://tracker.srv00.com:6969/announce,udp://tracker.torrent.eu.org:451/announce,udp://tracker1.bt.moack.co.kr:80/announce,udp://tracker6.lelux.fi:6969/announce,udp://uploads.gamecoast.net:6969/announce,udp://v1046920.hosted-by-vdsina.ru:6969/announce,udp://www.peckservers.com:9000/announce,ws://hub.bugout.link:80/announce,wss://tracker.openwebtorrent.com:443/announce
```