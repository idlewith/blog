# Manga

# extract image from mobi

before execute command, build virtualenv first, below is demo:

```
cd ~/code/venv
python -m venv mobi_extract

source ~/code/venv/mobi_extract/bin/activate
cd ~/code/test_extract_mobi
cp ~/lan_folder/1.mobi .
```

unpack

```
pip install mobi
mobiunpack 1.mobi .
```

## extract image from epub

```
pip install epub-extractor
epub-extract-jpeg 1.epub
```

## extract image from pdf


```
pip install wheel
pkg install libjpeg-turbo
LDFLAGS="-L/system/lib64/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install Pillow

pkg install poppler

pip install poppler-utils
pip install pdf2image
pip install pdf2image-cli

pdf2image mu.pdf --output mu
```


