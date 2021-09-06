n = int(input())
counter = 0
l = []
for i in range(n,0,-1):
	for k in range(1, i+1):
		if i % k == 0:
			counter += 1
	if counter > 2:
		counter = 0
	if counter == 2:
		l.append(i)
		counter = 0

l.sort()
print(l)