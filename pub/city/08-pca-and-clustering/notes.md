## daml-08-01-clas-vs-regr.ipynb 18:30-18:50

- classification and regressions are the same thing
- classification is just regression with some decision function (boundary)
- even plain classification methods are a constrained regression (e.g. kNN)

## daml-08-02-pca.ipynb 18:50-19:30

- unsupervised learning, we have no y vector telling us expected results
- dimensionality reduction, PCA finds directions of max variance
- talk just a little about eigenvectors and eigenvalues calculation
- eigenfaces are quite entertaining, there are 2914 dimensions, one per pixel
- the photos are from around 2000s, when privacy laws were not as strict
- PCA has only fit, transform and inverse\_transform; no predict
- the digits dataset fails the PCA linearity, i.e. is not linear at all

## pause 19:30-19:40

## daml-08-03-tsne.ipynb 19:40-20:00

- manifold technique, i.e. non linear transformation
- tSNE is very stochastic, produces different results
- no inverse transform, it is originally a visualization technique

## daml-08-04-kmeans.ipynb 20:00-20:20

- expectation maximization is quite common in ML
- apart from k-means there's also DBSCAN and hierarchical clustering techniques
- pretty much all other clustering techniques do not scale well!
- run the examples a couple of times
- silhouette analysis and cluster inertia
- digits again, explain that we will try to find what digits are
- fit\_transform is fit then transform, fit\_predict is the same story
- without knowing what digits were k-means gives a good estimate
- as with regularization, there are diffferent ways of defining distances

## daml-08-05-exercises-ul.ipynb 20:20-20:30

- explain that we will be trying to use tSNE preprocessing on digits
- the rest of the exercise is a copy paste from the lecture

