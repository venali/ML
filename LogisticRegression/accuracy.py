#Accuracy measures a fraction of the classi er's predictions that are correct.

from sklearn.metrics import accuracy_score
y_pred, y_true = [0, 1, 1, 0], [1, 1, 1, 1]
print 'Accuracy:', accuracy_score(y_true, y_pred)
