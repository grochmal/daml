## daml-10-01-online-learning.ipynb 18:30-19:00

- two functions: one is the model, the other the error
- gradient descent direction can be solved analytically
- SGD uses a sample of the data, so it is faster and can deal with more data
- run the dataset collection twice, i forgot to remove np.loadtxt
- note the class weights, the ozone dataset is not balanced
- the example of actual online learning is too random, be careful
- do not spend too much on the extra techniques

## daml-10-02-perceptron.ipynb 19:00-19-30

- bias term, either amplifier or the intercept in function construction
- sign function was the original perceptron idea
- xor will fail to converge, xor is not a linear division
- all other binary functions are similar to the sign function
- we can do it with 3 perceptrons

## pause 19:30-19:40

## daml-10-03-neural-networks.ipynb 19:40-20:00

- the glass dataset need to be run twice as well, need to fix it
- forensics, if you want to play poirot you now can
- the support for this dataset isn't great but we can make it work
- activation functions is a lot of plotting code
- backpropagation is hard to explain
- if there's time draw the derivate of sin(x) + 2 and show the gradients
- there are many, many hyperparameters in an ann

## daml-10-04-ann-architectures.ipynb 20:00-20:10

- there's a lot to remind yourself about here, read it just before the lecture
- apart from tensorflow there is also pytorch
- use the playground to show feature extraction by layers

## daml-10-05-what-next.ipynb 20:10-20:30

- focus on sklearn user guide
- there's much, much more on anns these days

