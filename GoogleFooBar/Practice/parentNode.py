# Python implementation to find the
# parent of the given node

import math

# Function to find the parent
# of the given node
def solution(H, Q):
    out=[]
    for converter in Q:
        out.append(findParent(H,converter))
    return out
        
def findParent(height, node):

	start = 1
	end = pow(2, height) - 1

	# Check whether the given node
	# is a root node.if it is then
	# return -1 because root
	# node has no parent
	if (end == node):
		return -1

	# Loop till we found
	# the given node
	while(node >= 1):

		end = end - 1

		# Find the middle node of the
		# tree because at every level
		# tree parent is divided
		# into two halves
		mid = start + (end - start)//2

		# if the node is found
		# return the parent
		# always the child nodes of every
		# node is node / 2 or (node-1)
		if(mid == node or end == node):
			return (end + 1)
		
		# if the node to be found is greater
		# than the mid search for left
		# subtree else search in right subtree
		elif (node < mid):
			end = mid

		else:
			start = mid



print(solution(5,[19,14,28]))