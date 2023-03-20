p=list(range(2,10ß0))
i = 0
while(i < len(p)):
	for q in p[i+1:]:
		if q%p[i] == 0:
			p.remove(q)
		i=i+1
print(p)
