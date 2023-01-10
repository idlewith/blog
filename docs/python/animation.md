


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


install mactex


brew install --cask mactex


unset HOMEBREW_BREW_GIT_REMOTE
git -C "$(brew --repo)" remote set-url origin https://github.com/Homebrew/brew


## No module named '_lzma' 

CFLAGS="-I$(brew --prefix xz)/include" LDFLAGS="-L$(brew --prefix xz)/lib" pyenv install 3.9.7


## merge srt

```
ffmpeg -i in.mp4 -vf subtitles=in.srt out.mp4
```


ffmpeg -i 20230110.mp4 -vf subtitles=20230110.srt 20230110_output.mp4



## manim options

disable_caching=True




## azure voicer

https://voiceover.manim.community/en/stable/services.html#azureservice