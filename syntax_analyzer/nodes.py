# walay gamit :3
class ProgramNode:
    def __init__(self, token):
        self.token = token

    def get(self, key):
        return self.token[key]

    def __repr__(self):
        return f"{self.token}"

class VariableNode:
    def __init__(self, left, right, assign_op = None, value = None):
        self.left = left
        self.right = right
        self.assign_op = assign_op
        self.value = value

    def get_left(self, key):
        return self.left[key]

    def get_right(self, key):
        return self.right[key]

    def __repr__(self):
        return f"{self.left}, {self.right}, {self.assign_op}, {self.value}"

class NumberNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f"{self.token}"

