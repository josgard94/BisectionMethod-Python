# BisectionMethod-Python
The bisection method is based on the mean value theorem and assumes that f (a) and f (b) have opposite signs. Basically, the method involves repeatedly halving the subintervals of [a, b] and in each step, locating the half containing the solution, m.

Below is an example of approximation of the root of the function f (x) = 10x ^ 2:

interval a: -2
interval b: 5

n  |	   a 		|	   b 		|	    c 	 |   f(a)	   |    f(b) 		 |  f(c)

1  | -2.00000 | 5.00000 |	 1.50000 |	6.00000  |	-15.00000  | 7.75000

2  | 1.50000 	| 5.00000 |	 3.25000 |	7.75000  |	-15.00000  | -0.56250

3  | 1.50000 	| 3.25000 |	 2.37500 |	7.75000  |	-0.56250 	 | 4.35938

4  | 2.37500 	| 3.25000 |	 2.81250 |	4.35938  |	-0.56250   | 2.08984

5  | 2.81250 	| 3.25000 |	 3.03125 |	2.08984  |	-0.56250 	 | 0.81152

6  | 3.03125 	| 3.25000 |	 3.14062 |	0.81152  |	-0.56250 	 | 0.13647

7  | 3.14062 	| 3.25000 |	 3.19531 |	0.13647  |	-0.56250 	 | -0.21002

8  | 3.14062 	| 3.19531 |	 3.16797 |	0.13647  |	-0.21002 	 | -0.03603

9  | 3.14062 	| 3.16797 |	 3.15430 |	0.13647  |	-0.03603 	 | 0.05041

10 | 3.15430 	| 3.16797 |	 3.16113 |	0.05041  |	-0.03603 	 | 0.00724

Result: 
Approximate root:  3.16113  iterations performed:  10  Error:  0.00724
