

# MPV


**mpvnet-player download address**

https://github.com/mpvnet-player/mpv.net/releases


**mpv.conf**

```
# 不退出播放器
keep-open=yes

##播放状态记录

#退出时记住播放状态（包括是否暂停、音量、播放速度、位置等）

save-position-on-quit=yes

#播放状态保存位置

watch-later-directory=C:\software\mpv\Cache\watch_later

#不记录是否暂停（除了pause同理可写fullscreen,mute,speed,ontop等参数）

watch-later-options-remove=pause
hwdec=auto
libplacebo-opts=peak_detection_preset=high_quality,color_map_preset=high_quality

# 隐藏进度条
osd-on-seek=no

```
