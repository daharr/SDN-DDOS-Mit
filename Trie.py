class Trie:

	trie child[] 		#arry of pointers to children in lattice
	int depth 			# depthof the node
	boolean fringe 		# true iff subtrie < T_split
	vol_type volume 	# volume of traffic trapped at node
	vol_type subtotal	#total volume of traffic on all descendents
	vol_type miss_copy	# missed traffic - est by copy-all
	vol_type miss_split	#missed traffic -est by splitting