def Update(key, value):
n = root
while true:
	if n.fringe:
		if n.volume + value < T_split:
			n.volume = n.volume + value
			return n.depth - 1
		else
			n.fringe = false
			if n.depth == W:
				n.subtotal = value
				return n.depth
	else if n.depth == W:
		n.subtotal = n.subtotal + value
		return n.depth
	index = get_Nth_bit(key, n.depth + 1)
	c = get_child(n,index)
	if c == NULL:
		c = create_child(n, index)
	n = c
