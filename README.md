# Symbolic AI: Logic & Knowledge Representation

**Author:** Zoë Finelli  
**Course:** A.B. Cognitive Science - ARTI4500  
**Date:** 19 April 2025

---

## Project Overview

This project demonstrates the implementation of **Symbolic Artificial Intelligence** and **Automated Reasoning**. Unlike statistical machine learning models (which rely on pattern recognition in large datasets), this project utilizes formal logic to model knowledge, enforce constraints, and derive truth values through strict inference.

The core objective is to bridge the gap between natural language and computational logic. By translating ambiguous English statements into **First-Order Logic (FOL)** and **Propositional Logic**, we create a knowledge base that an inference engine can use to solve puzzles and prove mathematical theorems.

---

## Technical Architecture

This repository consists of two primary components:

### 1. The Knowledge Base (`logic_problems.py`)
* **Author:** Zoë Finelli
* **Function:** This is the application layer. It defines the specific logical atoms, predicates, and axiomatic constraints that model the world. It implements solutions for propositional logic translation, kinship domains, constraint satisfaction puzzles, and number theory.

### 2. The Inference Engine (`logic.py`)
* **Author:** Percy Liang (Stanford University)
* **Function:** The backend driver that processes the formulas defined in the knowledge base. It handles the low-level computational logic, including:
    * **CNF Conversion:** Transforming formulas into Conjunctive Normal Form.
    * **Unification:** Identifying variable substitutions to match logical expressions.
    * **Resolution:** The core algorithm used to prove theorems by contradiction.
    * **Model Checking:** Verifying if a set of formulas holds true for a given domain.

---

## Implemented Domains

The `logic_problems.py` script implements four distinct areas of logical reasoning:

### A. Propositional Logic
We model boolean constraints where the truth of a complex sentence depends purely on the truth of its simpler parts.
* **Concept:** Implication ($\implies$), Bi-conditional equivalence ($\iff$), and Logical Conjunction/Disjunction.
* **Implementation Example:**
    > *"It is wet if and only if it is raining or the sprinklers are on."*
    >
    > `Equiv(Wet, Or(Rain, Sprinklers))`

### B. First-Order Logic (FOL) & Kinship
We use quantifiers to assert rules over a domain of objects, allowing us to define relationships without explicitly listing every connection in a database.
* **Concept:** Universal Quantifiers ($\forall$) and Existential Quantifiers ($\exists$).
* **Implementation Example:**
    > *"Every person has a parent."*
    >
    > `Forall('$x', Implies(Person('$x'), Exists('$y', Parent('$x', '$y'))))`

### C. Constraint Satisfaction: The Liar's Puzzle
We solve a "Knights and Knaves" style logic puzzle by encoding conflicting witness statements as axioms.
* **The Puzzle:** Four suspects (Mark, John, Nicole, Susan) give contradictory statements about a server crash.
* **The Logic:** The system uses resolution to find the only consistent model where **exactly one** person is telling the truth and **exactly one** person is guilty.

### D. Axiomatic Number Theory
We define the fundamental properties of integers using Peano-style axioms to prove properties of numbers through logical derivation.
* **Concept:** Defining "Even" and "Odd" not by arithmetic modulo, but by their relationship to a "Successor" function.
* **Axiom Example:** *"The successor of an even number is odd."*

---

## Installation & Usage

### Prerequisites
* Python 3.10 or higher.
* No external `pip` dependencies are required (uses Python Standard Library).

### Execution
1.  Ensure both `logic_problems.py` and `logic.py` are in the same directory.
2.  Run the main script to verify the axioms and see the inference engine in action:

```bash
python logic_problems.py
