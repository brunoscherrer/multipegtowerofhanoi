<html>

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Multi-peg Tower of Hanoi

Illustration of **Frame-Stewart algorihm** for solving the **multi-peg Hanoi Tower problem**. Here with 10 discs.

- 3 pegs:

![](10_3.gif)

- 4 pegs:

![](10_4.gif)

- 5 pegs:

![](10_5.gif)

- 6 pegs:

![](10_6.gif)


Frame-Stewart's algorithm solves the \\(p\\)-peg \\(n\\)-disc from source to destination as follows:

- choose a height \\(h \in {1,\dots,n-1}\\) (see below) ;
- move the \\((n-h)\\)-high upper part of the tower to any peg different from source and destination, say number peg \\(i\\) ;
- move the \\(h\\)-high lower part from source to destination using all pegs except \\(i\\) ;
- move the \\((n-h)\\) from \\(i\\) to destination.

The number of steps S(n,p) to solve the p-peg n-disc problem satisfies the recurrence relation:

\\(\forall p\\ge 3, \forall n,   S(n,p) = \\min_h 2 S(n-h,p) + S(h,p-1),\\)

with \\(S(1,2) = 1\\) and \\(S(n,2)=\infty\\) for all \\(n\ge2\\).

For any \\((n,p)\\), an optimal choice \\(h(n,p)\\) is any that reaches the minimum above. 
A reasonable approximation is \\(\hat h(n,p) = n^{(p-4)/(p-3)}\\). And the optimal number of steps is in \\(O\left( 2^{n^{(p-4)/(p-3)}} \right)\\).

**References:**<br>
Sandi Klavžar, Uroš Milutinović, Ciril Petr. *On the Frame–Stewart algorithm for the multi-peg Tower of Hanoi problem.* Discrete Applied Mathematics. Volume 120, Issues 1–3, 15 August 2002, Pages 141-157.<br>
Thierry Bousch. *La quatrième tour de Hanoï.* Bull. Belg. Math. Soc. Simon Stevin Volume 21, Number 5 (2014), 895-912.<br>
Janez Zerovnik. *Self Similarities of the Tower of Hanoi Graphs and a proof of the Frame-Stewart Conjecture.* arXiv.


</html>
