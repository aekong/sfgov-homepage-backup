import re
import os
import fnmatch

cwd = os.getcwd()
cssdir = './sfgov.org/sites/default/files/css_injector'
jsdir = './sfgov.org/sites/default/files/js_injector'
fontdir = './sfgov.org/sites/all/themes/sf/fonts/fa'

def fix_filenames(directory, regex, replace=''):
  d = os.path.join(cwd, directory)
  for filename in os.listdir(d):
    pattern = re.compile(r'' + regex)
    newfilename = re.sub(pattern, replace, filename)
    os.rename(d + '/' + filename, d + '/' + newfilename)

def fix_references():
  for dName, sdName, fList in os.walk(cwd + '/sfgov.org'):
    for filename in fList:
      if fnmatch.fnmatch(filename, '*.html') or fnmatch.fnmatch(filename, '*.css') or fnmatch.fnmatch(filename, '*json.js'):
        fn = os.path.join(dName+'/'+filename)
        f = open(fn, 'r')
        str = f.read()
        f.close()
        str = re.sub(r'%3F.*\.css', '', str) # fixes css references with ? in the path
        str = re.sub(r'\.js%3F.*?"', '.js"', str) # fixes js references with ? in the path
        str = re.sub(r'%3Fv=.*?\)', ')', str) # fixes font references with ? in the path
        str = re.sub(r'http:\\/\\/sfgov.org\\/sites\\/default\\/files\\/Images', 'sites/default/files/Images', str) # fixes image path references in json files
        str = re.sub(r'news%3F', 'news-', str) # fixes references for news pages
        f = open(fn, 'w')
        f.write(str)
        f.close
      if fnmatch.fnmatch(filename, 'js_injector*.js'): # fixes the js references
        fn = os.path.join(dName + '/' + filename)
        f = open(fn, 'r')
        str = f.read()
        f.close()
        str = re.sub(r'_json', '_json.js', str)
        f = open(fn, 'w')
        f.write(str)
        f.close



fix_filenames(cssdir, '\?.*\.css')
fix_filenames(jsdir, '\?.*')
fix_filenames(fontdir, '\?.*')
fix_filenames('./sfgov.org', 'news\?', 'news-')

fix_references()
  
