# Android

# disable system upgrade automatically


## install adb


```
brew install android-platform-tools
```


## pair device


macos

```
adb pair ip:port
```

windows

```
adb connect ip:port
```


list devices


```
adb devices
```


## disable auto upgrade

disable

```
adb shell pm disable-user com.hihonor.ouc 
```


enable

```
adb shell pm enable com.hihonor.ouc 
```


## disconnect


```
adb disconnect
```
