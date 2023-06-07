import sympy
x,y = sympy.symbols('x y')

from sympy import init_printing
sympy.init_printing()

y = -x

sympy.plot(y, xlim=(-2,2), ylim=(-2,2))

#༼ つ ◕_◕ ༽つ
