## Exercise 
1. Since a perceptron's output is defined as:
   $$ \text{output} = \left\{ \begin{array}{ll}   0 & \text{if } w\cdot x + b \leq 0 \\ 1 & \text{if } w\cdot x + b > 0 \end{array} \right. $$ 
   Multiplying all weights and biases by a constant c > 0, would make the piecewise :

   $$\text{output} = \left\{ \begin{array}{ll}   0 & \text{if } cw\cdot x + c  b \leq 0 \\ 1 & \text{if } cw\cdot x + cb > 0 \end{array} \right.$$ 

   Since the constant $c$ is positive, it can be divided out of the equations without inverting the inequality, having no effect on the perceptron's output.

2. The output of the sigmoid function is 
   $$ \sigma = \dfrac{1}{1+e^{-z}}$$
   while defining $z = w \cdot x + b$.
   Multiplying the weights and biases by $c$ and taking the limit while $c \rightarrow \infty$ 
   $$ \sigma = \lim_{c \rightarrow \infty} \dfrac{1}{1+e^{-c z}}$$
   Using some math; 🤷‍♂️
   $$ \sigma = \dfrac{1}{1+e^{\lim_{c \rightarrow \infty}(-c z)}} $$
   Substituting by $\infty$ for simplification;
   $$\sigma = \left\{ \begin{array}{ll}   \dfrac{1}{1+e^{\infty}} & \text{if } z <0 \\ \\\dfrac{1}{1+e^{-\infty}} & \text{if } z > 0 \end{array} \right.$$ 
   Since $e^\infty \rightarrow \infty$, and $e^{-\infty} \rightarrow 0$, therefore,
   $$\sigma = \left\{ \begin{array}{ll}   0 & \text{if } z <0 \\ 1 & \text{if } z > 0 \end{array} \right.$$ 
   Which is similar to the perceptron's output.

   If $z = 0$, the limit becomes
   $$\lim_{c \rightarrow \infty}(-c z) = - 0 \times \infty$$
   Which is indeterminate.
   
   

   