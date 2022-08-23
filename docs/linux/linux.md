# linux

## 错误：为仓库 'appstream' 下载元数据失败 : Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried



解决：
修改 /etc/yum.repos.d/CentOS-Base.repo，CentOS-AppStream.repo，CentOS-Extras.repo
修改如下：
注释mirrorlist，把baseurl取消注释并修改为阿里云镜像地址
CentOS-Base.repo：

```
# CentOS-Base.repo
[BaseOS]
name=CentOS-$releasever - Base
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=BaseOS&infra=$infra
#baseurl=http://mirror.centos.org/$contentdir/$releasever/BaseOS/$basearch/os/
baseurl=https://mirrors.aliyun.com/centos/$releasever/BaseOS/$basearch/os/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
```

CentOS-AppStream.repo：

```
# CentOS-AppStream.repo
[AppStream]
name=CentOS-$releasever - AppStream
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=AppStream&infra=$infra
#baseurl=http://mirror.centos.org/$contentdir/$releasever/AppStream/$basearch/os/
baseurl=https://mirrors.aliyun.com/centos/$releasever/AppStream/$basearch/os/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
```

CentOS-Extras.repo

```
# CentOS-Extras.repo
[extras]
name=CentOS-$releasever - Extras
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras&infra=$infra
#baseurl=http://mirror.centos.org/$contentdir/$releasever/extras/$basearch/os/
baseurl=https://mirrors.aliyun.com/centos/$releasever/extras/$basearch/os/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
```

修改之后清缓存，制作元数据缓存


```
# 清除所有缓存文件
yum clean all

# 制作元数据缓存
yum makecache
```






下面的一系列指令暂时没用

替换 CentOS-Base.repo 元

cd /etc/yum.repos.d

mv CentOS-Linux-BaseOS.repo CentOS-Linux-BaseOS.repo.backup #备份

wget -O CentOS-LinuxBaseOS.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo #拉取新文件


修改配置

vim /etc/yum.repos.d/CentOS-Linux-AppStream.repo

替换 baseurl

```
#baseurl=http://mirrors.cloud.aliyuncs.com/$contentdir/$releasever/AppStream/$basearch/os/
baseurl=http://mirrors.cloud.aliyuncs.com/centos-vault/8.5.2111/AppStream/$basearch/os/
```

yum makecache