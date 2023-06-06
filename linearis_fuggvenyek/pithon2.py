import sympy
x,y = sympy.symbols('x y')

from sympy import init_printing
sympy.init_printing()

y = -2*x-5

sympy.plot(y, xlim=(-3,3), ylim=(-6,2))

#༼ つ ◕_◕ ༽つ
