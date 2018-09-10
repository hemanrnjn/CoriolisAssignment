import urllib.request as urlLib


response = urlLib.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt')
html = response.read()
print(html)