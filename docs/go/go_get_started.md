

# get started


brew install go


cd ~/go

make sure `bin`, `pkg` and `src` 3 paths in `~/go`, create dir if not exists

vim ~/.zshrc

```
export GOPATH=~/go
export GOROOT=/usr/local/go
PATH="${GOPATH}/bin:${PATH}"
export PATH
```


mkdir a new project like `~/go/src/demoProject`

then execute command `go mod init demoProject`

using install instead of get in command, like `go get ...`, please use `go install ....`

then it will download exe file in `~/go/bin`




# windows


基本的

GOOS=windows GOARCH=amd64 go build -o bin/app-amd64.exe app.go


GOOS=windows GOARCH=386 go build -o bin/app-386.exe app.go


## cross platform compile

GOOS=windows GOARCH=amd64 CGO_ENABLED=1 go build -o bin/app-386.exe main.go

error info: gcc_libinit_windows.c:7:10: fatal error: 'windows.h' file not found

brew install mingw-w64

add /usr/local/Cellar/mingw-w64/10.0.0_3/bin to PATH



编译x64

可执行文件


```
CGO_ENABLED=1 CC=x86_64-w64-mingw32-gcc CXX=x86_64-w64-mingw32-g++ GOOS=windows GOARCH=amd64 go build -x -v -ldflags "-s -w -H windowsgui " -o out_x64.exe
```

静态库

```
CGO_ENABLED=1 CC=x86_64-w64-mingw32-gcc CXX=x86_64-w64-mingw32-g++ GOOS=windows GOARCH=amd64 go build -buildmode=c-archive -x -v -ldflags "-s -w -H windowsgui " -o bin/x64/x64.a main.go
```


动态库

将`-buildmode=c-archive`改为`-buildmode=c-shared`即可




编译x86


可执行文件

```
CGO_ENABLED=1 CC=i686-w64-mingw32-gcc CXX=i686-w64-mingw32-g++ GOOS=windows GOARCH=386 go build -x -v -ldflags "-s -w  -H windowsgui " -o out_x86.exe
```

静态库

```
CGO_ENABLED=1 CC=i686-w64-mingw32-gcc CXX=i686-w64-mingw32-g++ GOOS=windows GOARCH=386 go build -buildmode=c-archive -x -v -ldflags  "-s -w -H windowsgui " -o bin/x86/x86.a main.go
```

动态库

将`-buildmode=c-archive`改为`-buildmode=c-shared`即可














# mac

GOOS=darwin GOARCH=amd64 go build -o bin/app-amd64-darwin app.go

GOOS=darwin GOARCH=386 go build -o bin/app-386-darwin app.go

after build, rename app to app.app, app.app will not open console


# linux

GOOS=linux GOARCH=amd64 go build -o bin/app-amd64-linux app.go

GOOS=linux GOARCH=386 go build -o bin/app-386-linux app.go


go install fyne.io/fyne/v2/cmd/fyne

fyne install



fyne package -os android -appID com.idlewith.fyne
no Android NDK found in $ANDROID_HOME/ndk-bundle nor in $ANDROID_NDK_HOME


no compiler for arm was found in the NDK (tried /Users/new/android/NDK/toolchains/llvm/prebuilt/darwin-x86_64/bin/armv7a-linux-androideabi16-clang). Make sure your NDK version is >= r19c. Use `sdkmanager --update` to update it