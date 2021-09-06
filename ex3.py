st = input()
p = st.split(' ')
q = []
r = 0
for i in p:
	conv = i.strip('][').split(',')
	q.append(conv)



for i in range(0, len(q[1])):
	r += int(q[0][i]) * int(q[1][i])

print(r)