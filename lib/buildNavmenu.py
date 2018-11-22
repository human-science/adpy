#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Build navigation menu contents with the tool default variable and a specific asciidoc filename from toc.adoc file.
from bs4 import BeautifulSoup
import re
import sys
import os


def main():
    args = sys.argv
    langName = args[1]


    class mergeDoc(object):
        # コンストラクタ（クラス変数のセット）
        def __init__(self, langName):
            self.filename = '../../lib/toc_' + langName + '.adoc'
            self.lang = '../../html/' + langName + '/'
            self.bl = False
            self.opText = ''

        def numbering(self, text, number):
        # ヘディング関数（H1のテキストがある場合の変数セット）
        # H1に変数（{hoge}）が含まれる場合があるため、先に辞書型で全変数を取得する。
            allText = ''
            with open(self.lang + text, 'r', encoding='utf_8_sig') as fh:
                soup = BeautifulSoup(fh, 'lxml')
                soup.h2.string.replace_with(re.sub(r'^\d+', str(number), soup.h2.string))
                for foundH3 in soup.find_all('h3'):
                    foundH3.a.string.replace_with(re.sub(r'^\d+', str(number), foundH3.a.string))
                for foundH4 in soup.find_all('h4'):
                    foundH4.a.string.replace_with(re.sub(r'^\d+', str(number), foundH4.a.string))
                allText = str(soup)

            with open(self.lang + text, 'w', encoding='utf_8_sig') as fh:
                fh.write(allText)

        def heading(self, text):
            headingText = '<li class="drawer-dropdown">\n'
            with open(self.lang + text, 'r', encoding='utf_8_sig') as fh:
                soup = BeautifulSoup(fh, 'lxml')
                # ヘディング1を処理
                headingText += '<a class="drawer-menu-item" href="' +  text + '#' + soup.h2['id'] + '" aria-expanded="true">' + soup.h2.a.string + ' </a>\n'
                if soup.h3 != None:
                    headingText += '<ul class="drawer-dropdown-menu">\n'
                    for foundH3 in soup.find_all('h3'):
                        headingText += '<li>\n<a class="drawer-dropdown-menu-item" href="' + text + '#' + foundH3['id'] + '">' + foundH3.a.string + '</a>\n</li>\n'
                    headingText += '</ul>\n</li>\n'
                fh.close()
                return headingText
            headingText += '</ul>\n</li>\n'
            return headingText

        # 基本処理
        def process(self):
            self.opText += '<button type="button" id="hamburger-button" class="drawer-toggle drawer-hamburger">\n<span class="sr-only">toggle navigation</span>\n<span class="drawer-hamburger-icon"></span>\n</button>\n<div class="drawer-nav-container" id="drawer-nav-container">\n<nav style="display:none;" class="drawer-nav" id="drawer-nav" role="navigation" >\n<ul class="drawer-menu" id="drawer-menu">\n<li class="drawer-brand" id="drawer-brand"><a href="index.html">HOME</a></li>\n'
            cnt = 0
            with open(self.filename, 'r', encoding='utf_8_sig') as fh:
                for line in fh:
                    if self.bl:
                        if re.search(r'^include::', line.strip()) and not re.search(r'^include::index.adoc', line.strip()) and not re.search(r'^99', re.sub(r'^include::([^\[]*?)\[\].*?$', '\\1', line.strip())):
                            cnt = cnt + 1
                            self.numbering(re.sub(r'^include::([^\[]*?)\.adoc\[\].*?$', '\\1.html', line.strip()), cnt)
                            self.opText += self.heading(re.sub(r'^include::([^\[]*?)\.adoc\[\].*?$', '\\1.html', line.strip()))
                    else:
                        if line.strip() == 'toc::[]':
                            self.bl = True
            return self.opText

    mD = mergeDoc(langName)
    htmlText = mD.process()

    # 出力済みHTMLの保存
    f = open('../../lib/menucontent_' + langName + '.html', 'w', encoding='utf_8_sig')
    f.write(htmlText)
    f.close()


if __name__ == '__main__':
    main()
