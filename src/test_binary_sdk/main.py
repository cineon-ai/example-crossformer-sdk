from cineon_format import CineonData
from crossformer_binary_sdk.binary_sdk import BinarySDK
from numpy import ndarray


class CrossformerModel:
    """
    A wrapper around BinarySDK, to provide type hints to users.
    """

    def __init__(self, model_path: str):
        self.model = BinarySDK()
        self.model.load(model_path)

    def run(self, data: list[CineonData]) -> ndarray:
        return self.model.run(data)

    def preprocess(self, data: list[CineonData]) -> tuple[ndarray, ndarray]:
        return self.model.preprocess(data)

    def forward(self, features: ndarray, mask: ndarray) -> ndarray:
        return self.model.forward(features, mask)

    def is_valid(self):
        return self.model.is_valid()
