# Rule Engine with Abstract Syntax Tree (AST)

## Project Overview

The **Rule Engine with AST** is a dynamic eligibility assessment system designed to evaluate user eligibility based on various configurable attributes (e.g., age, department, income, and spending). This project demonstrates how to structure complex eligibility rules using an Abstract Syntax Tree (AST) for flexibility, allowing rule creation, combination, modification, and evaluation based on custom conditions. 

This system is highly applicable for situations requiring dynamic eligibility criteria evaluation, such as in insurance, finance, and access control systems.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
  - [Example Workflow](#example-workflow)
- [Project Structure](#project-structure)
- [Functionality Overview](#functionality-overview)
- [Testing](#testing)
- [Design Choices](#design-choices)
- [Dependencies](#dependencies)
- [Future Enhancements](#future-enhancements)
- [Acknowledgments](#acknowledgments)

---

## Features

- **Dynamic Rule Creation**: Create rules with complex logic using logical operators (`AND`, `OR`) and specific conditions (e.g., age > 30).
- **AST Representation**: Efficiently structure rules in an AST to handle rule creation, modification, and evaluation.
- **Rule Combination**: Combine multiple rules to form complex conditions, with logical optimizations to avoid redundancy.
- **JSON Data Evaluation**: Evaluate user data represented in JSON format against the combined AST rule.
- **Error Handling & Validation**: Provides validation for rule syntax, operator checking, and correct data structure.

---

## Prerequisites

To get started, make sure you have:

- **Python 3.x** installed on your system
- **Docker** (optional) if you prefer a containerized setup

---

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your_username/RuleEngineWithAST.git
cd RuleEngineWithAST
```


Step 2: Install Dependencies
Install the necessary packages using pip:



pip install -r requirements.txt
Usage
Running Locally
To run the rule engine, execute:

python rule_engine.py
Docker Setup (Optional)
A Dockerfile is provided for containerized setup, along with a docker-compose.yml file for easier deployment.


Build and Run with Docker Compose

docker-compose up --build
Example Workflow
Define a Rule: Create a rule string to define eligibility criteria, such as:


rule_string = "((age > 30 AND department == 'Sales') OR (age < 25 AND department == 'Marketing')) AND (salary > 50000 OR experience > 5)"
Generate AST: Convert the rule string into an AST representation:


rule_ast = create_rule(rule_string)
Evaluate Rule: Apply the rule to a user’s data (provided as JSON):


data = { "age": 32, "department": "Sales", "salary": 55000, "experience": 4 }
result = evaluate_rule(rule_ast, data)
print(result)  # True or False based on evaluation
Combine Multiple Rules: Use the combine_rules() function to merge multiple rules if needed, creating a more complex AST.

