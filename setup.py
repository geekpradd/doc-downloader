from setuptools import setup

try:
    import pypandoc
    description=pypandoc.convert('readme.md','rst')
except:
    description=''
setup(name='DocDownloader',
      version="1.3.2",
      description='Downloads Documentation from ReadTheDocs in multiple formats',
      long_description=description,
      url='https://github.com/geekpradd/doc-downloader',
      author='Pradipta Bora',
      author_email='pradd@outlook.com',
      license='MIT',
      packages=['DocDownloader'],
      install_requires=[
          'beautifulsoup4',
          'requests'  ,'wget' ],
      scripts=['bin/docdownloader'],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
      ],
      zip_safe=False)
