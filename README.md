## Exercise 📝

Since a perceptron's output is defined as:
 
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

The output of the sigmoid function is 
 
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

A lot of the code is reused from [the book](http://neuralnetworksanddeeplearning.com/chap1.html#learning_with_gradient_descent). Whith modifications mainly to support Python 3.

### Stochastic Gradient Descent

```python
def SGD(self, training_data, epochs, mini_batch_size, eta,
            test_data=None):
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print(f"Epoch {j}: {self.evaluate(test_data)} / {n_test}")
            else:
                print(f"Epoch {j} complete")
```

The first thing is shuffling the dataset and dividing into `mini_batches`. These batches will be used for estimating the SGD.

```python
random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in range(0, n, ini_batch_size)]
```

Then, a for each `mini_batch`, the weights and biases are updated for each gradient.

```python
for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
```

This `self.update_mini_batch(mini_batch, eta)` method works using the backwards propagation algorithm which is implemented using the `backprob()` method.

### Evaluating the performance

The neural networks performance by passing the `test_data` argument. Using `evaluate(test_data)`, the number of correct outputs for the test inputs. The net's output is calculated using `feedforward(x)`.

### Running the code

A python file named `test.py` is created to test the neural network. In order to run the code in Python 3, modifications done are:

1. Using `pickle` instead of `cPickle` to decompress the dataset.
2. Wrapping the zip calls in a list; `list(zip(...))` instead `zip(...)`.

### Output

After running the 'test.py' file using parameters; 30 epochs, 10 mini-batch size and 3.0 learning rate, the following the output is shown
```
Epoch 0: 8129 / 10000
Epoch 1: 8294 / 10000
Epoch 2: 8400 / 10000
Epoch 3: 8478 / 10000
Epoch 4: 8453 / 10000
Epoch 5: 8483 / 10000
Epoch 6: 8525 / 10000
Epoch 7: 8510 / 10000
Epoch 8: 8509 / 10000
Epoch 9: 8536 / 10000
Epoch 10: 8520 / 10000
Epoch 11: 8508 / 10000
Epoch 12: 8548 / 10000
Epoch 13: 8529 / 10000
Epoch 14: 8557 / 10000
Epoch 15: 8527 / 10000
Epoch 16: 8525 / 10000
Epoch 17: 8548 / 10000
Epoch 18: 8558 / 10000
Epoch 19: 8552 / 10000
Epoch 20: 8532 / 10000
Epoch 21: 8582 / 10000
Epoch 22: 8714 / 10000
Epoch 23: 9486 / 10000
Epoch 24: 9498 / 10000
Epoch 25: 9476 / 10000
Epoch 26: 9483 / 10000
Epoch 27: 9499 / 10000
Epoch 28: 9502 / 10000
Epoch 29: 9490 / 10000
```
Which indicates the neural net has an accuracy of $94.9 \%$ After 30 epochs, meaning for the 10000 images in the testing data, 9490 were identified correctly.