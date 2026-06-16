from cineon_format import CineonData
from typeguard import typechecked

import test_binary_sdk
from test_binary_sdk import CrossformerModel


@typechecked
def test_version():
    assert test_binary_sdk.__version__


@typechecked
def test_model_load():
    model = CrossformerModel("model")
    assert model is not None


@typechecked
def test_model_preprocess(data: CineonData):
    model = CrossformerModel("model")
    features, mask = model.preprocess([data])
