import glob

import nbformat
import pytest
from nbconvert.preprocessors import ExecutePreprocessor


@pytest.mark.parametrize("nb_path", glob.glob("notebooks/*.ipynb"))
def test_notebooks(nb_path):
    with open(nb_path) as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600)
    ep.preprocess(nb, {"metadata": {"path": "notebooks"}})
