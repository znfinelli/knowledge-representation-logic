"""
Description:
    This module demonstrates the implementation of Symbolic AI concepts using 
    Python. It defines logical axioms and formulas to model natural language 
    statements, utilizing a custom inference engine to handle Propositional 
    Logic and First-Order Logic (FOL).

    Key Components:
    1. Propositional Logic: Modeling boolean constraints.
    2. First-Order Logic: Using quantifiers (Forall, Exists) to model domains.
    3. Constraint Satisfaction: Solving the 'Liars and Truth-tellers' puzzle.
    4. Axiomatic Systems: defining Peano-style axioms for Number Theory.

Dependencies:
    - logic.py (Inference Engine Backend)
"""

import collections
import os
import sys
from typing import List, Tuple

# Import the inference engine
from logic import *

############################################################
# Section 1: Propositional Logic
############################################################

def formula1a() -> Formula:
    """
    Sentence: "If it's summer and we're in California, then it doesn't rain."
    """
    Summer = Atom('Summer')
    California = Atom('California')
    Rain = Atom('Rain')
    
    return Implies(And(Summer, California), Not(Rain))

def formula1b() -> Formula:
    """
    Sentence: "It's wet if and only if it is raining or the sprinklers are on."
    """
    Rain = Atom('Rain')
    Wet = Atom('Wet')
    Sprinklers = Atom('Sprinklers')
    
    return Equiv(Wet, Or(Rain, Sprinklers))

def formula1c() -> Formula:
    """
    Sentence: "Either it's day or night (but not both)."
    """
    Day = Atom('Day')
    Night = Atom('Night')
    
    return And(Or(Day, Night), Not(And(Day, Night)))

############################################################
# Section 2: First-Order Logic
############################################################

def formula2a() -> Formula:
    """
    Sentence: "Every person has a parent."
    """
    def Person(x): return Atom('Person', x)
    def Parent(x, y): return Atom('Parent', x, y)

    return Forall('$x', Implies(Person('$x'), Exists('$y', Parent('$x', '$y'))))

def formula2b() -> Formula:
    """
    Sentence: "At least one person has no children."
    """
    def Person(x): return Atom('Person', x)
    def Child(x, y): return Atom('Child', x, y)

    return Exists('$x', And(Person('$x'), Not(Exists('$y', Child('$x', '$y')))))

def formula2c() -> Formula:
    """
    Defines 'Father' in terms of 'Male' and 'Parent'.
    """
    def Male(x): return Atom('Male', x)
    def Parent(x, y): return Atom('Parent', x, y)
    def Father(x, y): return Atom('Father', x, y)
    
    return Forall('$x', Forall('$y', Equiv(And(Male('$x'), Parent('$y', '$x')), Father('$y', '$x'))))

def formula2d() -> Formula:
    """
    Defines 'Granddaughter' in terms of 'Female' and 'Child'.
    """
    def Female(x): return Atom('Female', x)
    def Child(x, y): return Atom('Child', x, y)
    def Granddaughter(x, y): return Atom('Granddaughter', x, y)
    
    return Forall('$x', Forall('$y', Equiv(Granddaughter('$y', '$x'), And(Female('$x'), Exists('$z', And(Child('$y', '$z'), Child('$z', '$x')))))))

############################################################
# Section 3: Constraint Satisfaction (Liar Puzzle)
############################################################

def liar() -> Tuple[List[Formula], Formula]:
    """
    Solves a logic puzzle with the following facts:
    0. Mark: "It wasn't me!"
    1. John: "It was Nicole!"
    2. Nicole: "No, it was Susan!"
    3. Susan: "Nicole's a liar."
    4. Exactly one person is telling the truth.
    5. Exactly one person crashed the server.
    
    Returns:
        Tuple containing the list of formulas and the query (Who crashed the server?).
    """
    def TellTruth(x): return Atom('TellTruth', x)
    def CrashedServer(x): return Atom('CrashedServer', x)
    
    mark = Constant('mark')
    john = Constant('john')
    nicole = Constant('nicole')
    susan = Constant('susan')
    people = [mark, john, nicole, susan]
    
    formulas = []
    
    # 0. Mark's statement
    formulas.append(Equiv(TellTruth(mark), Not(CrashedServer(mark))))
    # 1. John's statement
    formulas.append(Equiv(TellTruth(john), CrashedServer(nicole)))
    # 2. Nicole's statement
    formulas.append(Equiv(TellTruth(nicole), CrashedServer(susan)))
    # 3. Susan's statement
    formulas.append(Equiv(TellTruth(susan), Not(TellTruth(nicole))))

    # 4. Exactly one person is telling the truth
    oneTruth = And(
        OrList([TellTruth(p) for p in people]), 
        AndList([Not(And(TellTruth(p1), TellTruth(p2))) for i, p1 in enumerate(people) for p2 in people[i+1:]])
    )
    formulas.append(oneTruth)

    # 5. Exactly one person crashed the server
    oneCrash = And(
        OrList([CrashedServer(p) for p in people]), 
        AndList([Not(And(CrashedServer(p1), CrashedServer(p2))) for i, p1 in enumerate(people) for p2 in people[i+1:]])
    )
    formulas.append(oneCrash)
    
    query = CrashedServer('$x')
    return (formulas, query)

############################################################
# Section 4: Number Theory Axioms
############################################################

def ints() -> Tuple[List[Formula], Formula]:
    """
    Defines the axioms for Even/Odd integers and Successors.
    Query: For each number, does there exist an even number larger than it?
    """
    def Even(x): return Atom('Even', x)
    def Odd(x): return Atom('Odd', x)
    def Successor(x, y): return Atom('Successor', x, y)
    def Larger(x, y): return Atom('Larger', x, y)

    formulas = []
    
    # 1. Each number $x$ has exactly one successor, which is not equal to $x$.
    formulas.append(Forall('$x', Exists('$y', AndList([Successor('$x', '$y'), Not(Equals('$x', '$y')), Forall('$z', Implies(Successor('$x', '$z'), Equals('$z', '$y')))]))))
    
    # 2. Each number is either even or odd, but not both.
    formulas.append(Forall('$x', And(Or(Odd('$x'), Even('$x')), Not(And(Odd('$x'), Even('$x'))))))
    
    # 3. The successor number of an even number is odd.
    formulas.append(Forall('$x', Forall('$y', Implies(And(Even('$x'), Successor('$x', '$y')), Odd('$y')))))
    
    # 4. The successor number of an odd number is even.
    formulas.append(Forall('$x', Forall('$y', Implies(And(Odd('$x'), Successor('$x', '$y')), Even('$y')))))
    
    # 5. For every number $x$, the successor of $x$ is larger than $x$.
    formulas.append(Forall('$x', Forall('$y', Implies(Successor('$x', '$y'), Larger('$y', '$x')))))
    
    # 6. Larger is a transitive property.
    formulas.append(Forall('$x', Forall('$y', Forall('$z', Implies(And(Larger('$x', '$y'), Larger('$y', '$z')), Larger('$x', '$z'))))))
    
    query = Forall('$x', Exists('$y', And(Even('$y'), Larger('$y', '$x'))))
    return (formulas, query)


############################################################
# Execution Entry Point
############################################################

if __name__ == '__main__':
    print("\n" + "="*50)
    print(" LOGIC & KNOWLEDGE REPRESENTATION DEMO")
    print("="*50 + "\n")

    print("--- 1. Propositional Logic Examples ---")
    print(f"Formula 1a (Summer/Rain):  {formula1a()}")
    print(f"Formula 1b (Wet/Rain):     {formula1b()}")
    print(f"Formula 1c (Day/Night):    {formula1c()}")
    print("\n")

    print("--- 2. First-Order Logic Examples ---")
    print(f"Formula 2a (Parents):       {formula2a()}")
    print(f"Formula 2b (No Children):   {formula2b()}")
    print(f"Formula 2c (Father def):    {formula2c()}")
    print(f"Formula 2d (Granddaughter): {formula2d()}")
    print("\n")

    print("--- 3. The Liar Puzzle Setup ---")
    liar_formulas, liar_query = liar()
    print(f"Query: {liar_query}")
    print(f"Number of Fact/Rule Axioms: {len(liar_formulas)}")
    print("Sample Axiom (Mark's statement):")
    print(f"  {liar_formulas[0]}")
    print("\n")

    print("--- 4. Number Theory Axioms ---")
    int_formulas, int_query = ints()
    print(f"Query: {int_query}")
    print(f"Number of Axioms defined: {len(int_formulas)}")
    print("Sample Axiom (Successor is Larger):")
    print(f"  {int_formulas[4]}")
    print("\n")
