# -*- coding: utf-8 -*-
'''
Created on 21/08/2011

@author: robson
'''
from distutils.core import setup
import py2exe
import os

def arquivos(base):
    for i,_,k in os.walk("data/" + base):
        if i.find(".svn") == -1 and len(k) > 0:
            for f in k:
                yield os.path.join(i,f)
    
di = arquivos("images")
ds = arquivos("sound")

setup(windows=['ourgame.py'],
      name='ATAC-PY',
      version='1.0',
      description='ATAC-PY : A Free/Opensource space shooter in Python',
      author='Robson França',
      author_email='robsonsfranca@fmail.com',
      url='http://code.google.com/p/atac-py/',
      packages=['atacpy', 'data', 'engine'],
      data_files=[('data/images', di),
                  ('data/sound', ds)],
      options={'py2exe': {
        "optimize": 2,
        "bundle_files": 2, # This tells py2exe to bundle everything
      }})
