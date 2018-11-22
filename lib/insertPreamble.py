#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Insert preamble to the specific asciidoc files in adoc folder.
# Toll's default preamble can be overridden by preamble written in a specific asciidoc file from adoc folder.
import re
import sys
import os


def main():
    args = sys.argv
    langName = args[1]

    preamble = ''':doctype: book
:lang: ''' + langName + '''
:hardbreaks:
:sectnums!:
:sectlinks:
:sectids:
:experimental:
:toc: macro
:docinfo: shared
:docinfodir: ../../lib
ifdef::backend-html5[:nofooter:]
ifdef::backend-html5[:linkcss:]
:idprefix:
:imagesdir: images
:toclevels: 2
:stylesdir: css
:icons: font
:chapter-label:
:leveloffset: 1
'''

    fnameList = os.listdir('.')
    for file in fnameList:
        fname, ext = os.path.splitext(file)
        if ext == '.adoc':
            f = open(file, 'r', encoding='utf_8_sig')
            l = f.readlines()
            l.insert(0, preamble + '\n')
            f = open(file, 'r+', encoding='utf_8_sig')
            f.writelines(l)
            f.close


if __name__ == '__main__':
    main()
