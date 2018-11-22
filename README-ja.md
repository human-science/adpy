# ADPY
AsciidocファイルをAsciidoctorとPythonを介してHTMLファイルに変換します。また、Asciidoctor-pdfを介してPDFファイルを出力することもできます。

この文書は以下の言語で読むことができます。

[English](https://github.com/human-science/adpy/README.md) | [日本語](https://github.com/human-science/adpy/README-ja.md)

より詳しい情報をお知りになりたいかたは弊社ウェブサイトへお越しください。

[humanscience.co.jp](https://www.science.co.jp/)

## 動作条件

ADPYをLinux、OS X(Mac)またはWindowsで動作させるためには、下記のRubyとPythonの実装すべてが必要です。

* [Ruby](https://www.ruby-lang.org/)

* [Asciidoctor](https://github.com/asciidoctor/asciidoctor#requirements)

* [Asciidcotor-pdf](https://github.com/asciidoctor/asciidoctor-pdf)

* [Python3.X](https://www.python.org/downloads/)

* [Beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

* [lxml](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser)

## 使い方

1. このリポジトリーをクローンします。

    ```
    $ git clone git@git
    $ cd adpy
    ```

2. `adoc` ディレクトリ内でAsciidocファイルを作成します。

    ```
    $ cd adoc/en
    $ vi index.adoc
    ```

3. リポジトリーのルートディレクトリに戻り、以下のコマンドを実行します。

    ```
    $ cd ../
    $ adpy html en
    ```

    * For windows,
      ```
      $ cd ../
      $ adpy.bat html en
      ```

4. `html\en`フォルダ内に変換済みのhtmlファイルが書き出されます。

## 書き出し時のコマンドライン引数

ADPYは、書き出し時に2つのコマンドライン引数を取ることができます。

```
$ adpy [File type] [Language code]
```

例えば、Asciidocファイルを日本語のPDFに変換したいときは、以下のようなコマンド文になります。

```
$ adpy pdf ja
```

コマンドライン引数に何も指定されていない場合は、`File type`には`html`が、`Language code`には`en`が設定されます。

* File type

    変換するファイル形式を選択できます。変換したファイルは、コマンドライン引数で指定したファイル形式と同名のフォルダ内に出力されます。何も設定されていない場合は、デフォルトの`html`が設定されます。

    * html
    * pdf

* Language code

    変換する言語コードを選択できます。変換したファイルは、コマンドライン引数で指定した言語コードと同名のフォルダ内に出力されます。何も設定されていない場合は、デフォルトの`en`が設定されます。

    * en
    * ja

## その他のオプション

* バージョンを表示する

    ```
    $ adpy version
    ```

* マニュアルページを表示する

    ```
    $ adpy man
    ```

## ライセンス

Copyright © 2018 Human Science Co., Ltd. Free use of this software is granted under the terms of the MIT License.

For the full text of the license, see the [LICENSE](https://github.com/human-science/adpy/LICENCE) file.

This tool has inspired by [https://github.com/continuous-manual-writing](https://github.com/continuous-manual-writing)
