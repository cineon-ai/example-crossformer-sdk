import python_template
from typeguard import typechecked


@typechecked
def test_hello():
    python_template.hello()


@typechecked
def test_version():
    python_template.__version__
