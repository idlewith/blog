# auto switch keyboard

## vscode


### macos

Auto Switch Input Method: Obtain IMCmd

```
/usr/local/bin/im-select
```


Auto Switch Input Method: Switch IMCmd

```
/usr/local/bin/im-select {im} && /usr/local/bin/im-select com.apple.keylayout.ABC
```

### windows


Auto Switch Input Method: Obtain IMCmd

```
/usr/local/bin/im-select.exe
```


Auto Switch Input Method: Switch IMCmd

```
/usr/local/bin/im-select.exe {im} && /usr/local/bin/im-select.exe 1033
```


## pycharm

install `ideavim` and `ideavim extensions`

open ~/.ideavim

```
set keep-english-in-normal
```

其它可选指令:

set keep-english-in-normal 开启输入法自动切换功能(默认)
set keep-english-in-normal-and-restore-in-insert 回到insert模式时恢复输入法
set nokeep-english-in-normal-and-restore-in-insert 保留输入法自动切换功能，但是回到insert模式不恢复输入法
set nokeep-english-in-normal 关闭输入法自动切换功能
