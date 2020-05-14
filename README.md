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

<img src="https://latex.codecogs.com/svg.latex?&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" title="x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />


Frame-Stewart's algorithm solves the <img src="https://latex.codecogs.com/svg.latex?&space;p"/>-peg <img src="https://latex.codecogs.com/svg.latex?n"/>-disc from source to destination as follows:

- choose a height <img src="https://latex.codecogs.com/svg.latex?h \in {1,\dots,n-1}"/> (see below) ;
- move the <img src="https://latex.codecogs.com/svg.latex?(n-h)"/>-high upper part of the tower to any peg different from source and destination, say number peg <img src="https://latex.codecogs.com/svg.latex?i"/> ;
- move the <img src="https://latex.codecogs.com/svg.latex?h"/>-high lower part from source to destination using all pegs except <img src="https://latex.codecogs.com/svg.latex?i"/> ;
- move the <img src="https://latex.codecogs.com/svg.latex?(n-h)"/> from <img src="https://latex.codecogs.com/svg.latex?i"/> to destination.

The number of steps <img src="https://latex.codecogs.com/svg.latex?S(n,p)"/> to solve the p-peg n-disc problem satisfies the recurrence relation:

<img src="https://latex.codecogs.com/svg.latex?\forall&space;p\ge&space;3,&space;\forall&space;n,&space;S(n,p)=\min_h2S(n-h,p)+S(h,p-1),"/>

with <img src="https://latex.codecogs.com/svg.latex?S(1,2)=1"/> and <img src="https://latex.codecogs.com/svg.latex?S(n,2)=\infty"/> for all <img src="https://latex.codecogs.com/svg.latex?n\ge&space;2"/>.

For any <img src="https://latex.codecogs.com/svg.latex?(n,p)"/>, an optimal choice <img src="https://latex.codecogs.com/svg.latex?h(n,p)"/> is any that reaches the minimum above. 
A reasonable approximation is <img src="https://latex.codecogs.com/svg.latex?\hat&space;h(n,p)=n^{(p-4)/(p-3)}"/>. And the optimal number of steps is <img src="https://latex.codecogs.com/svg.latex?O\left(2^{n^{(p-4)/(p-3)}}\right)"/>.

**References:**<br>
Sandi Klavžar, Uroš Milutinović, Ciril Petr. *On the Frame–Stewart algorithm for the multi-peg Tower of Hanoi problem.* Discrete Applied Mathematics. Volume 120, Issues 1–3, 15 August 2002, Pages 141-157.<br>
Thierry Bousch. *La quatrième tour de Hanoï.* Bull. Belg. Math. Soc. Simon Stevin Volume 21, Number 5 (2014), 895-912.<br>
Janez Zerovnik. *Self Similarities of the Tower of Hanoi Graphs and a proof of the Frame-Stewart Conjecture.* arXiv.
