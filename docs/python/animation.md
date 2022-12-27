


# manim

## macOS


open vpn

set proxy


```
export https_proxy=http://127.0.0.1:7890
export http_proxy=http://127.0.0.1:7890
export all_proxy=socks5://127.0.0.1:7890
```


使用 homebrew 安装 ffmpeg 和 pango

```
brew install ffmpeg
brew install pango
```


安装 MacTex

```
brew install --cask mactex-no-gui
```

Python安装包

```
pip install manim
```


example code


```
from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
```

generating video

output mp4

```
manim -pqk main.py CreateCircle
```

- p: play
- q: quality
- k: 4k

or  

output is gif

```
manim -pqk --format=gif main.py CreateCircle
```


local config file


must be `manim.cfg`


```
[CLI]
preview=True
quality=k
```
