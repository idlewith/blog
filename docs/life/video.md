# Video


## ffmpeg

cut video

```
ffmpeg -ss 00:30:00 -to 01:05:00 -i input.mp4 output.mp4
```


mp4 to gif


```
ffmpeg -ss 00:11:36 -i ep52.mp4 -t 3 -vf "fps=10,scale=320:-1:flags=lanczos" ep52-short.gif
```