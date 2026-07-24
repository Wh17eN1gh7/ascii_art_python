[English](README.md) | [简体中文](README_CN.md) | [日本語](README_JP.md)



##该工具现已上线网页版，无需下载此脚本，点击[unicode-character-art-generator.noritovo.workers.dev]即可使用

# Unicode Character Art Generator

一个基于 Python 的 Unicode 字符画生成器。

通过读取图片像素灰度，将图片转换为由 Unicode 字符组成的字符画，并输出为 `.txt` 文件。

支持多种字符风格，可用于终端展示、Markdown、论坛签名、头像字符化等场景。

## 功能特点

* 支持常见图片格式（PNG、JPG 等）
* 根据图片灰度自动转换字符
* 输出 Unicode 字符画文本文件
* 支持自定义字符集
* 支持调整生成宽度
* UTF-8 编码输出，支持中文环境

## 效果示例

输入图片：

```
example.png
```

输出：

```
unicode_art.txt
```

生成内容示例：

```
        ⠂⠄⡀
     ⢀⣀⣤⣶⣿
   ⢀⣤⣶⣿⣿⣿
  ⣤⣿⣿⣿⣿⣿
```

实际效果会根据图片内容和字符集变化。

## 环境要求

* Python 3.10+
* Pillow

安装依赖：

```bash
pip install pillow
```

## 使用方法

### 1. 准备图片

将需要转换的图片放入项目目录。

例如：

```
unicode-character-art-generator
│
├── script.py
├── example.png
└── unicode_art.txt
```

默认读取：

```python
image_path = "example.png"
```

如果图片名称不同，可以修改：

```python
image_path = "你的图片名称.png"
```

---

### 2. 选择字符风格

在脚本中修改：

```python
chars = " ⠁⠂⠄⡀⢀⣀⣤⣶⣿"
```

目前提供三种风格：

### Braille 点阵风格

```python
chars = " ⠁⠂⠄⡀⢀⣀⣤⣶⣿"
```

特点：

* Unicode 风格
* 细节丰富
* 适合终端显示

### 高对比 ASCII 风格

```python
chars = " .:-=+*#%@"
```

特点：

* 黑白区别明显
* 适合头像和简单图案

### 细腻 ASCII 风格

```python
chars = "               .,:;i1tfLCG08@"
```

特点：

* 灰度层次更多
* 适合照片转换

---

### 3. 调整图片宽度

修改：

```python
width = 128
```

说明：

| 宽度    | 效果         |
| ----- | ---------- |
| 50 左右 | 较小，适合聊天发送  |
| 70 左右 | 推荐值        |
| 100+  | 细节更多，但文本较宽 |

生成的高度会根据图片比例自动计算。

---

### 4. 运行

执行：

```bash
python script.py
```

成功后：

```
生成完成: unicode_art.txt
```

打开：

```
unicode_art.txt
```

即可查看字符画。

---

## 项目结构

```
unicode-character-art-generator
│
├── script.py              # 主程序
├── example.png            # 示例图片
├── unicode_art.txt        # 输出文件
└── README.md
```

## 注意事项

为了保证字符画正常对齐，建议使用等宽字体打开输出文件，例如：

* Consolas
* Cascadia Mono
* Courier New

普通比例字体可能导致字符错位。

## 原理简介

程序流程：

```
图片
 ↓
读取像素
 ↓
转换灰度
 ↓
根据灰度匹配字符
 ↓
输出 Unicode 字符画
```

灰度越暗：

```
⠁ → ⣿
```

灰度越亮：

```
⣿ → 空格
```

最终形成类似 ASCII Art 的效果。

## License

MIT License
