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