#coding=utf-8

def decrypt(ctext):
	for i in xrange(0,26):
		new=[]
		print i
		for x in xrange(0,len(ctext)):
			asc=ord(ctext[x])+i
			#避免超出上限
			if asc >ord('z'):
				asc = (asc - ord('z')-1)+ord('a')
			chars = chr(asc)
			new.append(chars)
		print "".join(new)

ctxt = 'ComeChina'
ctxt= ctxt.lower()
decrypt(ctxt)