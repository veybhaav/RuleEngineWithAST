class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # 'operator' or 'operand'
        self.value = value     # For operators like 'AND', 'OR' or operands like 'age > 30'
        self.left = left       # Left child node
        self.right = right     # Right child node

def create_rule(rule_string):
    """
    Parses a rule string into an AST.
    """
    import ast
    tree = ast.parse(rule_string, mode='eval')
    return convert_to_custom_ast(tree.body)

def convert_to_custom_ast(tree):
    """
    Recursively converts the Python AST to the custom Node-based AST.
    """
    if isinstance(tree, ast.BoolOp):  # AND/OR operator
        operator = "AND" if isinstance(tree.op, ast.And) else "OR"
        return Node('operator', operator, 
                    convert_to_custom_ast(tree.values[0]), 
                    convert_to_custom_ast(tree.values[1]))
    elif isinstance(tree, ast.Compare):  # Example: age > 30
        return Node('operand', f'{tree.left.id} {tree.ops[0].__class__.__name__} {tree.comparators[0].n}')
    elif isinstance(tree, ast.Str):  # Example: 'Sales'
        return Node('operand', tree.s)

def combine_rules(rules):
    """
    Combines multiple rules into a single AST using AND/OR.
    """
    combined = None
    for rule in rules:
        rule_ast = create_rule(rule)
        if combined:
            combined = Node('operator', 'AND', combined, rule_ast)  # Combine using AND
        else:
            combined = rule_ast
    return combined

def evaluate_rule(ast_node, user_data):
    """
    Evaluates the AST against the user data.
    """
    if ast_node.type == 'operator':
        if ast_node.value == 'AND':
            return evaluate_rule(ast_node.left, user_data) and evaluate_rule(ast_node.right, user_data)
        elif ast_node.value == 'OR':
            return evaluate_rule(ast_node.left, user_data) or evaluate_rule(ast_node.right, user_data)
    elif ast_node.type == 'operand':
        key, operator, value = ast_node.value.split()
        return eval(f"{user_data[key]} {operator} {value}")
