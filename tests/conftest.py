from cineon_format import CineonData
from pytest import fixture


@fixture(scope="session")
def data() -> CineonData:
    return CineonData.from_csv("data/example.csv")
