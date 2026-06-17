from cineon_format import CineonData
from cineon_sdk.crossformer_binary_sdk import CrossformerBinarySDK
from numpy import ndarray


class CrossformerModel:
    """
    A wrapper around CrossformerBinarySDK, to provide type hints to users.
    """

    def __init__(self, model_path: str):
        self.model = CrossformerBinarySDK()
        self.model.load(model_path)

    def run(self, data: list[CineonData]) -> ndarray:
        return self.model.run(data)

    def preprocess(self, data: list[CineonData]) -> tuple[ndarray, ndarray]:
        return self.model.preprocess(data)

    def forward(self, features: ndarray, mask: ndarray) -> ndarray:
        return self.model.forward(features, mask)

    def is_valid(self):
        return self.model.is_valid()

if __name__ == "__main__":
    model = CrossformerModel("model")
    data = CineonData.from_csv("data/example.csv")
    
    features, masks = model.preprocess([data])
    print(model.forward(features, masks))