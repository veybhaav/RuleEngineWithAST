
from ast_module import create_rule, evaluate_rule, combine_rules

def test_create_individual_rules():
    rule1 = "((age > 30 AND department == 'Sales') OR (age < 25 AND department == 'Marketing')) AND (salary > 50000 OR experience > 5)"
    rule_ast = create_rule(rule1)
    
    # Simple check if the root node is 'AND'
    assert rule_ast.type == 'operator'
    assert rule_ast.value == 'AND'
    print("Test 1 passed: Rule creation verified.")

def test_combine_rules():
    rule1 = "((age > 30 AND department == 'Sales')) AND (salary > 50000)"
    rule2 = "(experience > 5)"
    
    combined_ast = combine_rules([rule1, rule2])
    
    # Check if combined AST root node is 'AND'
    assert combined_ast.type == 'operator'
    assert combined_ast.value == 'AND'
    print("Test 2 passed: Rule combination verified.")

def test_evaluate_rule():
    rule1 = "((age > 30 AND department == 'Sales') OR (age < 25 AND department == 'Marketing')) AND (salary > 50000 OR experience > 5)"
    rule_ast = create_rule(rule1)
    
    data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    assert evaluate_rule(rule_ast, data) == True

    data2 = {"age": 22, "department": "Marketing", "salary": 40000, "experience": 4}
    assert evaluate_rule(rule_ast, data2) == False

    print("Test 3 passed: Rule evaluation verified.")

# Run tests
test_create_individual_rules()
test_combine_rules()
test_evaluate_rule()
