#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Generate a toc.adoc file with the tool default variable and a specific asciidoc filename from adoc folder.
# Toll's default variables can be overridden by variables written in a specific asciidoc file from adoc folder.
import re
import sys
import os


def main():
    args = sys.argv
    langName = args[1]

    preamble = ''':doctype: book
:lang: ''' + langName + '''
:hardbreaks:
:sectnums:
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
:pdf-stylesdir: ../../lib
:pdf-style: default-theme.yml

'''

    tocandindex = '''

toc::[]

include::index.adoc[]

'''

    ## Set project name
    if (os.path.isfile('../../README.md')):
        t = open('../../README.md', 'r', encoding='utf-8_sig')
        text = t.readline()
        regex = r'^#{1}.+?$'
        pattern = re.compile(regex)
        r = pattern.match(text)
        result = r.group(0)
        pname = '= ' + str(result[2:])
    else:
        pwd = os.path.dirname(os.path.abspath(__file__))
        pwd = pwd.replace('\\', '/')
        r = pwd.split('/')
        result = r[-2]
        pname = '= ' + result

    ## Append preamble, project name, toc and index
    f = open('../../lib/toc_' + langName + '.adoc', 'a', encoding='utf-8_sig')
    f.write(str(preamble))
    f.write(str(pname))
    f.write(str(tocandindex))
    f.close()

    ## Append asciidoc files name in adoc folder
    fnameList = os.listdir('.')
    for file in fnameList:
        fname, ext = os.path.splitext(file)
        if ext == '.adoc' and not fname == 'index':
            f = open('../../lib/toc_' + langName + '.adoc', 'a', encoding='utf-8_sig')
            f.write(str('include::' + file + '[]\n\n<<<\n\n'))
            f.close()


if __name__ == '__main__':
    main()
