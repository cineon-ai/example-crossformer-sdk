from cineon_format import CineonData
from pytest import fixture

from example_crossformer_sdk import CrossformerModel


@fixture(scope="session")
def data() -> CineonData:
    return CineonData.from_csv("data/example.csv")

@fixture(scope="session")
def crossformer() -> CrossformerModel:
    return CrossformerModel("model")