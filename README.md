<p><html>
<head></p>

<script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

<p></head> 
<body></p>

<h1>Multi-peg Tower of Hanoi</h1>

<p>We consider <strong>Stewart's algorihm</strong> for solving the <strong>multi-peg Hanoi Tower problem</strong>.</p>

<h2>Algorithm</h2>

<p>Stewart's algorithm solves the p-peg n-disc from source to destination as follows:</p>

<ul>
<li>choose a height \(h\in\left\{1,\dots,n-1\right\}\) (see below) ;</li>
<li>move the \((n-h)\)-high upper part of the tower to any peg different from source and destination, say number peg \(i\) ;</li>
<li>move the \(h\)-high lower part from source to destination using all pegs except \(i\) ;</li>
<li>move the \((n-h)\) from \(i\) to destination.</li>
</ul>

<p>See <a href="#anim">below</a> for an illustration of this algorithm for n=10 discs.</p>

<h2>Quick analysis</h2>

<p>The number of steps \(S(n,p)\) to solve the p-peg n-disc problem satisfies the recurrence relation:</p>

<p>\(\forall{}p\ge{}3,{}\forall{}n,{}S(n,p)=\min_{1\le{}h\le{}n-1}2S(n-h,p)+S(h,p-1),\) <br>
with \(S(1,2)=1\) and \(S(n,2)=\infty\) for all \(n\ge{}2.\)</p>

<p>For any \((n,p)\), an optimal choice is any element of the argmin set \(h(n,p)\).</p>

<p>Here are illustrations of the optimal values and the set and the number of minimizers:</p>

<ul>
<li>p=3</li>
</ul>

<p><img src="S_h_3.png" alt="" title="" /></p>

<ul>
<li>p=4</li>
</ul>

<p><img src="S_h_4.png" alt="" title="" /></p>

<ul>
<li>p=5</li>
</ul>

<p><img src="S_h_5.png" alt="" title="" /></p>

<ul>
<li>p=6</li>
</ul>

<p><img src="S_h_6.png" alt="" title="" /></p>

<p>These graphs suggest that there are many paths. In fact, the number of paths $N(n,p)$ can be seen to satisfy the following recurrence:</p>

<p>\(N(n,p) = \sum_{h \in h(n,p)} N(h,p)+N(n-h,p-1),\) <br>
with \(N(n,p)=1\) if \( n &lt; p \) or \( p=3 \).</p>

<h2>Graphical illustration of the algorithm <a name="anim"></a></h2>

<ul>
<li>3 pegs:</li>
</ul>

<p><img src="10_3.gif" alt="" title="" /></p>

<ul>
<li>4 pegs:</li>
</ul>

<p><img src="10_4.gif" alt="" title="" /></p>

<ul>
<li>5 pegs:</li>
</ul>

<p><img src="10_5.gif" alt="" title="" /></p>

<ul>
<li>6 pegs:</li>
</ul>

<p><img src="10_6.gif" alt="" title="" /></p>

<h2>References</h2>

<p>Sandi Klavžar, Uroš Milutinović, Ciril Petr. <em>On the Frame–Stewart algorithm for the multi-peg Tower of Hanoi problem.</em> Discrete Applied Mathematics. Volume 120, Issues 1–3, 15 August 2002, Pages 141-157.<br>
Thierry Bousch. <em>La quatrième tour de Hanoï.</em> Bull. Belg. Math. Soc. Simon Stevin Volume 21, Number 5 (2014), 895-912.<br></p>

<p></body>
</html></p>
