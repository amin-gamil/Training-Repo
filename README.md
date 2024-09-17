## Exercise 📝

1. Since a perceptron's output is defined as:
 
   $$
   \text{output} = \left\lbrace
   \begin{array}{ll} 
   0 & \text{if } w\cdot x + b \leq 0 \\ 
   1 & \text{if } w\cdot x + b > 0 
   \end{array} 
   \right. 
   $$
   
   Multiplying all weights and biases by a constant $c > 0$, would make the piecewise:

   $$
   \text{output} = \left\lbrace 
   \begin{array}{ll} 
   0 & \text{if } cw\cdot x + cb \leq 0 \\ 
   1 & \text{if } cw\cdot x + cb > 0 
   \end{array} 
   \right. 
   $$

   Since the constant $c$ is positive, it can be divided out of the equations without inverting the inequality, having no effect on the perceptron's output.

2. The output of the sigmoid function is 
 
   $$
   \sigma = \dfrac{1}{1+e^{-z}}
   $$
   
   while defining $z = w \cdot x + b$.
   Multiplying the weights and biases by $c$ and taking the limit as $c \rightarrow \infty$:
   
   $$
   \sigma = \lim_{c \rightarrow \infty} \dfrac{1}{1+e^{-c z}}
   $$
   
   Using some math; 🤷‍♂️
   
   $$
   \sigma = \dfrac{1}{1+e^{\lim_{c \rightarrow \infty}(-c z)}}
   $$
   
   Substituting $\infty$ for simplification:
   
   $$
   \sigma = \left\lbrace 
   \begin{array}{ll} 
   \dfrac{1}{1+e^{\infty}} & \text{if } z <0 \\ 
   \dfrac{1}{1+e^{-\infty}} & \text{if } z > 0 
   \end{array} 
   \right.
   $$
   
   Since $e^\infty \rightarrow \infty$, and $e^{-\infty} \rightarrow 0$, therefore,
   
   $$
   \sigma = \left\lbrace 
   \begin{array}{ll} 
   0 & \text{if } z <0 \\ 
   1 & \text{if } z > 0 
   \end{array} 
   \right.
   $$ 
   
   Which is similar to the perceptron's output.

   If $z = 0$, the limit becomes:
   
   $$
   \lim_{c \rightarrow \infty}(-c z) = - 0 \times \infty
   $$
   
   Which is indeterminate.

3. Each neuron "bit" in the fourth layer should have 10 inputs with 10 weights. Some guiding rules are:
   - The first neuron representing the LSB would have a weight of zero for all even numbers.
   - The MSB neuron would have a weight of zero for all numbers less than 8.

   The activation of each neuron in the forth bit is 

    $$
    a = \sum_{i=0}^{9}{w_i x_i} = w \cdot x
    $$

    |  | $w_0$ | $w_1$ | $w_2$ | $w_3$ | $w_4$ | $w_5$ | $w_6$ | $w_7$ | $w_8$ | $w_9$ |
    |:-------:|:-----:|:-----:|:-----:|:-----:| :-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
    |  $a_1$  |   0   |  4.65 |   0   |  2.32 |   0   |  2.32 |   0   |  1.55 |   0   |  2.32 |
    |  $a_2$  |   0   |   0   |  4.65 |  2.32 |   0   |   0   |  2.32 |  1.55 |   0   |   0   |
    |  $a_3$  |   0   |   0   |   0   |   0   |  4.65 |  2.32 |  2.32 |  1.55 |   0   |   0   |
    |  $a_4$  |   0   |   0   |   0   |   0   |   0   |   0   |   0   |   0   |  4.65 |  2.32 |

    These weights would work for all digits expect zero where the output wouldn't be activated at all since $w_0=0$ for all neurons. That's why we need to add bias,

    $$b_0 = 3$$

    and update the weights to be;

    | Weights | $w_0$ | $w_1$ | $w_2$ | $w_3$ | $w_4$ | $w_5$ | $w_6$ | $w_7$ | $w_8$ | $w_9$ |
    |:-------:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
    |  $a_1$  |   -1  |  4.65 |   0   |  2.32 |   0   |  2.32 |   0   |  1.55 |   0   |  2.32 |
    |  $a_2$  |   -1  |   0   |  4.65 |  2.32 |   0   |   0   |  2.32 |  1.55 |   0   |   0   |
    |  $a_3$  |   -1  |   0   |   0   |   0   |  4.65 |  2.32 |  2.32 |  1.55 |   0   |   0   |
    |  $a_4$  |   -1  |   0   |   0   |   0   |   0   |   0   |   0   |   0   |  4.65 |  2.32 |

## Creating a Neural Network
To create a neural network, we need to implement:

1. The stochastic gradient descent algorithm (SGD).
2. A way to calculate the gradients at each mini-batch.
3. Evaluation for each epoch.

A lot of the code is reused from [the book](http://neuralnetworksanddeeplearning.com/chap1.html#learning_with_gradient_descent).