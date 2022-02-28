# others

## build android apk from kivy and buildozer

ln -s /usr/local/bin/glibtoolize /usr/local/bin/libtoolize

export PATH="/usr/local/opt/openssl@1.1/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib -L/usr/local/opt/zlib/lib"
export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include -I/usr/local/opt/zlib/include"
export PKG_CONFIG_PATH="/usr/local/opt/openssl@1.1/lib/pkgconfig:/usr/local/opt/zlib/lib/pkgconfig"


brew reinstall autoconf automake libtool openssl pkg-config zlib

buildozer android debug deploy run

brew install zlib-ng

