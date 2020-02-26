import os

from PIL import Image

for f in os.listdir('.'):
    print(f)
    if '.gif' in f :
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        print(fext)
        i = i.convert('RGB')
        i.save('{}.pdf'.format(fn),resolution=19.0 ,quality=60,optimize=True)
print('Terminou...')
'''
import requests
session = requests.Session()
r = session.get('http://www.superflix.net')
print(session.cookies.get_dict())
print(r.cookies._cookies)
'''