
# poetry


```shell

pip install poetry
poetry new --src project
cd project
poetry install
```

install third modules

```shell
poetry add requests
```

# pyenv

## install pyenv

Pre-requisites

```shell
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y zlib zlib-devel bzip2-devel openssl-devel sqlite-devel readline-devel git
```

Installation

```shell
curl https://pyenv.run | bash
```

Update your shell environment, I am using zsh.

```
# ~/.zshrc

# PYENV
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

# PYENV Auto-completions. This should be towards the end of the file.
eval "$(pyenv init -)"
```


## install 3.6.15 by pyenv


```
arch -x86_64 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
alias brew86="arch -x86_64 /usr/local/bin/brew"\nalias pyenv86="arch -x86_64 pyenv"
brew86 install pyenv gcc libffi gettext

export PYTHON_BUILD_HOMEBREW_OPENSSL_FORMULA=openssl@1.1
export CPPFLAGS="-I$(brew86 --prefix libffi)/include -I$(brew86 --prefix openssl)/include -I$(brew86 --prefix readline)/lib"
export CFLAGS="-I$(brew86 --prefix openssl)/include -I$(brew86 --prefix bzip2)/include -I$(brew86 --prefix readline)/include -I$(xcrun --show-sdk-path)/usr/include -Wno-implicit-function-declaration"
export LDFLAGS="-L$(brew86 --prefix openssl)/lib -L$(brew86 --prefix readline)/lib -L$(brew86 --prefix zlib)/lib -L$(brew86 --prefix bzip2)/lib -L$(brew86 --prefix gettext)/lib -L$(brew86 --prefix libffi)/lib"

pyenv86 install --patch 3.6.15 <<(curl -sSL https://raw.githubusercontent.com/pyenv/pyenv/master/plugins/python-build/share/python-build/patches/3.6.15/Python-3.6.15/0008-bpo-45405-Prevent-internal-configure-error-when-runn.patch\?full_index\=1)

pyenv install --patch 3.7.9 <<(curl -sSL https://github.com/python/cpython/commit/720bb456dc711b0776bae837d1f9a0b10c28ddf2.patch\?full_index\=1)
```

## install clash


https://luckyfuture.top/config-clash-on-linux#%E5%AE%89%E8%A3%85clash





# deploy

pex buildout, bazel 都做了类似 jar包的操作

WARNING: Value for scheme.headers does not match. Please report this to <https://github.com/pypa/pip/issues/10151>
distutils: /opt/idlepig/apps/include/python3.9/UNKNOWN
sysconfig: /root/Python-3.9.7/Include/UNKNOWN
WARNING: Additional context:
user = False
home = None
root = '/'
prefix = None
Looking in links: /tmp/tmpgxdpm1bw
Processing /tmp/tmpgxdpm1bw/setuptools-57.4.0-py3-none-any.whl
Processing /tmp/tmpgxdpm1bw/pip-21.2.3-py3-none-any.whl
Installing collected packages: setuptools, pip
  WARNING: Value for scheme.headers does not match. Please report this to <https://github.com/pypa/pip/issues/10151>
  distutils: /opt/idlepig/apps/include/python3.9/setuptools
  sysconfig: /root/Python-3.9.7/Include/setuptools
  WARNING: Value for scheme.headers does not match. Please report this to <https://github.com/pypa/pip/issues/10151>
  distutils: /opt/idlepig/apps/include/python3.9/pip
  sysconfig: /root/Python-3.9.7/Include/pip
  WARNING: The script pip3.9 is installed in '/opt/idlepig/apps/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-21.2.3 setuptools-57.4.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
[root@iZwz9cu9zu9ot2cpw1hdw0Z Python-3.9.7]# cd /opt/idlepig/apps/


nohup /root/code/venv/wx/bin/python /root/code/wx/main.py & >/dev/null 2>&1 