import argparse

from genbadge import Badge

# A map between code-complexity scores and colours
COLOUR_MAP = {
    "A": "green",
    "B": "yellow",
    "C": "orange",
    "D": "red",
    "E": "darkred",
    "F": "black",
}

# Get the filepath from the command-line
parser = argparse.ArgumentParser()
parser.add_argument("--input-file", help="Path to the complexity report file")
parser.add_argument("--output-file", help="Path to save the generated badge")
args = parser.parse_args()
input_path = args.input_file
output_path = args.output_file

# Read the complexity report
with open(input_path, "r") as f:
    complexity = f.read().strip()

# Extract the code complexity score
parts = complexity.split("Average complexity:")

if len(parts) < 2 or not parts[-1].strip():
    raise RuntimeError("Could not find 'Average complexity:' in Radon output")

complexity_score = parts[-1].strip()[0]
print(f"Score: {complexity_score}")

# Create the badge and save
b = Badge(
    left_txt="complexity",
    right_txt=complexity_score,
    color=COLOUR_MAP[complexity_score],
)
b.write_to(output_path, use_shields=False)
