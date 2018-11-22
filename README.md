# ADPY
ADPY is a convert Asciidoc file to html file via Asciidoctor and Python. Also can be use for convert Asciidoc file to PDF file via Asciidoctor-pdf.

This document is also available in the following languages:

[English](https://github.com/human-science/adpy/README.md) | [日本語](https://github.com/human-science/adpy/README-ja.md)

Please visit our company website for more information:

[humanscience.co.jp](https://www.science.co.jp/)

## Requirements

ADPY works on Linux, macOS and Windows and requires all of the following implementations of Ruby and python:

* [Ruby](https://www.ruby-lang.org/)

* [Asciidoctor](https://github.com/asciidoctor/asciidoctor#requirements)

* [Asciidcotor-pdf](https://github.com/asciidoctor/asciidoctor-pdf)

* [Python3.X](https://www.python.org/downloads/)

* [Beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

* [lxml](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser)

## Usage

1. Clone this repository.

    ```
    $ git clone git@git
    $ cd adpy
    ```

2. Write your asciidoc files in `adoc` directory.

    ```
    $ cd adoc/en
    $ vi index.adoc
    ```

3. Back to the root directory, execute a command as below.

    ```
    $ cd ../
    $ adpy html en
    ```

    For windows,
      ```
      $ cd ../
      $ adpy.bat html en
      ```

4. You can see the converted html files in `html\en` folder.

## Options to conversion

ADPY can take two optional arguments as below for conversion.

```
$ adpy [File type] [Language code]
```

For example, you can run the following commands to convert Asciidoc files to a PDF file in Japanese.

```
$ adpy pdf ja
```

If no arguments are set, `html` is defined as `File type` and `en` is defined as `Language code`.

* File type

    You can select a file type to be converted, from html and pdf. The converted file is output to a folder with the same name as the file type specified in the command line argument. With no arguments set, html is defined by default.

    * html
    * pdf

* Language code

    You can select a language code to be converted from `en` and `ja`. The converted file is output to a folder with the same name as the language code specified in the command line argument. With no arguments set, `en` is defined by default.

    * en
    * ja

## Other options

* Show version

    ```
    $ adpy version
    ```

* Show man page

    ```
    $ adpy man
    ```

## Copyright

Copyright © 2018 Human Science Co., Ltd. Free use of this software is granted under the terms of the MIT License.

For the full text of the license, see the [LICENSE](https://github.com/human-science/adpy/LICENCE) file.

This tool has inspired by [https://github.com/continuous-manual-writing](https://github.com/continuous-manual-writing)
