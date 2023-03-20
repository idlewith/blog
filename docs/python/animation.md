


# manim

## macOS


open vpn

set proxy


```
export https_proxy=http://127.0.0.1:7890
export http_proxy=http://127.0.0.1:7890
export all_proxy=socks5://127.0.0.1:7890
```

unset https_proxy
unset http_proxy
unset all_proxy


windows

set https_proxy=http://127.0.0.1:7890
set http_proxy=http://127.0.0.1:7890
set all_proxy=socks5://127.0.0.1:7890


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


install mactex


brew install --cask mactex


unset HOMEBREW_BREW_GIT_REMOTE
git -C "$(brew --repo)" remote set-url origin https://github.com/Homebrew/brew


## No module named '_lzma' 

CFLAGS="-I$(brew --prefix xz)/include" LDFLAGS="-L$(brew --prefix xz)/lib" pyenv install 3.9.7


## merge srt

simple

```
ffmpeg -i in.mp4 -vf subtitles=in.srt out.mp4
```

complex

```
ffmpeg -i "NewsDemo.mp4" -lavfi "subtitles=NewsDemo.srt:force_style='Alignment=2,OutlineColour=&H100000000,BorderStyle=3,Outline=1,Shadow=0,Fontsize=24,MarginV=5'" -crf 1 -c:a copy   "NewsDemo_output.mp4"
```




## manim options

disable_caching=True




## azure voicer

https://voiceover.manim.community/en/stable/services.html#azureservice

max letter number: 25