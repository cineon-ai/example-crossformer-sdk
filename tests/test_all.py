import test_binary_sdk
from typeguard import typechecked


@typechecked
def test_version():
    test_binary_sdk.__version__
