from cineon_format import CineonData
from cineon_sdk.crossformer_binary_sdk import CrossformerBinarySDK
import numpy as np
from numpy import ndarray

RESULTS_DICT = {
    0: "Low",
    1: "Medium",
    2: "High"
}


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

    # Load the model and data
    model = CrossformerModel("model")
    data = CineonData.from_csv("data/example_4.csv")

    # Preprocess the data and run the model
    features, masks = model.preprocess([data])
    logits = model.forward(features, masks)
    print("logits:\n", logits)
    print()

    # Convert logits to probabilities using the sigmoid function
    # Note that these are not normalized probabilities across classes
    probs = 1./(1 + np.exp(-logits))
    print("probabilities:\n", probs)
    print()

    # Get the index of the maximum probability for each sample
    results = np.argmax(probs, axis=1)
    print("results:\n", results)
    print()

    # Map the results to their corresponding labels using the results_dict
    predictions = [RESULTS_DICT[r] for r in results]
    print("predictions:\n", predictions)
    print()