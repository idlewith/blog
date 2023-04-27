


# 用twisted启动一个网络服务


## use twisted to start a http service

```
pip install twisted

mkdir -p /Users/new/logs

nohup /Users/new/.pyenv/versions/3.9.7/bin/python3.9 /Users/new/.pyenv/versions/3.9.7/bin/twistd web --path=/Users/new/Movies > /Users/new/logs/twistd.log 2>&1 &

nohup D:\Python310\Scripts\twistd web --path=D:\movie > D:\movie\logs\twistd.log 2>&1 &
```

## 转换mp4, 提取字幕

```
ffmpeg -i input.mkv -c:v copy -c:a copy output.mp4
```


```
ffprobe input.mkv
```

在命令输出中，找到包含默认字幕流的视频流。默认字幕流通常带有标记 default 或 forced。请记下此字幕流的 ID。


```
ffmpeg -i output.mp4 -filter_complex "[0:v][0:s:ID]overlay[video]" -map [video] -map 0:a -c:v libx264 -crf 18 -preset veryfast -c:a copy -movflags +faststart output_subs.mp4
```






