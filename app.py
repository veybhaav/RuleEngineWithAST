
from flask import Flask, request, jsonify
from ast_module import create_rule, evaluate_rule, combine_rules
from db_module import save_rule_to_db, get_rule_from_db

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json['rule']
    rule_ast = create_rule(rule_string)
    
    # Save to DB (serialization logic to be handled in db_module.py)
    save_rule_to_db(rule_string)
    
    return jsonify({'status': 'Rule created', 'rule': rule_string})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    rule_id = request.json['rule_id']
    user_data = request.json['data']
    
    # Fetch rule from DB and deserialize it (handled in db_module.py)
    rule_ast = get_rule_from_db(rule_id)
    
    result = evaluate_rule(rule_ast, user_data)
    return jsonify({'result': result})

@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    rules = request.json['rules']
    
    # Combine rules
    combined_ast = combine_rules(rules)
    
    # Optionally save combined AST to DB
    save_rule_to_db(' AND '.join(rules))
    
    return jsonify({'status': 'Rules combined', 'combined_ast': combined_ast.value})

if __name__ == '__main__':
    app.run(debug=True)
