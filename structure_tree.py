# root node index == 1 
# second node index ( parent node index x 2 )
# thrid node index ( parent node index x 2 + 1 )

# root node index == 0
# second node index ( parent node index x 2 + 1 )
# thrid node index ( parent node index x 2 + 2 )

# 메모리 낭비 단점

# 전위순회 preorder 부모 - 왼쪽 - 오른쪽
# 트리 복사, 구조 저장, 컴파일러 설계 등에 적합.

# 중위순회 inorder 왼쪽 - 부모 - 오른쪽 
# 정렬된 데이터 출력이 필요할 때, 특히 이진 탐색 트리에서 사용.

# 후위순회 postorder 왼쪽 - 오른쪽 - 부모
# 노드 삭제, 계산, 자원 해제와 같은 작업에서 유용.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(current_node.right, data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

# 사용 예시
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)

tree.inorder_traversal(tree.root)  # 출력: 2 5 7 10 15