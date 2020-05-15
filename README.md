# Multi-peg Tower of Hanoi

We consider **Stewart's algorihm** for solving the **multi-peg Hanoi Tower problem**.

## Algorithm

Stewart's algorithm solves the p-peg n-disc from source to destination as follows:

- choose a height <img src="https://latex.codecogs.com/svg.latex?h\in\left\{1,\dots,n-1\right\}"/> (see below) ;
- move the <img src="https://latex.codecogs.com/svg.latex?(n-h)"/>-high upper part of the tower to any peg different from source and destination, say number peg <img src="https://latex.codecogs.com/svg.latex?i"/> ;
- move the <img src="https://latex.codecogs.com/svg.latex?h"/>-high lower part from source to destination using all pegs except <img src="https://latex.codecogs.com/svg.latex?i"/> ;
- move the <img src="https://latex.codecogs.com/svg.latex?(n-h)"/> from <img src="https://latex.codecogs.com/svg.latex?i"/> to destination.

See [below](#anim) for an illustration of this algorithm for n=10 discs.

## Quick analysis

The number of steps <img src="https://latex.codecogs.com/svg.latex?S(n,p)"/> to solve the p-peg n-disc problem satisfies the recurrence relation:

<img src="https://latex.codecogs.com/svg.latex?\forall{}p\ge{}3,{}\forall{}n,{}S(n,p)=\min_{1\le{}h\le{}n-1}2S(n-h,p)+S(h,p-1),"/>

with <img src="https://latex.codecogs.com/svg.latex?S(1,2)=1"/> and <img src="https://latex.codecogs.com/svg.latex?S(n,2)=\infty"/> for all <img src="https://latex.codecogs.com/svg.latex?n\ge{}2"/>.

For any <img src="https://latex.codecogs.com/svg.latex?(n,p)"/>, an optimal choice <img src="https://latex.codecogs.com/svg.latex?h(n,p)"/> is any that reaches the minimum above. 
A reasonable approximation is <img src="https://latex.codecogs.com/svg.latex?\hat{h}(n,p)=n^r"/> with <img src="https://latex.codecogs.com/svg.latex?r=\frac{p-4}{p-3}"/>, and the optimal number of steps is <img src="https://latex.codecogs.com/svg.latex?O\left(2^{n^r+o(n^r)}\right)"/>.

Here are illustrations of the optimal values and the set of minimizers:

- p=3

![](S_h_3.png)

- p=4

![](S_h_4.png)

- p=5

![](S_h_5.png)

- p=6

![](S_h_6.png)

These graphs suggest that there are many optimal paths.


## Graphical illustration of the algorithm <a name="anim"></a>

- 3 pegs:

![](10_3.gif)

- 4 pegs:

![](10_4.gif)

- 5 pegs:

![](10_5.gif)

- 6 pegs:

![](10_6.gif)

## References

Sandi Klavžar, Uroš Milutinović, Ciril Petr. *On the Frame–Stewart algorithm for the multi-peg Tower of Hanoi problem.* Discrete Applied Mathematics. Volume 120, Issues 1–3, 15 August 2002, Pages 141-157.<br>
Thierry Bousch. *La quatrième tour de Hanoï.* Bull. Belg. Math. Soc. Simon Stevin Volume 21, Number 5 (2014), 895-912.<br>
