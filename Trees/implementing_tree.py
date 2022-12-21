class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right = None
    ans=0
    # valin=0
    def add_child(self,data):
        # if self.data is None:
        #     self.data = BinarySearchTreeNode(data)
        if data < self.data:
            if self.left is None:
                self.left = BinarySearchTreeNode(data)
            else:
                return self.left.add_child(data)
        elif data > self.data:
            if self.right is None:
                self.right = BinarySearchTreeNode(data)
            else:

                return self.right.add_child(data)

    # def inorder(self):
    #     result = []
    #     if self is not None:
    #         result.extend(self.left.inorder())
    #         result.append(self.data)
    #         result.extend(self.right.inorder())
    #     return result

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data)
        if self.right is not None:
            self.right.inorder()

    def preorder(self):
        print(self.data)
        if self.left is not None:
            self.left.preorder()

        if self.right is not None:
            self.right.preorder()

    def minimum(self):
        if self.left is None:
            return self.data
        return self.left.minimum()

    def maximum(self):
        if self.right is None:
            return self.data
        return self.right.maximum()

    def sum(self):

        if(self.left is None  or self.right is None):
            return self.data
        ans += self.left.sum()
        # ans=ans+self.data
        ans += self.right.sum()

        # ans=ans+ans1
        return ans



    def search(self,val):

        if(self.data==val):
            return True
        if (self.data > val):
            if self.left:
                return self.left.search(val)
            else:

                return False
        if (self.data < val):
            if self.right:
                return self.right.search(val)
            else:
                return False
def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root



numbers=[17,4,1,20,9,23,18,34]
number_tree=build_tree(numbers)
# print(number_tree.inorder())
# print(number_tree.preorder())
# print(number_tree.search(20))
# print(number_tree.minimum())
# print(number_tree.maximum())
print(number_tree.sum(0))
print(sum_bst())