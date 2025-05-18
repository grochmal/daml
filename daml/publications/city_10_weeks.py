from daml.pub import (
    Directory,
    ClearNotebook,
    CopyFile,
    ZipDirectory,
    build_lecture,
)


BASE = "city_10_weeks"
LECTURE_01 = Directory(f"{BASE}/01-python-jupyter")
LECTURE_02 = Directory(f"{BASE}/02-numpy")
LECTURE_03 = Directory(f"{BASE}/03-matplotlib")
LECTURE_04 = Directory(f"{BASE}/04-pandas")
LECTURE_05 = Directory(f"{BASE}/05-data-analysis")
LECTURE_06 = Directory(f"{BASE}/06-machine-learning")
LECTURE_07 = Directory(f"{BASE}/07-reg-and-fe")
LECTURE_08 = Directory(f"{BASE}/08-unsupervised-learning")
LECTURE_09 = Directory(f"{BASE}/09-supervised-learning")
LECTURE_10 = Directory(f"{BASE}/10-online-learning")
BUILD = {}

BUILD["lecture_01"] = [
    ClearNotebook(
        "apx-introduction-city.ipynb",
        "daml-01-01-introduction.ipynb",
        LECTURE_01,
    ),
    ClearNotebook(
        "apx-resources-city-online.ipynb",
        "daml-01-02-resources.ipynb",
        LECTURE_01,
    ),
    ClearNotebook(
        "py-introduction-daml.ipynb",
        "daml-01-03-daml.ipynb",
        LECTURE_01,
    ),
    ClearNotebook(
        "py-notebook-basics.ipynb",
        "daml-01-04-notebook-basics.ipynb",
        LECTURE_01,
    ),
    ClearNotebook(
        "py-notebook-code.ipynb",
        "daml-01-05-notebook-code.ipynb",
        LECTURE_01,
    ),
    ClearNotebook(
        "py-jupyter-exercises-1.ipynb",
        "daml-01-06-jupyter-exercises-1.ipynb",
        LECTURE_01,
    ),
    ClearNotebook(
        "py-pydata-primer.ipynb",
        "daml-01-07-pydata-primer.ipynb",
        LECTURE_01,
    ),
    ClearNotebook(
        "py-exercises.ipynb",
        "daml-01-08-python-exercises.ipynb",
        LECTURE_01,
    ),
    ClearNotebook(
        "py-notebook-magic.ipynb",
        "daml-01-09-notebook-magic.ipynb",
        LECTURE_01,
    ),
    ClearNotebook(
        "py-jupyter-exercises-2.ipynb",
        "daml-01-10-jupyter-exercises-2.ipynb",
        LECTURE_01,
    ),
    CopyFile("py-bob-ross.svg", LECTURE_01),
    CopyFile("py-cats.svg", LECTURE_01),
    CopyFile("py-chuck-norris.svg", LECTURE_01),
    CopyFile("py-ctrl-enter.svg", LECTURE_01),
    CopyFile("py-global-state.svg", LECTURE_01),
    CopyFile("py-jupyter-lab-interface.svg", LECTURE_01),
    CopyFile("py-magic.svg", LECTURE_01),
    CopyFile("py-python-anaconda.svg", LECTURE_01),
    ZipDirectory(LECTURE_01),
]

BUILD["lecture_02"] = [
    ClearNotebook(
        "np-numpy-basics.ipynb",
        "daml-02-01-numpy-basics.ipynb",
        LECTURE_02,
    ),
    ClearNotebook(
        "np-operations.ipynb",
        "daml-02-02-numpy-operations.ipynb",
        LECTURE_02,
    ),
    ClearNotebook(
        "np-randomness.ipynb",
        "daml-02-03-randomness.ipynb",
        LECTURE_02,
    ),
    ClearNotebook(
        "np-exercises.ipynb",
        "daml-02-04-numpy-exercises.ipynb",
        LECTURE_02,
    ),
    ClearNotebook(
        "np-array-algebra.ipynb",
        "daml-02-05-array-algebra.ipynb",
        LECTURE_02,
    ),
    ClearNotebook(
        "np-random-walk.ipynb",
        "daml-02-06-random-walk.ipynb",
        LECTURE_02,
    ),
    CopyFile("np-1d-array.svg", LECTURE_02),
    CopyFile("np-2d-array.svg", LECTURE_02),
    CopyFile("np-3d-array.svg", LECTURE_02),
    CopyFile("np-agg-axis-0.svg", LECTURE_02),
    CopyFile("np-agg-axis-1.svg", LECTURE_02),
    CopyFile("np-agg-axis-none.svg", LECTURE_02),
    CopyFile("np-argsort.svg", LECTURE_02),
    CopyFile("np-bookshelf.svg", LECTURE_02),
    CopyFile("np-broadcast-axis.svg", LECTURE_02),
    CopyFile("np-broadcast-simple.svg", LECTURE_02),
    CopyFile("np-broadcast-tv.svg", LECTURE_02),
    CopyFile("np-brownie.svg", LECTURE_02),
    CopyFile("np-dice.svg", LECTURE_02),
    CopyFile("np-memory-usage.svg", LECTURE_02),
    CopyFile("np-pointer.svg", LECTURE_02),
    CopyFile("np-slice-1-select.svg", LECTURE_02),
    CopyFile("np-slice-2-all-values.svg", LECTURE_02),
    CopyFile("np-slice-3-slice-both.svg", LECTURE_02),
    CopyFile("np-slice-4-step.svg", LECTURE_02),
    CopyFile("np-slice-5-step-both.svg", LECTURE_02),
    ZipDirectory(LECTURE_02),
]

BUILD["lecture_03"] = [
    ClearNotebook(
        "plt-plotting-basics.ipynb",
        "daml-03-01-plotting-basics.ipynb",
        LECTURE_03,
    ),
    ClearNotebook(
        "plt-reference.ipynb",
        "daml-03-02-reference.ipynb",
        LECTURE_03,
    ),
    ClearNotebook(
        "plt-3d-plots.ipynb",
        "daml-03-03-3d-plots.ipynb",
        LECTURE_03,
    ),
    ClearNotebook(
        "plt-stat-plots.ipynb",
        "daml-03-04-stat-plots.ipynb",
        LECTURE_03,
    ),
    ClearNotebook(
        "plt-exercises.ipynb",
        "daml-03-05-matplotlib-exercises.ipynb",
        LECTURE_03,
    ),
    ClearNotebook(
        "plt-engines.ipynb",
        "daml-03-06-engines.ipynb",
        LECTURE_03,
    ),
    CopyFile("plt-dots-3d.svg", LECTURE_03),
    CopyFile("plt-engine.svg", LECTURE_03),
    CopyFile("plt-inches.svg", LECTURE_03),
    CopyFile("plt-iris.svg", LECTURE_03),
    CopyFile("plt-table.svg", LECTURE_03),
    ZipDirectory(LECTURE_03),
]

BUILD["lecture_04"] = [
    ClearNotebook(
        "pd-pandas-intro.ipynb",
        "daml-04-01-pandas-intro.ipynb",
        LECTURE_04,
    ),
    ClearNotebook(
        "pd-data-frames.ipynb",
        "daml-04-02-data-frames.ipynb",
        LECTURE_04,
    ),
    ClearNotebook(
        "pd-database-operations.ipynb",
        "daml-04-03-database-operations.ipynb",
        LECTURE_04,
    ),
    ClearNotebook(
        "pd-dimensions.ipynb",
        "daml-04-04-dimensions.ipynb",
        LECTURE_04,
    ),
    ClearNotebook(
        "pd-exercises.ipynb",
        "daml-04-05-pandas-exercises.ipynb",
        LECTURE_04,
    ),
    ClearNotebook(
        "pd-time-series.ipynb",
        "daml-04-06-time-series.ipynb",
        LECTURE_04,
    ),
    ClearNotebook(
        "pd-metro.ipynb",
        "daml-04-07-metro.ipynb",
        LECTURE_04,
    ),
    CopyFile("pd-bat.svg", LECTURE_04),
    CopyFile("pd-british-isles.svg", LECTURE_04),
    CopyFile("pd-cardiff.svg", LECTURE_04),
    CopyFile("pd-metro.svg", LECTURE_04),
    CopyFile("pd-parchment.svg", LECTURE_04),
    CopyFile("pd-road.svg", LECTURE_04),
    CopyFile("pd-metro-traffic.csv", LECTURE_04),
    ZipDirectory(LECTURE_04),
]

BUILD["lecture_05"] = [
    ClearNotebook(
        "da-stats-basics.ipynb",
        "daml-05-01-stats-basics.ipynb",
        LECTURE_05,
    ),
    ClearNotebook(
        "da-distributions.ipynb",
        "daml-05-02-distributions.ipynb",
        LECTURE_05,
    ),
    ClearNotebook(
        "da-correlation.ipynb",
        "daml-05-03-correlation.ipynb",
        LECTURE_05,
    ),
    ClearNotebook(
        "da-stats-exercises.ipynb",
        "daml-05-04-stats-exercises.ipynb",
        LECTURE_05,
    ),
    ClearNotebook(
        "da-why-python.ipynb",
        "daml-05-05-why-python.ipynb",
        LECTURE_05,
    ),
    ClearNotebook(
        "da-die-hard.ipynb",
        "daml-05-06-die-hard.ipynb",
        LECTURE_05,
    ),
    CopyFile("da-bell.svg", LECTURE_05),
    CopyFile("da-christmas.svg", LECTURE_05),
    CopyFile("da-cosinus.svg", LECTURE_05),
    CopyFile("da-die-hard.svg", LECTURE_05),
    CopyFile("da-gauss-euler.svg", LECTURE_05),
    CopyFile("da-std-full.svg", LECTURE_05),
    CopyFile("da-std-sample.svg", LECTURE_05),
    CopyFile("da-weibull.svg", LECTURE_05),
    CopyFile("da-wikipedia-die-hard-cast.png", LECTURE_05),
    CopyFile("da-wikipedia-hidden-bday.png", LECTURE_05),
    CopyFile("da-wikipedia-vcard-pane.png", LECTURE_05),
    CopyFile("da-die-hard.csv", LECTURE_05),
    ZipDirectory(LECTURE_05),
]

BUILD["lecture_06"] = [
    ClearNotebook(
        "skl-ml-intro.ipynb",
        "daml-06-01-ml-intro.ipynb",
        LECTURE_06,
    ),
    ClearNotebook(
        "skl-monte-carlo.ipynb",
        "daml-06-02-monte-carlo.ipynb",
        LECTURE_06,
    ),
    ClearNotebook(
        "skl-sklearn.ipynb",
        "daml-06-03-sklearn-intro.ipynb",
        LECTURE_06,
    ),
    ClearNotebook(
        "skl-is-it-right.ipynb",
        "daml-06-04-is-it-right.ipynb",
        LECTURE_06,
    ),
    ClearNotebook(
        "skl-labels.ipynb",
        "daml-06-05-labels.ipynb",
        LECTURE_06,
    ),
    ClearNotebook(
        "skl-exercises.ipynb",
        "daml-06-06-exercises.ipynb",
        LECTURE_06,
    ),
    CopyFile("skl-dover-castle.svg", LECTURE_06),
    CopyFile("skl-knn-2d.svg", LECTURE_06),
    CopyFile("skl-labels.svg", LECTURE_06),
    CopyFile("skl-model-call.svg", LECTURE_06),
    CopyFile("skl-monte-carlo.svg", LECTURE_06),
    CopyFile("skl-neighbours.svg", LECTURE_06),
    CopyFile("skl-pi-area.svg", LECTURE_06),
    CopyFile("skl-pi-euclid.svg", LECTURE_06),
    CopyFile("skl-terminator.svg", LECTURE_06),
    ZipDirectory(LECTURE_06),
]

BUILD["lecture_07"] = [
    ClearNotebook(
        "fe-fallacies.ipynb",
        "daml-07-01-fallacies.ipynb",
        LECTURE_07,
    ),
    ClearNotebook(
        "fe-regression.ipynb",
        "daml-07-02-regression.ipynb",
        LECTURE_07,
    ),
    ClearNotebook(
        "fe-full-road-trip.ipynb",
        "daml-07-03-full-road-trip.ipynb",
        LECTURE_07,
    ),
    ClearNotebook(
        "fe-regularization.ipynb",
        "daml-07-04-regularization.ipynb",
        LECTURE_07,
    ),
    ClearNotebook(
        "fe-text-features.ipynb",
        "daml-07-05-text-features.ipynb",
        LECTURE_07,
    ),
    ClearNotebook(
        "fe-high-dimensions.ipynb",
        "daml-07-06-high-dimensions.ipynb",
        LECTURE_07,
    ),
    ClearNotebook(
        "fe-evaluation-exercises.ipynb",
        "daml-07-07-evaluation-exercises.ipynb",
        LECTURE_07,
    ),
    CopyFile("fe-driver.svg", LECTURE_07),
    CopyFile("fe-formula-one.svg", LECTURE_07),
    CopyFile("fe-fox.svg", LECTURE_07),
    CopyFile("fe-newsgroups.svg", LECTURE_07),
    CopyFile("fe-quick-brown-fox.svg", LECTURE_07),
    CopyFile("fe-thomas-bayes.svg", LECTURE_07),
    CopyFile("fe-turn.svg", LECTURE_07),
    CopyFile("fe-van-gogh.svg", LECTURE_07),
    CopyFile("fe-station16405-1945.csv", LECTURE_07),
    CopyFile("fe-stopwords-en.txt", LECTURE_07),
    ZipDirectory(LECTURE_07),
]

BUILD["lecture_08"] = [
    ClearNotebook(
        "ul-ml-catalogue.ipynb",
        "daml-08-01-ml-catalogue.ipynb",
        LECTURE_08,
    ),
    ClearNotebook(
        "ul-pca.ipynb",
        "daml-08-02-pca.ipynb",
        LECTURE_08,
    ),
    ClearNotebook(
        "ul-noise-reduction.ipynb",
        "daml-08-03-noise-reduction.ipynb",
        LECTURE_08,
    ),
    ClearNotebook(
        "ul-non-linearity.ipynb",
        "daml-08-04-non-linearity.ipynb",
        LECTURE_08,
    ),
    ClearNotebook(
        "ul-tsne.ipynb",
        "daml-08-05-tsne.ipynb",
        LECTURE_08,
    ),
    ClearNotebook(
        "ul-kmeans.ipynb",
        "daml-08-06-kmeans.ipynb",
        LECTURE_08,
    ),
    ClearNotebook(
        "ul-clusters.ipynb",
        "daml-08-07-clusters.ipynb",
        LECTURE_08,
    ),
    ClearNotebook(
        "ul-hierarchical.ipynb",
        "daml-08-08-hierarchical.ipynb",
        LECTURE_08,
    ),
    ClearNotebook(
        "ul-exercises.ipynb",
        "daml-08-09-exercises.ipynb",
        LECTURE_08,
    ),
    CopyFile("ul-andromeda.svg", LECTURE_08),
    CopyFile("ul-bush.svg", LECTURE_08),
    CopyFile("ul-godel.svg", LECTURE_08),
    CopyFile("ul-gosset.svg", LECTURE_08),
    CopyFile("ul-hilbert.svg", LECTURE_08),
    CopyFile("ul-moon.svg", LECTURE_08),
    CopyFile("ul-orange-man-bad.svg", LECTURE_08),
    CopyFile("ul-write.svg", LECTURE_08),
    ZipDirectory(LECTURE_08),
]

BUILD["lecture_09"] = [
    ClearNotebook(
        "sl-class-vs-regr.ipynb",
        "daml-09-01-class-vs-regr.ipynb",
        LECTURE_09,
    ),
    ClearNotebook(
        "sl-trees.ipynb",
        "daml-09-02-trees.ipynb",
        LECTURE_09,
    ),
    ClearNotebook(
        "sl-ensembles.ipynb",
        "daml-09-03-ensembles.ipynb",
        LECTURE_09,
    ),
    ClearNotebook(
        "sl-margins.ipynb",
        "daml-09-04-margins.ipynb",
        LECTURE_09,
    ),
    ClearNotebook(
        "sl-people.ipynb",
        "daml-09-05-people.ipynb",
        LECTURE_09,
    ),
    ClearNotebook(
        "sl-complete-procedure.ipynb",
        "daml-09-06-complete-procedure.ipynb",
        LECTURE_09,
    ),
    ClearNotebook(
        "sl-data-scaling.ipynb",
        "daml-09-07-data-scaling.ipynb",
        LECTURE_09,
    ),
    ClearNotebook(
        "sl-model-persistence.ipynb",
        "daml-09-08-model-persistence.ipynb",
        LECTURE_09,
    ),
    ClearNotebook(
        "sl-exercises.ipynb",
        "daml-09-09-exercises.ipynb",
        LECTURE_09,
    ),
    CopyFile("sl-bow-tie.svg", LECTURE_09),
    CopyFile("sl-crane.svg", LECTURE_09),
    CopyFile("sl-europe.svg", LECTURE_09),
    CopyFile("sl-jupiter.svg", LECTURE_09),
    CopyFile("sl-major-oak.svg", LECTURE_09),
    CopyFile("sl-ovo-ova.svg", LECTURE_09),
    CopyFile("sl-stallone.svg", LECTURE_09),
    CopyFile("sl-stew.svg", LECTURE_09),
    CopyFile("sl-tony-blair.svg", LECTURE_09),
    CopyFile("sl-wine.svg", LECTURE_09),
    ZipDirectory(LECTURE_09),
]

BUILD["lecture_10"] = [
    ClearNotebook(
        "ol-real-world.ipynb",
        "daml-10-01-real-world.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "ol-perceptron.ipynb",
        "daml-10-02-perceptron.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "ol-online-learning.ipynb",
        "daml-10-03-online-learning.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "ol-forest-cover.ipynb",
        "daml-10-04-forest-cover.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "ol-neural-networks.ipynb",
        "daml-10-05-neural-networks.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "ol-ann-concepts.ipynb",
        "daml-10-06-ann-concepts.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "ol-ann-usage.ipynb",
        "daml-10-07-ann-usage.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "ol-image-features.ipynb",
        "daml-10-08-image-features.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "ol-autoencoders.ipynb",
        "daml-10-09-autoencoders.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "ol-ann-architectures.ipynb",
        "daml-10-10-ann-architectures.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "fut-what-next.ipynb",
        "daml-10-11-what-next.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "apx-flew-over-nlp.ipynb",
        "daml-10-12-flew-over-nlp.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "apx-q-learning.ipynb",
        "daml-10-13-q-learning.ipynb",
        LECTURE_10,
    ),
    ClearNotebook(
        "apx-attention.ipynb",
        "daml-10-14-attention.ipynb",
        LECTURE_10,
    ),
    CopyFile("ol-activation-functions.svg", LECTURE_10),
    CopyFile("ol-ann-full.svg", LECTURE_10),
    CopyFile("ol-ann-matrix-form.svg", LECTURE_10),
    CopyFile("ol-columbo.svg", LECTURE_10),
    CopyFile("ol-earth.svg", LECTURE_10),
    CopyFile("ol-forest-aspen.svg", LECTURE_10),
    CopyFile("ol-forest-cottonwood.svg", LECTURE_10),
    CopyFile("ol-forest-douglas-fir.svg", LECTURE_10),
    CopyFile("ol-forest-krummholz.svg", LECTURE_10),
    CopyFile("ol-forest-lodgepole-pine.svg", LECTURE_10),
    CopyFile("ol-forest-ponderosa-pine.svg", LECTURE_10),
    CopyFile("ol-forest-spruce-fir.svg", LECTURE_10),
    CopyFile("ol-forest-willow.svg", LECTURE_10),
    CopyFile("ol-gradient-direction.svg", LECTURE_10),
    CopyFile("ol-gradient.svg", LECTURE_10),
    CopyFile("ol-hamburger.svg", LECTURE_10),
    CopyFile("ol-masks.svg", LECTURE_10),
    CopyFile("ol-neurons.svg", LECTURE_10),
    CopyFile("ol-olympics.svg", LECTURE_10),
    CopyFile("ol-perceptron-activation.svg", LECTURE_10),
    CopyFile("ol-perceptron-decision.svg", LECTURE_10),
    CopyFile("ol-perceptron-xor.svg", LECTURE_10),
    CopyFile("ol-photo.svg", LECTURE_10),
    CopyFile("ol-rembrandt.svg", LECTURE_10),
    CopyFile("ol-rembrandt-tulp.png", LECTURE_10),
    ZipDirectory(LECTURE_10),
]


if __name__ == "__main__":
    for k, v in BUILD.items():
        print(f"BUILB: {k}")
        build_lecture(v)
