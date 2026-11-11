# ==============================================
# Assessment 3.3: Non-Linear Data Structure
# Last Name: RESABA
# ==============================================

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


# ---------------- BUILD THE TREE ----------------
def build_tree():
    # Level 0 — Root
    root = Node('R')

    # Level 1
    root.left = Node('E')
    root.right = Node('S')

    # Level 2
    root.left.left = Node('S')
    root.left.right = Node('A')
    root.right.left = Node('A')
    root.right.right = Node('B')

    return root


# ---------------- BFS TRAVERSAL ----------------
from collections import deque


def bfs_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


# ---------------- DFS TRAVERSAL (Pre-order) ----------------
def dfs_traversal(root):
    result = []

    def preorder(node):
        if not node:
            return
        result.append(node.data)
        preorder(node.left)
        preorder(node.right)

    preorder(root)
    return result


# ---------------- RUN & DISPLAY ----------------
if __name__ == "__main__":
    tree_root = build_tree()

    print("=" * 50)
    print("     Assessment 3.3 — RESABA Tree Traversal")
    print("=" * 50)

    print("\n🌳 Binary Tree Structure:")
    print("        R")
    print("      /   \\")
    print("     E     S")
    print("    / \\   / \\")
    print("   S   A A   B")

    bfs_result = bfs_traversal(tree_root)
    dfs_result = dfs_traversal(tree_root)

    print("\n🔹 BFS (Breadth-First Search):")
    print("   Result:", " → ".join(bfs_result))

    print("\n🔹 DFS (Depth-First Search — Pre-order):")
    print("   Result:", " → ".join(dfs_result))

    print("\n✅ Done!")
