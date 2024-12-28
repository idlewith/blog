
# edit with ndd

## add

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\OpenWithNdd]
@="Edit with Ndd"

[HKEY_CLASSES_ROOT\*\shell\OpenWithNdd\command]
@="\"C:\\path\\to\\ndd.exe\" \"%1\""
```


## remove

```
Windows Registry Editor Version 5.00

[-HKEY_CLASSES_ROOT\*\shell\OpenWithNdd]

[-HKEY_CLASSES_ROOT\txtfile\shell\OpenWithNdd]

```




# cmd


## add cmd reg


```
Windows Registry Editor Version 5.00

; Created by: Shawn Brink

; http://www.sevenforums.com

; Tutorial: http://www.sevenforums.com/tutorials/47415-open-command-window-here-administrator.html

[-HKEY_CLASSES_ROOT\Directory\shell\runas]

[HKEY_CLASSES_ROOT\Directory\shell\runas]

@="Open cmd here as Admin"

"HasLUAShield"=""

[HKEY_CLASSES_ROOT\Directory\shell\runas\command]

@="cmd.exe /s /k pushd \"%V\""

[-HKEY_CLASSES_ROOT\Directory\Background\shell\runas]

[HKEY_CLASSES_ROOT\Directory\Background\shell\runas]

@="Open cmd here as Admin"

"HasLUAShield"=""

[HKEY_CLASSES_ROOT\Directory\Background\shell\runas\command]

@="cmd.exe /s /k pushd \"%V\""

[-HKEY_CLASSES_ROOT\Drive\shell\runas]

[HKEY_CLASSES_ROOT\Drive\shell\runas]

@="Open cmd here as Admin"

"HasLUAShield"=""

[HKEY_CLASSES_ROOT\Drive\shell\runas\command]

@="cmd.exe /s /k pushd \"%V\""

```


## remove cmd reg


```
Windows Registry Editor Version 5.00

; Created by: Shawn Brink

; http://www.sevenforums.com

; Tutorial: http://www.sevenforums.com/tutorials/47415-open-command-window-here-administrator.html

[-HKEY_CLASSES_ROOT\Directory\shell\runas]

[-HKEY_CLASSES_ROOT\Directory\Background\shell\runas]

[-HKEY_CLASSES_ROOT\Drive\shell\runas]

```