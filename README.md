[English](README.md) | [简体中文](README_CN.md) | [日本語](README_JP.md)



## Online Version

No Python installation required. Generate Unicode character art directly in your browser:

➡️ [Open Unicode Character Art Generator](https://unicode-character-art-generator.noritovo.workers.dev)

# Unicode Character Art Generator

A Python-based Unicode character art generator.

This project converts images into text-based character art by analyzing image brightness and mapping pixels to Unicode characters.

It supports multiple character styles and outputs the generated artwork as a `.txt` file.

Suitable for terminal displays, Markdown, forum signatures, profile pictures, and other creative uses.

## Features

* Supports common image formats (PNG, JPG, etc.)
* Converts images based on grayscale values
* Exports Unicode character art as text files
* Supports custom character sets
* Adjustable output width
* UTF-8 encoded output for better compatibility

## Example

Input:

```text
example.png
```

Output:

```text
unicode_art.txt
```

Example result:

```text
        ⠂⠄⡀
     ⢀⣀⣤⣶⣿
   ⢀⣤⣶⣿⣿⣿
  ⣤⣿⣿⣿⣿⣿
```

The actual output depends on the input image and selected character set.

## Requirements

* Python 3.10+
* Pillow

Install dependency:

```bash
pip install pillow
```

## Usage

### 1. Prepare an image

Place the image you want to convert into the project folder.

Example:

```text
unicode-character-art-generator
│
├── script.py
├── example.png
└── unicode_art.txt
```

The default input file is:

```python
image_path = "example.png"
```

If your image has a different name, modify it:

```python
image_path = "your_image_name.png"
```

---

### 2. Select a character style

Modify the `chars` variable in the script.

Currently supported styles:

### Braille Dot Style

```python
chars = " ⠁⠂⠄⡀⢀⣀⣤⣶⣿"
```

Features:

* Unicode-based style
* Rich details
* Suitable for terminal display

### High Contrast ASCII Style

```python
chars = " .:-=+*#%@"
```

Features:

* Clear black and white contrast
* Suitable for portraits and simple shapes

### Fine ASCII Style

```python
chars = "               .,:;i1tfLCG08@"
```

Features:

* More grayscale levels
* Better for photographs

---

### 3. Adjust output width

Change:

```python
width = 128
```

Recommended values:

| Width     | Description                         |
| --------- | ----------------------------------- |
| Around 50 | Small output, suitable for messages |
| Around 70 | Recommended balance                 |
| 100+      | More details, but wider text        |

The height is automatically calculated according to the image ratio.

---

### 4. Run

Execute:

```bash
python script.py
```

After successful conversion:

```text
Generated: unicode_art.txt
```

Open:

```text
unicode_art.txt
```

to view the generated character art.

---

## Project Structure

```text
unicode-character-art-generator
│
├── script.py              # Main program
├── example.png            # Example image
├── unicode_art.txt        # Generated output
└── README.md
```

## Notes

For proper alignment, open the output file with a monospaced font.

Recommended fonts:

* Consolas
* Cascadia Mono
* Courier New

Using proportional fonts may cause character alignment issues.

## How It Works

The conversion process:

```text
Image
 ↓
Read pixels
 ↓
Convert to grayscale
 ↓
Map brightness to characters
 ↓
Generate Unicode character art
```

Dark pixels are represented by denser characters:

```text
⠁ → ⣿
```

Bright pixels are represented by lighter characters:

```text
⣿ → space
```

The final result is similar to ASCII Art.

## License

MIT License
