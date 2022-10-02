# qt

brew install qt@5

If you need to have qt@5 first in your PATH, run:
  echo 'export PATH="/usr/local/opt/qt@5/bin:$PATH"' >> ~/.zshrc

For compilers to find qt@5 you may need to set:
  export LDFLAGS="-L/usr/local/opt/qt@5/lib"
  export CPPFLAGS="-I/usr/local/opt/qt@5/include"


export CMAKE_PREFIX_PATH=/usr/local/opt/qt@5


then reload in cmake menu


qmake -project
qmake


add below to myproject.pro file

```
CONFIG -= console
CONFIG+=sdk_no_version_check
QT += widgets
```

remove below config from myproject.pro

```
cmake-build-debug/untitled1_autogen/mocs_compilation.cpp \
cmake-build-debug/CMakeFiles/3.23.2/CompilerIdC/CMakeCCompilerId.c \
cmake-build-debug/CMakeFiles/3.23.2/CompilerIdCXX/CMakeCXXCompilerId.cpp
```



make


then make a main.o file



./configure -arch x86 -platform macx-g++ --universal -cocoa -debug-and-release -opensource -static -fast -no-accessibility -no-sql-sqlite -no-qt3support -no-opengl -no-openvg -qt-zlib -no-gif -no-libmng -qt-libmng -no-libtiff -qt-libjpeg -no-3dnow -sse -no-sse2 -no-openssl -no-dbus -no-phonon -no-multimedia -no-audio-backend -webkit -no-script -no-scripttools -no-declarative -nomake demos -nomake examples -no-exceptions -no-accessibility -confirm-license


invalid
g++ main.o -o out
gcc main.o -o out
