from collections import Counter
FREQ={"A":.08167,"B":.01492,"C":.02782,"D":.04253,"E":.12702,"F":.02228,"G":.02015,"H":.06094,"I":.06966,"J":.00153,"K":.00772,"L":.04025,"M":.02406,"N":.06749,"O":.07507,"P":.01929,"Q":.00095,"R":.05987,"S":.06327,"T":.09056,"U":.02758,"V":.00978,"W":.02360,"X":.00150,"Y":.01974,"Z":.00074}
BIG={"TH","HE","IN","ER","AN","RE","ON","AT","EN","ND","TI","ES","OR","TE","OF","ED","IS","IT","AL","AR"};TRI={"THE","AND","ING","HER","ERE","ENT","THA","NTH","WAS","FOR","SHE","ION","VER","EST","ERS"};WORDS={"THE","AND","THIS","THAT","WITH","FROM","HAVE","WERE","YOU","YOUR","ARE","NOT","FOR","IS","TO","IN","OF","ON"}
def clean(t):return ''.join(c.upper() for c in t if c.isalpha())
def frequency(t):
 c=Counter(clean(t));return {chr(65+i):c.get(chr(65+i),0) for i in range(26)}
def ioc(t):
 s=clean(t);n=len(s)
 if n<2:return 0.0
 return sum(v*(v-1) for v in Counter(s).values())/(n*(n-1))
def chi(t):
 s=clean(t);n=len(s)
 if not n:return float('inf')
 return sum((s.count(k)-n*v)**2/(n*v) for k,v in FREQ.items())
def ngram(t):
 s=clean(t);score=0
 for i in range(len(s)-1):score+=s[i:i+2] in BIG
 for i in range(len(s)-2):score+=2*(s[i:i+3] in TRI)
 for w in WORDS:score+=3*(w in s)
 return float(score)
def key_lengths(t,m=20):
 s=clean(t);out=[]
 for k in range(1,min(m,len(s))+1):
  vals=[ioc(s[i::k]) for i in range(k) if s[i::k]];out.append({'key_length':k,'ioc':sum(vals)/len(vals) if vals else 0})
 return sorted(out,key=lambda x:x['ioc'],reverse=True)
def kasiski(t):
 s=clean(t);counts=Counter()
 for n in range(3,6):
  pos={}
  for i in range(len(s)-n+1):pos.setdefault(s[i:i+n],[]).append(i)
  for p in pos.values():
   for a,b in zip(p,p[1:]):
    d=b-a
    for k in range(2,min(20,d)+1):
     if d%k==0:counts[k]+=1
 return [{'length':k,'count':v} for k,v in counts.most_common()]
def caesar_break(t):
 from ciphers.substitution.caesar import CaesarCipher
 out=[];c=CaesarCipher()
 for k in range(26):
  p=c.decrypt(t,k);out.append({'key':k,'plaintext':p,'chi_square':chi(p),'ngram_score':ngram(p)})
 return sorted(out,key=lambda x:(-x['ngram_score'],x['chi_square']))[:10]
def affine_break(t):
 from ciphers.substitution.affine import AffineCipher
 out=[]
 for a in AffineCipher.VALID_A_VALUES:
  for b in range(26):
   try:
    p=AffineCipher().decrypt(t,(a,b));out.append({'key':(a,b),'plaintext':p,'chi_square':chi(p),'ngram_score':ngram(p)})
   except:pass
 return sorted(out,key=lambda x:(-x['ngram_score'],x['chi_square']))[:10]
def vig_key(t,n,mode='vigenere'):
 s=clean(t);key=''
 for i in range(n):
  col=s[i::n];scores=[]
  for k in range(26):
   p=''.join(chr((k-(ord(c)-65))%26+65) if mode=='beaufort' else chr(((ord(c)-65-k)%26)+65) for c in col);scores.append((chi(p),k))
  key+=chr(min(scores)[1]+65)
 return key
def vig_dec(t,key,mode='vigenere'):
 out=[];i=0
 for c in t:
  if c.isalpha():
   x=ord(c.upper())-65;k=ord(key[i%len(key)])-65;p=(k-x)%26 if mode=='beaufort' else (x-k)%26;z=chr(p+65);out.append(z.lower() if c.islower() else z);i+=1
  else:out.append(c)
 return ''.join(out)
def poly_break(t,mode='vigenere'):
 lengths=key_lengths(t,12);cand=[]
 for x in lengths[:10]:
  k=vig_key(t,x['key_length'],mode);p=vig_dec(t,k,mode);cand.append({'key':k,'key_length':x['key_length'],'plaintext':p,'score':ngram(p)})
 cand.sort(key=lambda x:x['score'],reverse=True)
 return {'key_length_candidates':{'ioc_results':lengths,'kasiski':{'key_length_candidates':kasiski(t)},'friedman':{'estimated_key_length':None}},'candidates':cand[:10],'best':cand[0] if cand else None}
def analyze_cipher(name,t):
 s=clean(t);r={'analysis':{'length':len(s),'frequency':frequency(t),'ioc':ioc(t),'chi_square':chi(t),'ngram_score':ngram(t)}}
 if name=='Caesar':r['break']={'candidates':caesar_break(t),'best':caesar_break(t)[0]}
 elif name=='Atbash':
  from ciphers.substitution.atbash import AtbashCipher
  p=AtbashCipher().decrypt(t);r['break']={'plaintext':p,'best':{'plaintext':p}}
 elif name=='Affine':r['break']={'candidates':affine_break(t),'best':affine_break(t)[0]}
 elif name in ('Vigenère','Beaufort','Variant Beaufort'):r.update(poly_break(t,'beaufort' if name=='Beaufort' else 'vigenere'))
 elif name=='Monoalphabetic Substitution':r['analysis']['ranking']=sorted(frequency(t).items(),key=lambda x:x[1],reverse=True)
 elif name=='Homophonic Substitution':r['analysis']['frequencies']=dict(Counter(t.split()))
 return r
