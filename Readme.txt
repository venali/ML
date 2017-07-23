A popular quote from computer scientist Tom Mitchell de nes machine learning more formally: "A program can be said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured
by P, improves with experience E."

A supervised learning program learns from labeled examples of the outputs that should be produced for an input. There are many names for the output of a
machine learning program. Several disciplines converge in machine learning, and many of those disciplines use their own terminology. We will refer to
the output as the response variable. Other names for response variables include dependent variables, regressands, criterion variables, measured variables, responding variables, explained variables, outcome variables, experimental variables, labels,
and output variables. Similarly, the input variables have several names. We will refer to the input variables as features, and the phenomena they measure
as explanatory variables. Other names for explanatory variables include predictors, regressors, controlled variables, manipulated variables, and exposure variables. Response variables and explanatory variables may take real or discrete values.
The collection of examples that comprise supervised experience is called a training set. A collection of examples that is used to assess the performance of a program
is called a test set.


Two of the most common supervised machine learning tasks are classi cation
and regression. In classi cation tasks the program must learn to predict discrete values for the response variables from one or more explanatory variables. That
is, the program must predict the most probable category, class, or label for new observations. Applications of classi cation include predicting whether a stock's
price will rise or fall, or deciding if a news article belongs to the politics or leisure section. In regression problems the program must predict the value of a continuous response variable. Examples of regression problems include predicting the sales for a new product, or the salary for a job based on its description. 

A common unsupervised learning task is to discover groups of related observations, called clusters, within the training data. This task, called clustering or cluster analysis, assigns observations to groups such that observations within groups are more similar to each other based on some similarity measure than they are to observations in other groups.

cross-validation
The algorithm is trained using all but one of the partitions, and tested on the remaining partition. The partitions are then rotated several times so that the algorithm is trained and evaluated on all of the data.


bias variaence 
 There are two fundamental causes of prediction error: a model's bias and its variance. Assume that you have many training sets that are all unique, but equally representative of the population. A model with a high bias will produce similar errors for an input regardless of the training set it was trained with; the model biases its own assumptions about the real relationship over the relationship demonstrated in the training data. A model with high variance, conversely, will produce different errors for an input depending on the training set that it was trained with.

Accuracy
. Accuracy, or the fraction of instances that were classi ed correctly, is an intuitive measure of the program's performance.

When the system correctly classi es a tumor as being malignant, the prediction is called a true positive. When the system incorrectly classi es a benign tumor as being malignant, the prediction is a false positive. Similarly, a false negative is an incorrect prediction that the tumor is benign, and
a true negative is a correct prediction that a tumor is benign. These four outcomes can be used to calculate several common measures of classi cation performance, including accuracy, precision, and recall.


Accuracy is calculated with the following formula, where TP is the number of true positives, TN is the number of true negatives, FP is the number of false positives, and FN is the number of false negatives:
ACC = (TP + TN)/
(TP + TN + FP + FN)
Precision is the fraction of the tumors that were predicted to be malignant that are actually malignant. Precision is calculated with the following formula:
P= TP/ (TP+FP)
Recall is the fraction of malignant tumors that the system identi ed. Recall is calculated with the following formula:
R= TP/ (TP+FN)


 
