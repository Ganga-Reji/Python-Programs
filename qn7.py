text="the quick brown fox jump over the lazy dog"
abc=dict()
text_words=text.split(" ")
for i in text_words:
	if i in abc:
		abc[i]+=1
	else:
		abc[i]=1
print(abc)

