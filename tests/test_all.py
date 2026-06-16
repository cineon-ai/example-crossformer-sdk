from typeguard import typechecked

import test_binary_sdk


@typechecked
def test_version():
    test_binary_sdk.__version__
