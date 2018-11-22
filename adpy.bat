@echo off
chcp 65001 > nul
REM ADPY - Convert Asciidoc to html via Asciidoctor and Python.
REM Require Ruby, Asciidoctor-1.5.6.1(Available only this version, strictly, Asciidoctor-pdf, Python3.X, Beautifulsoup4, and lxml.
REM MIT License
REM Copyright (c 2018 Human Science Co., Ltd
REM Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software", to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, htmlribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

REM The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

REM THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

pushd %~p0

REM Variables
set FNAME=%0
set FTYPE=%1
set LANGS=%2
set MAN="Please visit our GitHub repository. thanks! https://github.com/human-science/adpy"

REM Process flow
REM initialize => prepare => main_%FTYPE% => after


:initialize
if /i {%FTYPE%} == {version} (
echo V 1.0.0
pause
exit /b
)
if /i {%FTYPE%} == {man} (
echo %MAN%
pause
exit /b
)
if /i {%FTYPE%} == {pdf} (
set FTYPE=%FTYPE%
) else (
set FTYPE=html
)
if /i {%LANGS%} == {ja} (
set LANGS=%LANGS%
) else (
set LANGS=en
)
goto :prepare %FTYPE% %LANGS%


:prepare
if exist %FTYPE%\%LANGS% rd /s /q %FTYPE%\%LANGS%
mkdir %FTYPE%\%LANGS%
if exist lib\toc_%LANGS%.adoc del lib\toc_%LANGS%.adoc
copy adoc\%LANGS%\*.adoc %FTYPE%\%LANGS% > nul
xcopy adoc\%LANGS%\images %FTYPE%\%LANGS%\images /D /E /I /Q /Y > nul

if /i {%FTYPE%} == {html} (
goto :prepare_html %FTYPE% %LANGS%
)
if /i {%FTYPE%} == {pdf} (
goto :main_pdf %FTYPE% %LANGS%
)

:prepare_html
if not exist html\css (
mkdir html\css
)
if not exist html\js (
mkdir html\js
)
goto :main_html %FTYPE% %LANGS%

:main_pdf
pushd .
cd %FTYPE%\%LANGS%

python ../../lib/insertPreamble.py %LANGS%
python ../../lib/generateToc.py %LANGS%
copy ..\..\lib\toc_%LANGS%.adoc > nul

call asciidoctor -b pdf -r asciidoctor-pdf toc_%LANGS%.adoc

popd
goto :after %FTYPE% %LANGS%


:main_html
pushd .
cd %FTYPE%\%LANGS%

python ../../lib/insertPreamble.py %LANGS%
python ../../lib/generateToc.py %LANGS%

for %%i in (*.adoc) do call asciidoctor -d book -a stylesdir=../css -b html5 %%i

python ../../lib/buildNavmenu.py %LANGS%

for %%i in (*.html) do call python ../../lib/convertHtml.py %%i %LANGS%

popd
goto :after %FTYPE% %LANGS%


:after
if /i {%FTYPE%} == {pdf} (
rd /s /q %FTYPE%\%LANGS%\images
)
del %FTYPE%\%LANGS%\*.adoc

echo Done.
pause
exit /b
