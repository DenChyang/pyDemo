# 二叉树

class Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            # 如果左节点为空，则添加
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            # 如果右节点为空，则添加
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    # 广度遍历
    def breadth_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self,node):
        # 先序遍历
        if node is Node:
            return
        print(node.elem)
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self,node):
        # 中序遍历
        if node is Node:
            return
        self.inorder(node.lchild)
        print(node.elem)
        self.inorder(node.rchild)

    def postorder(self,node):
        # 后序遍历
        if node is Node:
            return
        self.postorder(node.lchild)
        print(node.elem)
        self.postorder(node.rchild)

def main():
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()

if __name__ == '__main__':
    main()