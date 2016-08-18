import re
import urllib
import os

cwd = os.getcwd()
print "cwd: %s" % cwd

def get_images_from_file(filename, location):
  f = open(filename, 'r')
  str = f.read()
  f.close
  regex = r'<img.*src="(.*)".*?\/>'
  matches = re.findall(regex, str)
  
  for match in matches:
    absoluteurl = re.sub('\.\.', 'http://sfgov.org', match)
    imagefilename = match[match.rfind('/'):]
    loc = os.path.join(cwd, location) + imagefilename
    print "download: " + absoluteurl + " to " + loc
    urllib.urlretrieve(absoluteurl, loc)


def get_images_from_css(directory, location):
  d = os.path.join(cwd, directory)
  imagepaths = []
  for filename in os.listdir(d):    
    f = open(d+'/'+filename, 'r')
    str = f.read()
    f.close
    regex = r'(http:\/\/sfgov.org\/.*Images.*\.(?:jpg|png|gif|jpeg))'
    matches = re.findall(regex, str)
    for match in matches:
      imagepaths.append(match)

  for imagepath in imagepaths:
    imagefilename = imagepath[imagepath.rfind('/'):]
    loc = os.path.join(cwd, location) + imagefilename
    print "download: " + imagepath + " to " + loc
    urllib.urlretrieve(imagepath, loc)



get_images_from_file('./sfgov.org/sites/default/files/Homepage/carousel.html', 'sfgov.org/sites/default/files/Homepage/Carousel')
get_images_from_file('./sfgov.org/sites/default/files/Homepage/slide.html', 'sfgov.org/sites/default/files/Homepage/Slide')

get_images_from_css('./sfgov.org/sites/default/files/css_injector', 'sfgov.org/sites/default/files/Images/Mainpages')