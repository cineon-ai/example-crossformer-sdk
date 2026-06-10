from typeguard import typechecked


@typechecked
def hello() -> None:
    print("Hello from python-template!")
