hawk2.0
=======

New Rewrite of HawkAPI

<h2>Linux Install:</h2>

You will need to install <a href="https://github.com/mikemaccana/python-docx">python-docx:</a>

    $sudo pip install python-docx

You will need to install <a href="https://xlsxwriter.readthedocs.org">Xlsxwriter</a>
  
    $sudo pip install XlsxWriter

You will need to install <a href="http://www.reportlab.com/">ReportLab</a>

    $sudo apt-get install python-reportlab 

You will need to install these dependencies:

    $sudo apt-get install libffi-dev libffi6 mongodb python-pymongo

You will need to install <a href="http://pygal.org/">PyGal</a> and lxml for graphics

    $sudo pip install pygal CairoSVG tinycss cssselect

Download or clone the repo.

    $sudo python setup.py install

<h2>Windows Install:</h2>

Install <ahref="https://www.python.org/downloads/windows/">Python2.7</a>
Make sure it is the 32bit version.  The 64bit version has issues with
adding registry settings.

Add Python to your path:

     C:\Python27\;C:\Python\Scripts\

Download the <a href="https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py">ez_setup.py</a> script.

      python ez_setup.py

Get Pip <a href="https://pip.pypa.io/en/latest/installing.html">get_pip.py</a>

      python get_pip.py

You will need to install <a href="https://github.com/mikemaccana/python-docx">python-docx:</a>
   
      pip install python-docx
  
You will need to install <a href="https://xlsxwriter.readthedocs.org">Xlsxwriter</a>
 
      pip install XlsxWriter
 
You will need to install <a href="http://www.reportlab.com/">ReportLab</a>

      pip install reportlab

You will need to install the pygtk pygobject and pycario.  Go to
<a>www.Lfd.uci.edu/~gohlke/pythonlibs/#pygtk</a> and get the libraries
and install them.

You will need to install <a href="http://pygal.org/">PyGal</a> and lxml for graphics
  
      pip install pygal CairoSVG tinycss cssselect      

You will also need the request module

      pip install requests

Download or clone the repo

      python setup.py install
