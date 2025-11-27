

# Java to exe



## commands



SimpleGuiApp.java

```java
import javax.swing.*;
import java.awt.*;

public class SimpleGuiApp {
    public static void main(String[] args) {
        // 在 Event-Dispatch Thread 中创建 GUI，保证线程安全
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Simple GUI Demo");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(400, 120);
            frame.setLayout(new FlowLayout());

            JTextField input = new JTextField(20);
            JButton btn = new JButton("显示文字");
            JLabel output = new JLabel("这里将显示你输入的文字");

            btn.addActionListener(e -> {
                String text = input.getText();
                output.setText(text);
            });

            frame.add(new JLabel("输入:"));
            frame.add(input);
            frame.add(btn);
            frame.add(output);

            frame.setLocationRelativeTo(null); // 窗口居中
            frame.setVisible(true);
        });
    }
}

```

java to class

```
javac SimpleGuiApp.java
```


class to jar


```
jar --create --file SimpleGuiApp.jar --main-class SimpleGuiApp SimpleGuiApp.class
```



download Launch4j


launch4j config

```
Output file: javaGui.exe
Jar: select jar file generated above
```

click Build wrapper which like settings icon

input `javaGui.exe`, select all file type

done.




