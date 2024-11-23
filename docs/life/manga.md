# Manga

# extract picture from mobi

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

## extract picture from epub

```
pip install epub-extractor
epub-extract-jpeg 1.epub
```

