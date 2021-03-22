import fileinput

def getKey(val, d):
  for key, value in d.items():
    if val == value:
      return key
  return "key doesn't exist"

lines = []
for line in fileinput.input():
    lines.append(line)
opt = lines[0].replace('\n','')
msg = lines[1].replace(' ', '').replace('\n', '')

k = {
  (0,0):'E', (1,0):'P', (2,0):'F', (3,0):'L', (4,0):'U',
  (0,1):'N', (1,1):'T', (2,1):'G', (3,1):'M', (4,1):'V',
  (0,2):'C', (1,2):'A', (2,2):'H', (3,2):'O', (4,2):'W',
  (0,3):'R', (1,3):'B', (2,3):'I', (3,3):'Q', (4,3):'X',
  (0,4):'Y', (1,4):'D', (2,4):'K', (3,4):'S', (4,4):'Z'
}

idx = []
for x in msg:
  key = getKey(x,k)
  idx.append(key[0])
  idx.append(key[1])

l = int(len(idx)/2)
if opt == 'ENCRYPT':
  idxa = []
  idxb = []
  for i in range (0, l):
    idxa.append(idx[i*2])
    idxb.append(idx[i*2+1])
  neoidx = idxa
  neoidx = neoidx + idxb

elif opt == 'DECRYPT':
  neoidx = []
  for i in range(0, l):
    neoidx.append(idx[i])
    neoidx.append(idx[i+l])

else:
  print('Not a valid option')

res = ''
for i in range(0, l):
  res = res + k.get((neoidx[i*2],neoidx[(i*2+1)]))
print(res)






