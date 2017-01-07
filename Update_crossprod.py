def Update_CP(key1,key2,key3):
 lis1 = Update(trie1, key1, value)
 lis2 = Update(trie2, key2, value)
 if lis1 >= 0 && l2 >= 0:
	p1 = prefix(key1, lis1)
	p2 = prefix(key2, lis2)
	H[lis1][lis2].update(p1,p2,value)
