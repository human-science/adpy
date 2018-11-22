#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Add navigation menu, additional header, ids nad classes.
from bs4 import BeautifulSoup
import lxml
import sys
import re
import os


def main():
    ## Variables
    args = sys.argv
    sfile = args[1]
    langName = args[2]

    ## Set project name
    if (os.path.isfile('../../README.md')):
        t = open('../../README.md', 'r', encoding='utf_8_sig')
        text = t.readline()
        regex = r'^#{1}.+?$'
        pattern = re.compile(regex)
        r = pattern.match(text)
        result = r.group(0)
        pname = result[2:]
    else:
        pwd = os.path.dirname(os.path.abspath(__file__))
        pwd = pwd.replace('\\', '/')
        r = pwd.split('/')
        result = r[-2]
        pname = result

    aheadContent = '<div id="global-header"><a class="modelnumber" href="./index.html">' + pname + '</a><a class="inline-block" href="https://www.science.co.jp/"><figure><img alt="logo" src="images/logo.png" style="width:180px;" /></figure></a></div>'

    f = open(sfile, 'r', encoding='utf-8_sig')
    text = f.read()
    f.close()
    soup = BeautifulSoup(text, 'lxml')

    ## Asciidoctor native elements
    contentOrgDiv = soup.find('div', attrs={'id': 'content'})
    headerOrgDiv = soup.find('div', attrs={'id': 'header'})
    footerOrgDiv = soup.find('div', attrs={'id': 'footer'})
    bodyElem = soup.body

    ## Navigation menu
    # Open and read external file.
    mfile = '../../lib/menucontent_' + langName + '.html'
    m = open(mfile, 'r', encoding='utf-8_sig')
    menuContent = m.read()
    m.close()
    # Insert navigation menu element.
    headerElem = soup.new_tag('header', role='banner')
    headerElem.append(menuContent)
    contentOrgDiv.insert_before(headerElem)
    drawerContent = soup.new_tag('div')
    drawerContent['class'] = 'drawer-contents'
    drawerContainer = soup.new_tag('main', id='content', role='main')
    drawerContainer['class'] = 'drawer-container t-gutter'
    # Wrap and Clean up nodes.
    contentOrgDiv.wrap(drawerContent)
    contentOrgDiv.wrap(drawerContainer)
    contentOrgDiv['id'] = 'contentOrg'
    bodyElem['class'] = 'drawer drawer--left drawer--sidebar'
    for sect1Elem in soup.select('.sect1'):
        sect1Elem['class'] = 'sect1 contentarea'

    ## Additional header
    if headerOrgDiv == None:
        headerElem.insert_before(aheadContent)
    else:
        headerOrgDiv = soup.div.extract()
        contentOrgDiv.insert_before(headerOrgDiv)
        bodyElem.insert(1, aheadContent)

    ## Footer
    copyrightDiv = soup.find('div', attrs={'id': 'copyright'})
    if footerOrgDiv == None:
        soup.main.insert_after(copyrightDiv)
        divFooter = soup.new_tag('div', id='footer')
        copyrightDiv.wrap(divFooter)
    else:
        soup.main.insert_after(footerOrgDiv)
        footerOrgDiv.append(copyrightDiv)

    ## Prettify
    text = soup.prettify()
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&amp;', '&')

    f = open(sfile, 'w', encoding='utf-8_sig')
    f.write(text)
    f.close()


if __name__ == '__main__':
    main()
