import json

pertot = [0,0]
entry = 0

class Trie:

    def __init__(self, maxdepth, maxchild):
        self.maxdepth = maxdepth
        self.maxchild = maxchild
        self.child = [None] * self.maxchild	# arry of pointers to children in tree
        self.depth = 0	# depth of the node
        self.fringe = True	# true iff subtrie < T_split
        self.volume = 0	# volume of traffic trapped at node
        self.pastent = []
        self.pastmem = []
        self.pastval = []

H = [ [None]*13 for i in range(2) ]
T_split = 20
portbyttrie = Trie(1,10)
destbyttrie = Trie(12,16)
portpacktrie = Trie(1,10)
destpacktrie = Trie(12,16)

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

def match_bit(mem, dep, maxd):
    if dep >= len(mem):
        print str(maxd) + " " + str(dep) + " " + mem
    return mem[dep]

def create_children(n):
    #create a new trie
    for i in range(0,n.maxchild):
        n.child[i] = Trie(n.maxdepth, n.maxchild)
        n.child[i].fringe = True
        n.child[i].volume = 0
        n.child[i].depth = n.depth + 1
        #fill the trie with the flows that made up it's volume
        for j in range(0, len(n.pastmem) - 1):
            if i == int(match_bit(n.pastmem[j],n.child[i].depth-1, n.maxdepth),16) and n.pastent[j] not in n.child[i].pastent:
                n.child[i].volume = n.child[i].volume + n.pastval[j]
                n.child[i].pastent.append(n.pastent[j])
                n.child[i].pastmem.append(n.pastmem[j])
                n.child[i].pastval.append(n.pastval[j])

def Update(trieroot, key, value, ent, totind):
    #return the depth of the node
    n = trieroot
    while 1==1:
        if ent not in n.pastent:
            n.pastent.append(ent)
            n.pastmem.append(key)
            n.pastval.append(value)
        if n.fringe:
            if (n.volume + value / ( pertot[totind] * 1.0 )) * 100 < T_split:
                n.volume = n.volume + value
                return n.depth - 1
            else:
                n.fringe = False
                if n.depth == n.maxdepth:
                    n.volume = value + n.volume
                    return n.depth
        else:
            if n.depth == n.maxdepth:
                n.volume = n.volume + value
                return n.depth
        newdep = n.depth + 1
        index = get_Nth_bit(key, newdep)
        c = get_child(n,int(index, 16)) ##takes a single character and puts it as an int so dec maps to dec and hex maps to hex
        if c == None:
            create_children(n)
            c = get_child(n,int(index, 16))
        n = c
        n.volume = n.volume + value

def Update_CP(portkey,edestkey, bytvalue, pacvalue):
    #update function for each dimension
    global pertot
    global entry
    entry = entry + 1
    pertot[0] = pertot[0] + bytvalue
    pertot[1] = pertot[1] + pacvalue
    portkey = str(portkey)
    edestkey = edestkey.translate(None, ':')
    len1 = Update(portbyttrie, portkey, bytvalue, entry, 0)
    len2 = Update(destbyttrie, edestkey, bytvalue, entry, 0)
    len3 = Update(portpacktrie, portkey, pacvalue, entry, 1)
    len4 = Update(destpacktrie, edestkey, pacvalue, entry, 1)

def HHHdet(trieroot, totind, f):
    n = trieroot
    hhhsum = 0
    if n.depth != n.maxdepth and get_child(n,0) != None:
        for i in range(0,len(n.child)):
            hhhsum = hhhsum + HHHdet(get_child(n, i), totind, f)
        val = (n.volume / ( pertot[totind] * 1.0 )) * 100
        if val > 10 and val - hhhsum > 10:
            json.dump(entry, f)
            f.write(',')
            json.dump(n.volume, f)
            f.write(',')
            json.dump(n.pastmem[0][0:n.depth+1], f)
            f.write(',')
            json.dump(len(n.pastmem), f)
            f.write('\n\n')
            hhhsum = hhhsum + val
        return hhhsum
    val = (n.volume / ( pertot[totind] * 1.0 )) * 100
    if val > 10:
        json.dump(entry, f)
        f.write(',')
        json.dump(n.volume, f)
        f.write(',')
        json.dump(n.pastmem[0][0:n.depth+1], f)
        f.write(',')
        json.dump(len(n.pastmem), f)
        f.write('\n\n')
        hhhsum = hhhsum + val
    return hhhsum

def checkHHH():
    if pertot[0] != 0:
        f = open('HHH3filepb.txt', 'a')
        HHHdet(portbyttrie, 0, f)
        f.close()
        f = open('HHH3filedb.txt', 'a')
        HHHdet(destbyttrie, 0, f)
        f.close()
        f = open('HHH3filepp.txt', 'a')
        HHHdet(portpacktrie, 1, f)
        f.close()
        f = open('HHH3filedp.txt', 'a')
        HHHdet(destpacktrie, 1, f)
        f.close()
