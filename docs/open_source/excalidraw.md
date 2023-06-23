# excalidraw: 手绘风格流程图

## 添加自定义字体

1、按照官网进行下载 git clone

```shell
git clone https://github.com/excalidraw/excalidraw
```

2、打开静态资源目录 public，将准备好的字体包放到当前目录下，示例中字体文件名：MyFonts.woff2

3、修改 public/fonts.css，增加如下代码：

```css
@font-face {
  font-family: "MyFonts";
  src: url("MyFonts.woff2");
  font-display: swap;
}
```

4、修改 public/index.html，在head 标签中增加如下代码：

```html
<link
    rel="preload"
    href="MyFonts.woff2"
    as="font"
    type="font/woff2"
    crossorigin="anonymous"
/>
```

5、修改 src/constants.ts，增加字体变量 MyFonts: 

```ts
export const FONT_FAMILY = {
  Virgil: 1,
  Helvetica: 2,
  Cascadia: 3,
};
```

// 变更为

```ts
export const FONT_FAMILY = {
  MyFonts: 1,
  Virgil: 4,
  Helvetica: 2,
  Cascadia: 3,
};
```

6、修改 src/actions/actionProperties.tsx，替换字体的使用：

```tsx
{
    value: FONT_FAMILY.Virgil,
    text: t("labels.handDrawn"),
    icon: FreedrawIcon,
}
```

// 变更为

```tsx
{
    value: FONT_FAMILY.MyFonts,
    text: t("labels.handDrawn"),
    icon: FreedrawIcon,
}
{
    value: FONT_FAMILY.Virgil,
    text: t("labels.handDrawn"),
    icon: FreedrawIcon,
}
```

7、启动服务器查看即可~

```shell
npm start
```

**除了以上方法外，暴力方法：直接覆盖 public/Virgil.woff2 文件即可。但是英文也会用这个字体，不怎么好**

