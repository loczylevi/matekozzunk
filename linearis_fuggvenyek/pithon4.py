import sympy
x,y = sympy.symbols('x y')

from sympy import init_printing
sympy.init_printing()

y = (1/2)*x + 2

sympy.plot(y, xlim=(-2,2), ylim=(-4,4))

#༼ つ ◕_◕ ༽つ
