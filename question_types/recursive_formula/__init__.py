# coding=utf-8

import numpy as np
import sympy
from sympy.solvers import solve
from modules.generators.matrix import pmatrix_displaymath

x = sympy.Symbol("x")
k = sympy.Symbol("k");

def generateCoefficients(): 

    coefficients = np.random.randint(-10, 10, 2)

    while len(solve(x**2 - coefficients[1] * x - coefficients[0], x)) < 2:
        coefficients = np.random.randint(-10, 10, 2)

    return coefficients

def generate_question(matrix_dimension=3, max_random_value=4, min_random_value=-4):

    coefficients = generateCoefficients()
    startValues = np.random.randint(-10, 10, 2)

    output = "\\question Die Folge \( (a_n)_{n \\in \\mathbb{{N}}_0} \) mit \( a_n \\in \\mathbb{{Q}} \) sei definiert durch die Rekursionsgleichung"
    output += "\\begin{align*} a_n = " + str(coefficients[0]) + "a_{n-2} " + '{0:+d}'.format(coefficients[1]) + " a_{n-1} \\end{align*}"
    output += "für alle \( n \geq 2 \), und die Anfangsglieder"
    output += "\\begin{align*} a_0=" + str(startValues[0]) + ", a_1=" + str(startValues[1]) + ". \\end{align*}"
    output += "Berechnen Sie mit Methoden der linearen Algebra eine geschlossene Formel für die Folgenglieder \(a_n\)."

    b = solve(x**2 - coefficients[1] * x - coefficients[0], x)
    exp = sympy.simplify( pow(b[0]**k*b[1] - b[1]**k*b[0] / (b[1] - b[0])) * startValues[0] + (b[1]**k - b[0]**k / (b[1] - b[0])) * startValues[1])

    print(exp);

    output += "\\begin{solutionorbox}[1in]\n"

    output += f"${sympy.latex(exp)}$"

    output += "\\end{solutionorbox}\n"

    return [output]


if __name__ == "__main__":
    print(generate_question())
