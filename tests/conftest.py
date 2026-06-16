from cineon_format import CineonData
from pytest import fixture


@fixture(scope="session")
def data() -> CineonData:
    return CineonData.from_csv("data/cineon-gd2-standardized-p001.csv")
