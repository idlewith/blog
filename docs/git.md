# git

## issue分支和master分支冲突

先在本地master分支pull issue分支，会自动合并，

自动合并不了的，才去手动合并，

然后再push到master分支上，github上的冲突会显示ok

```bash
git add .
git commit --no-edit
git push origin master
```

## 处理别人的pull request

先添加别人的源

```bash
git remote add otfsenter https://github.com/otfsenter/test_merge.git

```

现在remote有自己的、别人的各种分支

```bash
git remote -v
```

fetch别人的代码

```bash
git fetch otfsenter
```

会下载远程的别人的代码

local的分支有自己的、别人的各种分支

```bash
git branch -a
```



切换到别人的代码，review或者查看

```bash
git checkout -b otfsenter remotes/otfsenter/main
```

切换到自己的分支, merge别人的分支

```bash
git checkout main
git merge otfsenter
git branch -D otfsenter
git push
```

参考资料

https://liuyib.github.io/2020/09/19/add-commits-to-others-pr/#%E5%9B%BE%E5%BD%A2%E5%8C%96%E6%96%B9%E5%BC%8F
