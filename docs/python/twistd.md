



# use twisted to start a http service

```
pip install twisted

mkdir -p /Users/new/logs

nohup /Users/new/.pyenv/versions/3.9.7/bin/python3.9 /Users/new/.pyenv/versions/3.9.7/bin/twistd web --path=/Users/new/Movies > /Users/new/logs/twistd.log 2>&1 &
```




