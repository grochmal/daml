## daml-09-01-svms.ipynb 18:30-19:20

- quickly go over all methods we went through, and compare them
- dim reduction: pca - most basic, always try
- dim reduction: manifold - may not make sense, use to supplement pca
- clustering: k-means - easy to use, can be batched with some changes
- clustering: dbscan - a variant of the k-means with max distance
- clustering: hierarchical clustering - a different useful technique
- clustering: most other techniques do not scale well
- regression: ordinary least squares and polynomials - better then expected
- regression: LARS, OMP - specific hihg-dimensional cases
- regression: Huber, RANSAC - robust to outliers
- regression: time series has ARIMA like models
- classification: naive bayes - great for a baseline
- classification: knn - simple, still useful for complex structures
- classification: logistic regression - binary classifier
- classification - and more to come
- and never forget to check your data
- svms are binary classifiers
- naive separation, line through the middle
- margin, though a hyperplane, quadratic programming
- svc is support vector classifier
- had margin and soft margin, C hyperparameter
- non-linear separation: kernels (polynomial, radial basis function)
- kernel trick, during a dual problem we get k(x).k(y)
- olivietti faces is ordered, use KFold
- we now have a really good deal of hyperparameters to search (grid search)
- random search, which one is better?  does it matter?
- multi-class: OVO and OVA/OVR
- real problem: train, test and validation sets, do not overfit hyperparamters
- if test and validation scores are similar we have good generalization
- the final model performs alright

## pause 19:20-19:30

## daml-09-02-scale-and-ensemble.ipynb 19:30-20:00

- wine dataset
- plot dimensions, difficult to separate
- pca shows that this should be easy, but it isn't
- pca is actually showing a difference in feature scaling
- proline and magnesium have crazy values
- standard scaler: mean 0 and std 1, vs normal scaler: between o and 1
- quick on decision trees, cheap for multi-label
- decision trees have a big tendency to overfit
- simple bagging, often good enough
- random forest, one of the best classifiers
- ada boost, super performance but difficult to parallelize
- quick over the iris dataset

## daml-09-03-image-features.ipynb 20:00-20:15

- feature extraction, other options for video and audio
- moviepy, imageio, scipu.io.wavfile
- scipy.io even has matlab conversion procedures
- y coordinate top to bottom (standard for images)
- hsv, lab vs rgb
- filters for edges
- bluring before segmentation

## daml-09-04-model-persistence.ipynb 20:15-20:25

- pickle is python serialization, it is pretty old
- joblib does considerably better
- if you need to work with python 2 today, you're in trouble

## daml-09-05-real-world.ipynb 20:25-20:30

- do this one for as long as it takes
- this is the summary of the important things in this course
- it is completely fine to drag this one onto the next lecture

