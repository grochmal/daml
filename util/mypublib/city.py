#!/usr/bin/env python

from .nbops import ClearNotebook, CopyFile, SoftLink


BUILD = {}

BUILD['lecture01'] = [
ClearNotebook(
    'nb/da/introduction.ipynb',
    'pub/city/01-python-jupyter/daml-01-01-introduction.ipynb'),
ClearNotebook(
    'nb/da/resources-city.ipynb',
    'pub/city/01-python-jupyter/daml-01-02-resources.ipynb'),
ClearNotebook(
    'nb/jupyter/notebook-basics.ipynb',
    'pub/city/01-python-jupyter/daml-01-03-notebook-basics.ipynb'),
ClearNotebook(
    'nb/jupyter/notebook-code.ipynb',
    'pub/city/01-python-jupyter/daml-01-04-notebook-code.ipynb'),
ClearNotebook(
    'nb/jupyter/jupyter-exercises-1.ipynb',
    'pub/city/01-python-jupyter/daml-01-05-jupyter-exercises-1.ipynb'),
#pub/city/01-python-jupyter/daml-01-06-jupyter-exercises-1-solutions.ipynb
ClearNotebook(
    'nb/da/pydata-primer.ipynb',
    'pub/city/01-python-jupyter/daml-01-07-pydata-primer.ipynb'),
ClearNotebook(
    'nb/da/python-exercises.ipynb',
    'pub/city/01-python-jupyter/daml-01-08-python-exercises.ipynb'),
#pub/city/01-python-jupyter/daml-01-09-python-exercises-solutions.ipynb
ClearNotebook(
    'nb/jupyter/notebook-magic.ipynb',
    'pub/city/01-python-jupyter/daml-01-10-notebook-magic.ipynb'),
ClearNotebook(
    'nb/jupyter/jupyter-exercises-2.ipynb',
    'pub/city/01-python-jupyter/daml-01-11-jupyter-exercises-2.ipynb'),
#pub/city/01-python-jupyter/daml-01-12-jupyter-exercises-solutions-2.ipynb
]

BUILD['lecture02'] = [
ClearNotebook(
    'nb/numpy/numpy-basics.ipynb',
    'pub/city/02-numpy/daml-02-01-numpy-basics.ipynb'),
ClearNotebook(
    'nb/numpy/numpy-operations.ipynb',
    'pub/city/02-numpy/daml-02-02-numpy-operations.ipynb'),
ClearNotebook(
    'nb/numpy/randomness.ipynb',
    'pub/city/02-numpy/daml-02-03-randomness.ipynb'),
ClearNotebook(
    'nb/numpy/numpy-exercises.ipynb',
    'pub/city/02-numpy/daml-02-04-numpy-exercises.ipynb'),
#pub/city/02-numpy/daml-02-05-numpy-exercises-solutions.ipynb
ClearNotebook(
    'nb/numpy/random-walk.ipynb',
    'pub/city/02-numpy/daml-02-06-random-walk.ipynb'),
SoftLink(
    'nb/numpy/1d-array.svg',
    'pub/city/02-numpy/daml-02-extra-1d-array.svg'),
SoftLink(
    'nb/numpy/2d-array.svg',
    'pub/city/02-numpy/daml-02-extra-2d-array.svg'),
SoftLink(
    'nb/numpy/3d-array.svg',
    'pub/city/02-numpy/daml-02-extra-3d-array.svg'),
SoftLink(
    'nb/numpy/agg-axis-0.svg',
    'pub/city/02-numpy/daml-02-extra-agg-axis-0.svg'),
SoftLink(
    'nb/numpy/agg-axis-1.svg',
    'pub/city/02-numpy/daml-02-extra-agg-axis-1.svg'),
SoftLink(
    'nb/numpy/agg-axis-none.svg',
    'pub/city/02-numpy/daml-02-extra-agg-axis-none.svg'),
SoftLink(
    'nb/numpy/broadcast-axis.svg',
    'pub/city/02-numpy/daml-02-extra-broadcast-axis.svg'),
SoftLink(
    'nb/numpy/broadcast-simple.svg',
    'pub/city/02-numpy/daml-02-extra-broadcast-simple.svg'),
SoftLink(
    'nb/numpy/memory-usage.svg',
    'pub/city/02-numpy/daml-02-extra-memory-usage.svg'),
SoftLink(
    'nb/numpy/slice-1-select.svg',
    'pub/city/02-numpy/daml-02-extra-slice-1-select.svg'),
SoftLink(
    'nb/numpy/slice-2-all-values.svg',
    'pub/city/02-numpy/daml-02-extra-slice-2-all-values.svg'),
SoftLink(
    'nb/numpy/slice-3-slice-both.svg',
    'pub/city/02-numpy/daml-02-extra-slice-3-slice-both.svg'),
SoftLink(
    'nb/numpy/slice-4-step.svg',
    'pub/city/02-numpy/daml-02-extra-slice-4-step.svg'),
SoftLink(
    'nb/numpy/slice-5-step-both.svg',
    'pub/city/02-numpy/daml-02-extra-slice-5-step-both.svg'),
]

BUILD['lecture03'] = [
ClearNotebook(
    'nb/matplotlib/plotting-basics.ipynb',
    'pub/city/03-matplotlib/daml-03-01-plotting-basics.ipynb'),
ClearNotebook(
    'nb/matplotlib/reference.ipynb',
    'pub/city/03-matplotlib/daml-03-02-reference.ipynb'),
ClearNotebook(
    'nb/matplotlib/stat-plots.ipynb',
    'pub/city/03-matplotlib/daml-03-03-stat-plots.ipynb'),
ClearNotebook(
    'nb/matplotlib/extras.ipynb',
    'pub/city/03-matplotlib/daml-03-04-extras.ipynb'),
ClearNotebook(
    'nb/matplotlib/matplotlib-exercises.ipynb',
    'pub/city/03-matplotlib/daml-03-05-matplotlib-exercises.ipynb'),
#pub/city/03-matplotlib/daml-03-06-matplotlib-exercises-solutions.ipynb
]

BUILD['lecture04'] = [
ClearNotebook(
    'nb/pandas/pandas-intro.ipynb',
    'pub/city/04-pandas/daml-04-01-pandas-intro.ipynb'),
ClearNotebook(
    'nb/pandas/pandas-database-operations.ipynb',
    'pub/city/04-pandas/daml-04-02-database-operations.ipynb'),
ClearNotebook(
    'nb/pandas/pandas-time-series.ipynb',
    'pub/city/04-pandas/daml-04-03-pandas-time-series.ipynb'),
ClearNotebook(
    'nb/pandas/pandas-exercises.ipynb',
    'pub/city/04-pandas/daml-04-04-pandas-exercises.ipynb'),
#pub/city/04-pandas/daml-04-06-pandas-exercises-solutions.ipynb
SoftLink(
    'data/fremont-bridge.csv',
    'pub/city/04-pandas/daml-04-extra-fremont-bridge.csv'),
]

BUILD['lecture05'] = [
ClearNotebook(
    'nb/stats/stats-basics.ipynb',
    'pub/city/05-data-analytics/daml-05-01-stats-basics.ipynb'),
ClearNotebook(
    'nb/stats/stats-exercises.ipynb',
    'pub/city/05-data-analytics/daml-05-02-stats-exercises.ipynb'),
#pub/city/05-data-analytics/daml-05-03-stats-exercises-solutions.ipynb
ClearNotebook(
    'nb/seaborn/seaborn-plots.ipynb',
    'pub/city/05-data-analytics/daml-05-04-seaborn.ipynb'),
ClearNotebook(
    'nb/seaborn/seaborn-exercises.ipynb',
    'pub/city/05-data-analytics/daml-05-05-seaborn-exercises.ipynb'),
#pub/city/05-data-analytics/daml-05-06-seaborn-exercises-solutions.ipynb
CopyFile(
    'nb/da/die-hard.ipynb',
    'pub/city/05-data-analytics/daml-05-07-die-hard.ipynb'),
SoftLink(
    'nb/da/wikipedia-die-hard-cast.png',
    'pub/city/05-data-analytics/daml-05-extra-wikipedia-die-hard-cast.png'),
SoftLink(
    'nb/da/wikipedia-vcard-pane.png',
    'pub/city/05-data-analytics/daml-05-extra-wikipedia-vcard-pane.png'),
SoftLink(
    'nb/da/wikipedia-hidden-bday.png',
    'pub/city/05-data-analytics/daml-05-extra-wikipedia-hidden-bday.png'),
]

BUILD['lecture06'] = [
ClearNotebook(
    'nb/ml/machine-learning-intro.ipynb',
    'pub/city/06-sklearn-validation/daml-06-01-machine-learning.ipynb'),
ClearNotebook(
    'nb/ml/monte-carlo.ipynb',
    'pub/city/06-sklearn-validation/daml-06-02-monte-carlo.ipynb'),
ClearNotebook(
    'nb/sklearn/sklearn-intro.ipynb',
    'pub/city/06-sklearn-validation/daml-06-03-sklearn-intro.ipynb'),
]

BUILD['lecture07'] = [
ClearNotebook(
    'nb/ml/supervised-learning-summary.ipynb',
    'pub/city/07-fe-and-regularization/daml-07-01-supervised-learning.ipynb'),
ClearNotebook(
    'nb/sklearn/regularization-and-linear-regression.ipynb',
    'pub/city/07-fe-and-regularization/daml-07-02-regularization-lr.ipynb'),
ClearNotebook(
    'nb/sklearn/feature-engineering-and-naive-bayes.ipynb',
    'pub/city/07-fe-and-regularization/daml-07-03-fe-and-naive-bayes.ipynb'),
ClearNotebook(
    'nb/sklearn/exercises-regression.ipynb',
    'pub/city/07-fe-and-regularization/daml-07-04-exercises-regr.ipynb'),
#pub/city/07-fe-and-regularization/daml-07-05-exercises-regr-solutions.ipynb
ClearNotebook(
    'nb/sklearn/exercises-classification.ipynb',
    'pub/city/07-fe-and-regularization/daml-07-06-exercises-clas.ipynb'),
#pub/city/07-fe-and-regularization/daml-07-07-exercises-clas-solutions.ipynb
ClearNotebook(
    'nb/ml/least-squares.ipynb',
    'pub/city/07-fe-and-regularization/daml-07-extra-least-squares.ipynb'),
SoftLink(
    'data/stopwords-en.txt',
    'pub/city/07-fe-and-regularization/daml-07-extra-stopwords-en.txt'),
]

BUILD['lecture08'] = [
ClearNotebook(
    'nb/ml/classification-vs-regression.ipynb',
    'pub/city/08-pca-and-clustering/daml-08-01-clas-vs-regr.ipynb'),
ClearNotebook(
    'nb/sklearn/pca.ipynb',
    'pub/city/08-pca-and-clustering/daml-08-02-pca.ipynb'),
ClearNotebook(
    'nb/sklearn/tsne.ipynb',
    'pub/city/08-pca-and-clustering/daml-08-03-tsne.ipynb'),
ClearNotebook(
    'nb/sklearn/kmeans.ipynb',
    'pub/city/08-pca-and-clustering/daml-08-04-kmeans.ipynb'),
ClearNotebook(
    'nb/sklearn/exercises-unsupervised-learning.ipynb',
    'pub/city/08-pca-and-clustering/daml-08-05-exercises-ul.ipynb'),
#pub/city/08-pca-and-clustering/daml-08-06-exercises-ul-solutions.ipynb
]

BUILD['lecture09'] = [
ClearNotebook(
    'nb/sklearn/svms.ipynb',
    'pub/city/09-svms-and-random-forests/daml-09-01-svms.ipynb'),
ClearNotebook(
    'nb/sklearn/scaling-and-ensembles.ipynb',
    'pub/city/09-svms-and-random-forests/daml-09-02-scale-and-ensemble.ipynb'),
ClearNotebook(
    'nb/skimage/image-features.ipynb',
    'pub/city/09-svms-and-random-forests/daml-09-03-image-features.ipynb'),
ClearNotebook(
    'nb/joblib/model-persistence.ipynb',
    'pub/city/09-svms-and-random-forests/daml-09-04-model-persistence.ipynb'),
ClearNotebook(
    'nb/ml/real-world.ipynb',
    'pub/city/09-svms-and-random-forests/daml-09-05-real-world.ipynb'),
SoftLink(
    'data/rembrandt-tulp.png',
    'pub/city/09-svms-and-random-forests/daml-09-extra-rembrant-tulp.png'),
]

BUILD['lecture10'] = [
ClearNotebook(
    'nb/ml/online-learning.ipynb',
    'pub/city/10-online-and-anns/daml-10-01-online-learning.ipynb'),
ClearNotebook(
    'nb/sklearn/perceptron.ipynb',
    'pub/city/10-online-and-anns/daml-10-02-perceptron.ipynb'),
ClearNotebook(
    'nb/sklearn/neural-networks.ipynb',
    'pub/city/10-online-and-anns/daml-10-03-neural-networks.ipynb'),
ClearNotebook(
    'nb/ml/ann-architectures.ipynb',
    'pub/city/10-online-and-anns/daml-10-04-ann-architectures.ipynb'),
ClearNotebook(
    'nb/ml/what-next.ipynb',
    'pub/city/10-online-and-anns/daml-10-05-what-next.ipynb'),
SoftLink(
    'nb/ann/perceptron-activation.svg',
    'pub/city/10-online-and-anns/daml-10-extra-perceptron-activation.svg'),
SoftLink(
    'nb/ann/perceptron-xor.svg',
    'pub/city/10-online-and-anns/daml-10-extra-perceptron-xor.svg'),
SoftLink(
    'nb/ann/ann.svg',
    'pub/city/10-online-and-anns/daml-10-extra-ann.svg'),
]

