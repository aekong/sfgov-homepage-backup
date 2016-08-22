import re
import os
import fnmatch

cwd = os.getcwd()
cssdir = './sfgov.org/sites/default/files/css_injector'
jsdir = './sfgov.org/sites/default/files/js_injector'

def fix_filenames(directory, regex):
  d = os.path.join(cwd, directory)
  for filename in os.listdir(d):
    pattern = re.compile(r'' + regex)
    newfilename = re.sub(pattern, '', filename)
    os.rename(d + '/' + filename, d + '/' + newfilename)

def fix_references():
  for dName, sdName, fList in os.walk(cwd + '/sfgov.org'):
    for filename in fList:
      if fnmatch.fnmatch(filename, '*.html'):

        fn = os.path.join(dName+'/'+filename)
        f = open(fn, 'r')
        str = f.read()
        f.close()
        str = re.sub(r'%3F.*?"', '"', str)
        f = open(fn, 'w')
        f.write(str)
        f.close

fix_filenames(cssdir, '\?.*\.css')
fix_filenames(jsdir, '\?.*')

fix_references()
  
