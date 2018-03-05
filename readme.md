#DocDownloader - Download Docs from ReadTheDocs

[![License](https://img.shields.io/pypi/l/DocDownloader.svg)](https://pypi.python.org/pypi/DocDownloader/)
[![Development Status](https://img.shields.io/pypi/status/DocDownloader.svg)](https://pypi.python.org/pypi/DocDownloader/)

DocDownloader is a python 2/3 module/utility to download Documenation hosted on ReadTheDocs in HTML, PDF and EPUB Formats

It can be used from the terminal or by using the API.

##Installation

Installing is simple,  just enter  this command:

```
pip install DocDownloader
```

You need to have pip installed to run this command

##Usage

Just run the following command:

```
docdownloader [-f format] [-d directory] url/package name
```

For example,

```
docdownloader -f HTML flask
```

or 

```
docdownloader -f epub http://scrapy.readthedocs.org/en/latest/
```

##API Usage

You can use the module from python also. Example code:

```python
from DocDownloader import DocDownloader
DocDwn=DocDownloader('flask','pdf')
DocDwn.download()
```

##Dependencies

1. requests
2. BeautifulSoup4
3. wget (the python module)

##Features

1. Download docs in HTML, EPUB and PDF Formats
2. Automatic Server setup using http.server/SimpleHttpServer by clicking on a .bat file

##Note for Linux and Mac OSX Users

The Automatic server setup is currently for Windows only. It'l be ported over soon (Once I learn some shell commands)

##About

Created By Pradipta aka geekpradd. 

