import fileinput

numbers = []
res = 0
for line in fileinput.input():
  try:
    numbers.append(int(line))
  except ValueError:
    numbers.append(float(line))

for i in numbers:
  res = i + res

print(res)
