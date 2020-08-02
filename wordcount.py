
contents = "Betty Botter bought a bit of butter \n but the bit of butter was bitter so Betty Botter bought a bit of better butter \nto make the bit of bitter butter better"
total_words = contents.split()
unique = set(contents.split())
words_count = {}
for w in unique:
    words_count.update({w:total_words.count(w)})    

print(str(words_count))

