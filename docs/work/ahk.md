# ahk

## clipboardToImageFile

```
#Include "Gdip_All.ahk"
 ; https://github.com/buliasz/AHKv2-Gdip

^!q::
{
 Send "#{PrintScreen}"
Sleep 1000

FilePath := "D:\work_image\" A_Now ".png"
clipboardToImageFile(FilePath)
sleep 1000
}

clipboardToImageFile(filePath) {
 pToken  := Gdip_Startup()
 pBitmap := Gdip_CreateBitmapFromClipboard() ; Clipboard -> bitmap
 Gdip_SaveBitmapToFile(pBitmap, filePath)    ; Bitmap    -> file
 Gdip_DisposeImage(pBitmap)
Gdip_Shutdown(pToken)
}
```