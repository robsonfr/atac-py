# -*- coding: utf-8 -*-
'''
Created on 21/08/2011

@author: robson
'''
from distutils.core import setup
from cx_Freeze import setup, Executable
import os, sys

def arquivos(base):
    for i,_,k in os.walk("data/" + base):
        if i.find(".svn") == -1 and len(k) > 0:
            for f in k:
                yield os.path.join(i,f)
    
di = arquivos("images")
ds = arquivos("sound")

opcoes = { 'packages' : ['os','pygame','random','sys']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(windows=['ourgame.py'],
      name='ATAC-PY',
      version='1.0',
      description='ATAC-PY : A Free/Opensource space shooter in Python',
      author='Robson França',
      author_email='robsonsfranca@gmail.com',
      url='http://code.google.com/p/atac-py/',
      packages=['atacpy', 'data', 'engine'],
      data_files=[('data/images', di),
                  ('data/sound', ds)],
      options={'build_exe': opcoes},
      executables = [Executable("ourgame.py", base=base)]
)
