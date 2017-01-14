class Trie:

    def __init__(self, maxdepth, maxchild):
        self.maxdepth = maxdepth
        self.maxchild = maxchild
        self.child = [None] * self.maxchild	# arry of pointers to children in tree
    depth = 0	# depth of the node
    fringe = True	# true iff subtrie < T_split
    volume = 0	# volume of traffic trapped at node
    subtotal = 0	# total volume of traffic on all descendents
    #miss_copy	# missed traffic - est by copy-all
    #miss_split	# missed traffic -est by splitting

H = [ [None]*13 for i in range(2) ]
T_split = 20
trie1 = Trie(1,10)
trie2 = Trie(12,10)

def get_Nth_bit(key, depth):
    #get the nth bit in the key
    return key[depth-1]

def prefix(key, leng):
    #return the matching prefix
    return key[0:leng]

def get_child(n, index):
    #get the specified child
    return n.child[index]

def printTrie(n, ind):
    print '   ' * n.depth + ind
    for i, ch in enumerate(n.child):
        printTrie(ch, i)

def create_child(n, index):
    #create a new trie
    n.child[index] = Trie(n.maxdepth, n.maxchild)
    n.child[index].fringe = True
    n.child[index].volume = 0
    n.child[index].subtotal = 0
    n.child[index].depth = n.depth + 1
    return n.child[index]

def Update(trieroot, key, value):
    #return the depth of the node
    n = trieroot
    while 1==1:
        if n.fringe:
            if n.volume + value < T_split:
                n.volume = n.volume + value
                return n.depth - 1
            else:
                n.fringe = False
                if n.depth == n.maxdepth:
                    n.subtotal = value
                    return n.depth
        else:
            if n.depth == n.maxdepth:
                n.subtotal = n.subtotal + value
                return n.depth
        newdep = n.depth + 1
        index = get_Nth_bit(key, newdep)
        c = get_child(n,int(index))
        if c == None:
            c = create_child(n,int(index))
        n = c

def Update_CP(key1,key2, value):
    #update function for each dimension
    len1 = Update(trie1, key1, value)
    len2 = Update(trie2, key2, value)
    if len1 >= 0 and len2 >= 0:
        p1 = prefix(key1, len1)
        p2 = prefix(key2, len2)
        H[len1][len2] = [p1,p2,str(value)]
