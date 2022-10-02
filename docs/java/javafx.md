# javafx



## jdk 8

download IDEA 2021.1.3


create project from javafx template, select jdk 1.8


project root path: C:\Users\new\IdeaProjects\untitled


Project Structure -> Project Settings -> Artifacts -> Add -> JavaFx application -> From module 'untitled' -> select main class

select "Java FX" menu

Applicaton class: sample.Main

Native bundle: exe


IDEA: Build -> Build Artifacts -> Build


then cd in project root path


```
javapackager -makeall -appclass sample.Main
```

output

```
没有基础 JDK。程序包将使用系统 JRE。
没有基础 JDK。程序包将使用系统 JRE。
Creating app bundle: Main in C:\Users\new\IdeaProjects\untitled\dist\bundles
Result application bundle: C:\Users\new\IdeaProjects\untitled\dist\bundles
检测到 [iscc.exe] 版本 0, 但需要版本 5。
由于配置问题, 跳过了打包程序EXE 安装程序: 找不到 InnoSetup 编译器 (iscc.exe)。
修复建议:   从 http://www.jrsoftware.org 下载 InnoSetup 5 或更高版本, 然后将其添加到 PATH。
由于配置问题, 跳过了打包程序MSI 安装程序: 找不到 WiX 工具 (light.exe, candle.exe)。
修复建议:   从 http://wix.sf.net 下载 WiX 3.0 或更高版本, 然后将其添加到 PATH。
```


cd exe path: C:\Users\new\IdeaProjects\untitled\dist\bundles\Main


touch run.bat

```
Main
```

touch run.vbs

```
Set ws = CreateObject("Wscript.Shell")
ws.run "cmd /c run.bat",vbhide
```


select all files in **exe path**

General

    select "Create SFX(Self-extracting archive) archive"

Advanced

    SFX options

    General

        Path to extract: javafx_program

    Setup

        Run after extraction: run.vbs

    Modes

        Slient Mode: Hide all

    Update

        Overwrite mode: Overwrite all files

    
if want to pacakge step by step install program


you need install  InnoSetup 5 and WiX 3.0

innosetup link: https://files.jrsoftware.org/is/5/

add **C:\Program Files (x86)\Inno Setup 5** to PATH


install .NET Framework 3.5.1

https://www.microsoft.com/en-us/download/details.aspx?id=22


wix link: https://wixtoolset.org/releases/v3.11.2/stable

wix actual link: https://github.com/wixtoolset/wix3/releases/tag/wix3112rtm

click install png

add **C:\Program Files (x86)\WiX Toolset v3.11\bin** to PATH


rerun 


```
C:\Users\new\IdeaProjects\untitled>javapackager -makeall -appclass sample.Main 
```


## newest java(jdk 17) to exe

use jpackage with maven


reference link

https://www.bilibili.com/video/BV1yh411s7jz/?vd_source=918504544d1d699edc0acd85b9d9319c


pom.xml


```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.topyunp</groupId>
    <artifactId>JavaFXApp</artifactId>
    <version>1.0-SNAPSHOT</version>
    <name>JavaFXApp</name>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <junit.version>5.7.1</junit.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.openjfx</groupId>
            <artifactId>javafx-controls</artifactId>
            <version>11.0.2</version>
        </dependency>
        <dependency>
            <groupId>org.openjfx</groupId>
            <artifactId>javafx-fxml</artifactId>
            <version>11.0.2</version>
        </dependency>

        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>${junit.version}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
            <version>${junit.version}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <pluginManagement>
            <plugins>
                <plugin>
                    <groupId>com.github.akman</groupId>
                    <artifactId>jpackage-maven-plugin</artifactId>
                    <version>0.1.3</version>
                    <configuration>
                        <!--
                          Specifies the JDK home path which provides the tool needed.
                          If not specified the jpackage tool executable will be find in
                          the following order:

                            - user specified JDK home directory by toolchains-plugin
                            - JDK home directory specified by system variable JAVA_HOME
                            - system path specified by system variable PATH
                        -->
                        <toolhome>${env.JPACKAGE_HOME}</toolhome>

                        <!--
                          Specifies the location in which generated output files are placed.
                          Default value: ${project.build.directory}/jpackage
                        -->
                        <dest>${project.build.directory}/jpackage</dest>

                        <!--
                          Specifies version of the application and/or package.
                        -->
                        <appversion>1.0</appversion>

                        <name>JavaFxApp</name>

                        <!--
                          Specifies the module path. The path where the jlink tool
                          discovers observable modules: modular JAR files, JMOD files,
                          exploded modules. If this option is not specified, then
                          the default module path is $ JAVA_HOME/jmods. This directory
                          contains the java.base module and the other standard and
                          JDK modules. If this option is specified but the java.base
                          module cannot be resolved from it, then the jlink command
                          appends $ JAVA_HOME/jmods to the module path.
                          Pass on &dash;-modulepath option to jlink.

                          pathelements - passed to jlink as is
                          filesets - sets of files (without directories)
                          dirsets - sets of directories (without files)
                          dependencysets - sets of dependencies with specified includes
                                           and excludes patterns (glob: or regex:)
                                           for file names and regex patterns only
                                           for module names, and excludes
                                           for automatic modules
                        -->
                        <modulepath>
                            <dependencysets>
                                <dependencyset>
                                    <includeoutput>true</includeoutput>
                                    <excludeautomatic>true</excludeautomatic>
                                </dependencyset>
                            </dependencysets>
                        </modulepath>
                        <module>com.topyunp.javafxapp/com.topyunp.javafxapp.HelloApplication</module>
                        <windirchooser>true</windirchooser>
                        <winmenu>true</winmenu>
                        <winperuserinstall>true</winperuserinstall>
                        <winshortcut>true</winshortcut>
                    </configuration>
                </plugin>
            </plugins>
        </pluginManagement>

        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>11</source>
                    <target>11</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.openjfx</groupId>
                <artifactId>javafx-maven-plugin</artifactId>
                <version>0.0.7</version>
                <executions>
                    <execution>
                        <!-- Default configuration for running with: mvn clean javafx:run -->
                        <id>default-cli</id>
                        <configuration>
                            <mainClass>com.topyunp.javafxapp/com.topyunp.javafxapp.HelloApplication</mainClass>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>com.github.akman</groupId>
                <artifactId>jpackage-maven-plugin</artifactId>
                <executions>
                    <execution>
                        <id>jpackage-installer</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>jpackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

main content

```

...

<module>com.topyunp.javafxapp/com.topyunp.javafxapp.HelloApplication</module>
<windirchooser>true</windirchooser>
<winmenu>true</winmenu>
<winperuserinstall>true</winperuserinstall>
<winshortcut>true</winshortcut>

...

<configuration>
    <mainClass>com.topyunp.javafxapp/com.topyunp.javafxapp.HelloApplication</mainClass>
</configuration>

...

```

```
mvn jpackage:jpackage
```
