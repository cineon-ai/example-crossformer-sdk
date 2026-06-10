from typeguard import typechecked

import python_template


@typechecked
def test_hello():
    python_template.hello()


@typechecked
def test_version():
    python_template.__version__
