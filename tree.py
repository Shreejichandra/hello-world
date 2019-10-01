#check tree mirror image
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    
def isSymmetric(root):
    return isMirror(root,root)

def isMirror(root1,root2):
    if root1 is None and root2 is None:
        return True
    if(root1 is not None and root2 is not None):
        if root1.key==root2.key:
            return(isMirror(root1.left,root2.right) and 
                   isMirror(root1.right,root2.left))
    return False
"""test 1
root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right.left = Node(4) 
root.right.right = Node(3)"""
#test2:
root=Node(1)
root.left=Node(2)
root.right=Node(2)
root.left.right=Node(3)
root.right.right=Node(3)

print("yes mirror" if isSymmetric(root) == True else "no mirror")


#foldable tree
class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None
def isfoldable(root):
    if root is None:
        return True
    return isfoldablesubtree(root.left,root.right)
def isfoldablesubtree(root1,root2):
    if (root1 is not None and root2 is not None):
        return True
    if(root1 is None or root2 is None):
        return False
    return isfoldablesubtree(root1.left,root2.right) and isfoldablesubtree(root1.right,root2.left)
    
"""test case 1
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(5)
root.right.left=Node(4)"""
#test case 2
root=Node(10)
root.left=Node(7)
root.right=Node(15)
root.left.right=Node(6)
root.left.left=Node(5)
root.right.left=Node(11)
print("yes" if isfoldable(root)==True else "No")
"""if(isfoldable(root)==True):
    print("yes foldable")
else:
    print("Not foldable")"""
    
    
#Evaluate expression tree
class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
def exptree(root):
    if root is None:
        return 0
    if (root.left is None and root.right is None):
        return int(root.data)
    left_tree=exptree(root.left)
    right_tree=exptree(root.right)
    if root.data=='+':
        return left_tree+right_tree
    if root.data=='-':
        return left_tree-right_tree
    if root.data=='*':
        return left_tree*right_tree
    if root.data=='/':
        return left_tree/right_tree
"""root=Node('+')
root.left=Node('*')
root.right=Node('-')
root.left.left=Node('5')
root.left.right=Node('4')
root.right.left=Node('100')
root.right.right=Node('20')
print("Answer:", exptree(root))"""

root = Node('+') 
root.left = Node('*') 
root.left.left = Node('5') 
root.left.right = Node('4') 
root.right = Node('-') 
root.right.left = Node('100') 
root.right.right = Node('/') 
root.right.right.left = Node('20') 
root.right.right.right = Node('2') 
print (exptree(root) )


#left view of a tree
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def leftview(root):
       q=queue.Queue()
       q.put(root)
       while q.qsize():
           currlevelsize=q.qsize()
        for i in range(currlevelsize):
            curr_node=q.get()
            if curr_node.left:
                q.put(curr_node.left)
            if curr_node.right:
                q.put(curr_node.right)
            if i==0:
                print(curr_node.data,end=" ")
                
                
                
#binary tree search
def binary_search(array,key):
    start=0
    end=len(array)
    while start<end:
        mid=(start+end)//2
        if array[mid]>key:
            end=mid
        elif array[mid]<key:
            start=mid+1
        else:
            return mid
    return -1
n=int(input("enter number of elements"))
array=list()
print("enter array elements")
for i in range(n):
    array_num=input("number:")
    array.append(int(array_num))
array.sort()
print("the array is:",array)
key=int(input("enter the elemnt to search: "))
index=binary_search(array,key)
if index<0:
    print("{} not found" .format(key))
else:
    print("{} found at position {}" .format(key,index))



#convert 1d array to 2d array

from itertools import islice
def convert(listt,varlist):
    index=0
    for i in varlist:
        yield listt[index:index+i]
        index=index+i
listt=[1,2,3,4,88,9]
varlist=[1,2,4]
print(list(convert(listt,varlist)))


from itertools import islice 
  
def convert(lst, var_lst): 
    idx = 0
    for var_len in var_lst: 
        yield lst[idx : idx + var_len] 
        idx += var_len 
      
# Driver code 
lst = [1, 2, 3, 4, 5, 6,00,89,67] 
var_lst = [1, 2, 3,2,2] 
res=convert(lst,var_lst)

print(tuple(res)) 























    
