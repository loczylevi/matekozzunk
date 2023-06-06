import sympy
x,y = sympy.symbols('x y')

from sympy import init_printing
sympy.init_printing()

y = 3*x + 1

sympy.plot(y, xlim=(-3,3), ylim=(-4,4))

#༼ つ ◕_◕ ༽つ
