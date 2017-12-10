from hashlib import md5
import string
for i in string.uppercase:
    for j in string.uppercase:
        for k in string.uppercase:
            a='TASC'+i+'O3RJMV'+j+'WDJKX'+k+'ZM'
            b=a
            c=md5(a).hexdigest()
            if(c[0:4]=='e903'):
                print c.upper()