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
