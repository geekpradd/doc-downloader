__author__ = 'Pradipta'
__version__= "1.2.5"
from bs4 import BeautifulSoup
import requests, wget, os, zipfile, sys, argparse
try:
    import urllib2
    python=2
except ImportError:
    python = 3
class DocDownloader:
    def __init__(self,url,format):
        if 'http' in url:
            self.url=self.getVariable(url)
        else:
            self.url=url
        self.format=format

    def download(self):

        self.downloadFile()
    def downloadFile(self):
        if self.format.lower()=="html":
            self.downloadHTML()
        elif self.format.lower()=="pdf":
            self.downloadPDF()
        elif  self.format.lower()=="epub":
            self.downloadEPUB()
        else:
            print ("Unknown Format {0}".format(self.format))
            sys.exit(0)
    def getVariable(self,url):
        html=requests.get(url).text
        soup=BeautifulSoup(html)
        for term in soup.find_all("script"):
            if "READTHEDOCS_DATA" in str(term.text):
                script=term
                break
            else:
                continue
        return find_between(find_between(script.text,"READTHEDOCS_DATA = {","}"),"project: ",",").replace('"','')
    def downloadHTML(self):
        url="https://media.readthedocs.org/htmlzip/{0}/latest/{0}.zip".format(self.url)
        location="{0}/{1}.zip".format(os.getcwd(),self.url)
        f=wget.download(url,out=os.getcwd())
        print ("\n{0} has been downloaded.. Extracting zip".format(self.url))
        extractZIP(location,self.url)
    def downloadEPUB(self):
        url="https://media.readthedocs.org/epub/{0}/latest/{0}.epub".format(self.url)
        f=wget.download(url,out=os.getcwd())
        print ("\n{0} has been downloaded".format(f))
    def downloadPDF(self):
        url="https://media.readthedocs.org/pdf/{0}/latest/{0}.pdf".format(self.url)
        f=wget.download(url,out=os.getcwd())
        print ("\n{0} has been downloaded".format(f))

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


def extractZIP(arg,name):

    with zipfile.ZipFile(arg,'r') as z:
        z.extractall(os.getcwd())
    print ("Extracting done... Creating bat file for server")
    createBAT("{0}/{1}-latest".format(os.getcwd(),name))

def createBAT(folder):
    with open("{0}/server.bat".format(folder),'w') as file:
        if python==3:
            file.write('@ECHO OFF \n cd "{0}"\n python -m http.server 5000'.format(folder))
        else:
            file.write('@ECHO OFF \n cd "{0}"\n python -m SimpleHttpServer 5000'.format(folder))
    print ("BAT Created")


def main():
    print ("Consult Documentation for usage or use the script.")
if __name__=='__main__':
    main()