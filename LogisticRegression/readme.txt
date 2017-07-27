the goal in classi cation tasks is to  nd a function that maps an observation to its associated class or label.
A learning algorithm must use pairs of feature vectors and their corresponding labels to induce the values of the mapping function's parameters that produce the best classi er, as measured by a particular performance metric. In binary classi cation, the classi er must assign instances to one of the two classes.

In multiclass classi cation, the classi er must assign one
of several labels to each instance. In multilabel classi cation, the classi er must assign a subset of the labels to each instance.

The normal distribution, also known as the Gaussian distribution or bell curve, is a function that describes the probability that an observation will have a value between any two real numbers.


he Bernoulli distribution describes the probability distribution of a random variable that can take the positive case with probability P or the negative case with probability 1-P. If the response variable represents a probability, it must be constrained to the range {0,1}. 

The response variable is modeled as a function of a linear combination of the explanatory variables using the logistic function. Given by the following equation, the logistic function always returns a value between zero and one:
F(t)= 1 / 1+e−t

For logistic regression, t is equal to a linear combination of explanatory variables, as follows:

F(t)= 1
--------
1+ e−(β0 +βx )

The logit function is the inverse of the logistic function. It links F ( x ) back to a linear combination of the explanatory variables:
g(x)=ln F(x)/1−F(x)  =  β0 +βx


