from cineon_format import CineonData
from typeguard import typechecked

import example_crossformer_sdk
from example_crossformer_sdk import CrossformerModel


@typechecked
def test_version():
    assert example_crossformer_sdk.__version__


@typechecked
def test_model_load(crossformer: CrossformerModel):
    assert crossformer is not None


@typechecked
def test_model_preprocess(crossformer: CrossformerModel, data: CineonData):
    features, mask = crossformer.preprocess([data])
    assert features is not None
    assert mask is not None
