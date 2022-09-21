# javafx


project root path: C:\Users\new\IdeaProjects\demo

open idea

create demo project from javafx template


file -> project structure


Click on + button and select JAR and click on From modules with dependencies


Main Class: select main class

extract to the target JAR

Directory for META-INF/MANIFEST.MF

and select path/to/src

the click ok

menu bar, Build, Build Artifacts, Build

output jar path: C:\Users\new\IdeaProjects\demo\out\artifacts\demo_jar\demo.jar

cd output jar path


download javafx sdk

login javafx website: https://gluonhq.com/products/javafx/

download platform sdk and unzip to C:\lib directory

java --module-path "C:\lib\javafx-sdk-19\lib" --add-modules javafx.controls,javafx.fxml -jar demo.jar


Conversion of jar to exe

download 1.8 jdk

https://www.java.com/zh-CN/download/

Download Launch4J and install it.

https://sourceforge.net/projects/launch4j/files/


launch4j parameter

C:\code\demo1\out

C:\Users\new\IdeaProjects\demo\out\artifacts\demo_jar\demo.jar

--module-path "C:\lib\javafx-sdk-19\lib" --add-modules javafx.controls,javafx.fxml 


save the configuration

click gear icon(settings) to generate exe file


