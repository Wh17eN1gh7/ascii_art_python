# Unicode Character Art Generator

Pythonで作成したUnicode文字アート生成ツールです。

画像の明るさ（グレースケール）を解析し、それぞれのピクセルをUnicode文字に変換することで、画像から文字だけで構成されたアートを生成します。

複数の文字スタイルに対応しており、生成結果は`.txt`ファイルとして保存できます。

ターミナル表示、Markdown、SNS投稿、プロフィール画像の装飾など、さまざまな用途に利用できます。

## 主な機能

* PNG、JPGなど一般的な画像形式に対応
* 画像の明るさに応じて文字を自動変換
* Unicode文字アートをテキストファイルとして出力
* 使用する文字セットを自由に変更可能
* 出力サイズ（横幅）を調整可能
* UTF-8形式で保存

## 使用例

入力：

```text
example.png
```

出力：

```text
unicode_art.txt
```

生成例：

```text
        ⠂⠄⡀
     ⢀⣀⣤⣶⣿
   ⢀⣤⣶⣿⣿⣿
  ⣤⣿⣿⣿⣿⣿
```

※ 実際の結果は使用する画像や文字セットによって変化します。

## 必要な環境

* Python 3.10以上
* Pillow

インストール：

```bash
pip install pillow
```

## 使い方

### 1. 画像を準備する

変換したい画像をプロジェクトフォルダに配置します。

例：

```text
unicode-character-art-generator
│
├── script.py
├── example.png
└── unicode_art.txt
```

デフォルトでは：

```python
image_path = "example.png"
```

を読み込みます。

画像名が違う場合は：

```python
image_path = "画像ファイル名.png"
```

に変更してください。

---

### 2. 文字スタイルを選択する

スクリプト内の`chars`を変更することで、生成スタイルを変更できます。

### Braille（点字）スタイル

```python
chars = " ⠁⠂⠄⡀⢀⣀⣤⣶⣿"
```

特徴：

* Unicode文字を使用
* 細かい表現が可能
* ターミナル表示に適しています

### 高コントラストASCIIスタイル

```python
chars = " .:-=+*#%@"
```

特徴：

* 黒と白の差が分かりやすい
* シンプルな画像に適しています

### 詳細ASCIIスタイル

```python
chars = "               .,:;i1tfLCG08@"
```

特徴：

* より多くの階調表現が可能
* 写真向きです

---

### 3. 出力サイズを調整する

変更箇所：

```python
width = 128
```

目安：

| 横幅    | 特徴            |
| ----- | ------------- |
| 約50   | 小さく表示、メッセージ向き |
| 約70   | バランスが良い推奨値    |
| 100以上 | 高精細だが横幅が広い    |

高さは画像の縦横比から自動計算されます。

---

### 4. 実行する

以下を実行します：

```bash
python script.py
```

成功すると：

```text
生成完了: unicode_art.txt
```

と表示されます。

生成された：

```text
unicode_art.txt
```

を開くと文字アートを確認できます。

---

## プロジェクト構成

```text
unicode-character-art-generator
│
├── script.py              # メインプログラム
├── example.png            # サンプル画像
├── unicode_art.txt        # 出力ファイル
└── README.md
```

## 注意事項

文字の位置を正しく表示するため、等幅フォントで開くことをおすすめします。

推奨フォント：

* Consolas
* Cascadia Mono
* Courier New

通常のプロポーショナルフォントでは文字がずれる場合があります。

## 仕組み

処理の流れ：

```text
画像
 ↓
ピクセル情報を取得
 ↓
グレースケールへ変換
 ↓
明るさに応じて文字を割り当て
 ↓
Unicode文字アートを生成
```

暗い部分：

```text
⠁ → ⣿
```

明るい部分：

```text
⣿ → 空白
```

のように変換され、最終的にASCII Artに似た文字画像になります。

## License

MIT License
