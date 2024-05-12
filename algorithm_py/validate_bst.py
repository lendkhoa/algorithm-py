# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    nodeOneIsAncestor = isAncestor(nodeOne, nodeTwo)
    nodeThreeIsAncestor = isAncestor(nodeThree, nodeTwo)
    nodeThreeIsDescendant = False
    nodeOneIsDescendant = False

    if nodeOneIsAncestor:
        nodeThreeIsDescendant = isAncestor(nodeTwo, nodeThree)
    if nodeThreeIsAncestor:
        nodeOneIsDescendant = isAncestor(nodeTwo, nodeOne)

    return (nodeOneIsAncestor and nodeThreeIsDescendant) or (
        nodeThreeIsAncestor and nodeOneIsDescendant
    )


def isAncestor(nodeA, nodeB) -> bool:
    children = [nodeA.left, nodeA.right]
    while children:
        current = children.pop()
        if current:
            if current.value == nodeB.value:
                return True
            if current.left:
                children.append(current.left)
            if current.right:
                children.append(current.right)

    return False
