
# apple

```
  ____  _             _     ___              
 / ___|| |__    __ _ | |_  / _ \  _ __   ___ 
| |    | '_ \  / _` || __|| | | || '_ \ / __|
| |___ | | | || (_| || |_ | |_| || |_) |\__ \
 \____||_| |_| \__,_| \__| \___/ | .__/ |___/
                                 |_|         
```



## ss-local



cd ~/Library/Application Support/ShadowsocksX-NG-R8

rm ss-local

vi ss-local

```bash
#!/bin/zsh

~/Library/Application Support/ShadowsocksX-NG-R8/ss-local-2.5.6.12.static/ss-local
networksetup -setproxyautodiscovery USB\ 10/100/1000\ LAN on
```

chmod +x ss-local




setup auto proxy enable on command

```
networksetup -setproxyautodiscovery USB\ 10/100/1000\ LAN on
networksetup -setproxyautodiscovery USB\ 10/100/1000\ LAN off
```




To restart shadowsocks-libev after an upgrade:
  brew services restart shadowsocks-libev
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/shadowsocks-libev/bin/ss-local -c /usr/local/etc/shadowsocks-libev.json


brew install shadowsocks-libev v2ray-plugin

## Then copy binaries to the App

cp -f /usr/local/opt/shadowsocks-libev/bin/ss-local  /Applications/ShadowsocksX-NG.app/Contents/Resources/ss-local
cp -f /usr/local/opt/v2ray/bin/v2ray  /Applications/ShadowsocksX-NG.app/Contents/Resources/v2ray-plugin

## And remove quarantine attribute to allow run binary

sudo xattr -d com.apple.quarantine '/Applications/ShadowsocksX-NG.app/Contents/Resources/v2ray-plugin'


view process of shadowsocks

```
lsof -iTCP -sTCP:LISTEN -n -P
```

```
COMMAND     PID         USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
Shadowsoc 65979 zhouxinzheng   11u  IPv4 0xd38e381a21fb3505      0t0  TCP 127.0.0.1:8090 (LISTEN)
Shadowsoc 65979 zhouxinzheng   12u  IPv6 0xd38e3823bb1a9aad      0t0  TCP [::1]:8090 (LISTEN)
ss-local  75261 zhouxinzheng    6u  IPv4 0xd38e381a2851e505      0t0  TCP 127.0.0.1:1086 (LISTEN)
privoxy   75265 zhouxinzheng    3u  IPv4 0xd38e381a284d0505      0t0  TCP 127.0.0.1:1087 (LISTEN)
```

check whether turn traffic

```
curl --socks5 127.0.0.1:1086 http://cip.cc
```

```
IP	: 103.137.63.129
地址	: 亚太地区  亚太地区

数据二	: 台湾省 | 彼得巧科技企业社

数据三	: 巴基斯坦

URL	: http://www.cip.cc/103.137.63.129
```

command list for get proxy settings 


```
$ system_profiler SPNetworkDataType # 获取完整网络配置信息

$ networksetup -listallnetworkservices # 列举所有网络设备
$ networksetup -getwebproxy Wi-Fi # 获取特定网络设备的系统代理配置

```


change terminal proxy automatically for mac

```
#!/bin/zsh
# Auto configure zsh proxy env based on system preferences
# Sukka (https://skk.moe)

# Cache the output of scutil --proxy
__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY=$(scutil --proxy)

# Pattern used to match the status
__ZSH_OSX_AUTOPROXY_HTTP_PROXY_ENABLED_PATTERN="HTTPEnable : 1"
__ZSH_OSX_AUTOPROXY_HTTPS_PROXY_ENABLED_PATTERN="HTTPSEnable : 1"
__ZSH_OSX_AUTOPROXY_FTP_PROXY_ENABLED_PATTERN="FTPSEnable : 1"
__ZSH_OSX_AUTOPROXY_SOCKS_PROXY_ENABLED_PATTERN="SOCKSEnable : 1"

__ZSH_OSX_AUTOPROXY_HTTP_PROXY_ENABLED=$__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY[(I)$__ZSH_OSX_AUTOPROXY_HTTP_PROXY_ENABLED_PATTERN]
__ZSH_OSX_AUTOPROXY_HTTPS_PROXY_ENABLED=$__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY[(I)$__ZSH_OSX_AUTOPROXY_HTTPS_PROXY_ENABLED_PATTERN]
__ZSH_OSX_AUTOPROXY_FTP_PROXY_ENABLED=$__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY[(I)$__ZSH_OSX_AUTOPROXY_FTP_PROXY_ENABLED_PATTERN]
__ZSH_OSX_AUTOPROXY_SOCKS_PROXY_ENABLED=$__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY[(I)$__ZSH_OSX_AUTOPROXY_SOCKS_PROXY_ENABLED_PATTERN]

# http proxy
if (( $__ZSH_OSX_AUTOPROXY_HTTP_PROXY_ENABLED )); then
    __ZSH_OSX_AUTOPROXY_HTTP_PROXY_SERVER=${${__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY#*HTTPProxy : }[(f)1]}
    __ZSH_OSX_AUTOPROXY_HTTP_PROXY_PORT=${${__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY#*HTTPPort : }[(f)1]}
    export http_proxy="http://${__ZSH_OSX_AUTOPROXY_HTTP_PROXY_SERVER}:${__ZSH_OSX_AUTOPROXY_HTTP_PROXY_PORT}"
    export HTTP_PROXY="${http_proxy}"
fi
# https_proxy
if (( $__ZSH_OSX_AUTOPROXY_HTTPS_PROXY_ENABLED )); then
    __ZSH_OSX_AUTOPROXY_HTTPS_PROXY_SERVER=${${__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY#*HTTPSProxy : }[(f)1]}
    __ZSH_OSX_AUTOPROXY_HTTPS_PROXY_PORT=${${__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY#*HTTPSPort : }[(f)1]}
    export https_proxy="http://${__ZSH_OSX_AUTOPROXY_HTTPS_PROXY_SERVER}:${__ZSH_OSX_AUTOPROXY_HTTPS_PROXY_PORT}"
    export HTTPS_PROXY="${https_proxy}"
fi
# ftp_proxy
if (( $__ZSH_OSX_AUTOPROXY_FTP_PROXY_ENABLED )); then
    __ZSH_OSX_AUTOPROXY_FTP_PROXY_SERVER=${${__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY#*FTPProxy : }[(f)1]}
    __ZSH_OSX_AUTOPROXY_FTP_PROXY_PORT=${${__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY#*FTPPort : }[(f)1]}
    export ftp_proxy="http://${__ZSH_OSX_AUTOPROXY_FTP_PROXY_SERVER}:${__ZSH_OSX_AUTOPROXY_FTP_PROXY_PORT}"
    export FTP_PROXY="${ftp_proxy}"
fi
# all_proxy
if (( $__ZSH_OSX_AUTOPROXY_SOCKS_PROXY_ENABLED )); then
    __ZSH_OSX_AUTOPROXY_SOCKS_PROXY_SERVER=${${__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY#*SOCKSProxy : }[(f)1]}
    __ZSH_OSX_AUTOPROXY_SOCKS_PROXY_PORT=${${__ZSH_OSX_AUTOPROXY_SCUTIL_PROXY#*SOCKSPort : }[(f)1]}
    export all_proxy="http://${__ZSH_OSX_AUTOPROXY_SOCKS_PROXY_SERVER}:${__ZSH_OSX_AUTOPROXY_SOCKS_PROXY_PORT}"
    export ALL_PROXY="${all_proxy}"
elif (( $__ZSH_OSX_AUTOPROXY_HTTP_PROXY_ENABLED )); then
    export all_proxy="${http_proxy}"
    export ALL_PROXY="${all_proxy}"
fi
```





## doing-设置terminal代理

打开ss之后，通过代理访问google

http_proxy=http://localhost:1087 curl -I http://google.com


## minikube mirrors

minikube start --image-mirror-country=cn   --iso-url=https://kubernetes.oss-cn-hangzhou.aliyuncs.com/minikube/iso/minikube-v1.6.2.iso  --registry-mirror=https://mhzm7ggy.mirror.aliyuncs.com  --image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers






## 更换brew镜像

科大真香实例：

```bash
git -C "$(brew --repo)" remote set-url origin https://mirrors.ustc.edu.cn/brew.git

git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git

git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git

if [ $SHELL = "/bin/bash" ] # 如果你的是bash
then 
    echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/' >> ~/.bash_profile
    source ~/.bash_profile
elif [ $SHELL = "/bin/zsh" ] # 如果用的shell 是zsh 的话
then
    echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/' >> ~/.zshrc
    source ~/.zshrc
fi

brew update
```

如果需要恢复原有镜像源的话（国内镜像源突然不能用了或版本不够新）

```bash
git -C "$(brew --repo)" remote set-url origin https://github.com/Homebrew/brew.git

git -C "$(brew --repo homebrew/core)" remote set-url origin https://github.com/Homebrew/homebrew-core.git

git -C "$(brew --repo homebrew/cask)" remote set-url origin https://github.com/Homebrew/homebrew-cask.git

# 找到 ~/.bash_profile 或者 ~/.zshrc 中的HOMEBREW_BOTTLE_DOMAIN 一行删除

brew update
```

如果不行的话可以依次尝试以下命令

```bash
brew doctor
brew update-reset
brew update
```


## Hide your computer name in ZSH/BASH

vim .zshrc

```bash
export PS1="[~]$ "; clear;
```

## 关闭登陆界面多个用户登陆


```bash
sudo defaults write /Library/Preferences/com.apple.loginwindow SHOWOTHERUSERS_MANAGED -bool FALSE
```

## 强开随航

```bash
defaults write com.apple.sidecar.display AllowAllDevices -bool true
defaults write com.apple.sidecar.display hasShownPref -bool true
```

## 环境变量配置

因为terminal每次只会加载.zshrc，所以必须要在.zshrc里面写alias和环境变量，才会每次重启终端生效配置

初始化的配置

```bash
alias t="ssh root@idlepig.cn"
alias ll="ls -l"
alias idlepig="cd /Users/username/docs/idlepig/source; source /Users/username/code/idlepig/bin/activate"

export PATH=/Users/username/code/idlepig/bin:/Users/username/Library/Python/3.8/bin:$PATH
```



## 苹果 电源适配器延长线缆


https://www.apple.com.cn/shop/product/MK122CH/A


## 调整鼠标速度

```bash
defaults write -g com.apple.mouse.scaling 18
```

terminal输入然后重启，已爽死，嫌快的调小数值就行

还有滚轮速度

```bash
defaults write -g com.apple.scrollwheel.scaling 1.2
```


