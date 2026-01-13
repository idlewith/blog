
# VIM init settings


**using english**

```
Vim/vim91/lang -> Vim/vim91/lang1
```


**disable backup**

Vim/vim91/vimrc_example.vim


comment code below

```
if has("vms")
  set nobackup		" do not keep a backup file, use versions instead
else
  set backup		" keep a backup file (restore to previous version)
  if has('persistent_undo')
    set undofile	" keep an undo file (undo changes after closing)
  endif
endif
```

**using custom vimrc**


```
https://github.com/idlewith/vimrc/blob/main/vimrc
```



