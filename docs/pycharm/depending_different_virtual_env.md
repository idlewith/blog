# Depending different virtual environment in pycharm external tools

python version: python 3.9.7

```
pip install merge_functions
pip install astunparse==1.6.3
```

External tools settings

Program

```shell
$PyInterpreterDirectory$/mf.exe
```

Arguments

```
-i $FilePath$ -m utils -a
```

Working directory

```
$ProjectFileDir$
```

Advanced Options

```
Synchronize files after exection
Open console for tool output
```