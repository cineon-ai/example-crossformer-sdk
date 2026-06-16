import argparse
import os

from genbadge import Badge

import test_binary_sdk

DEFAULT_BADGE_FILEPATH = os.path.join("badges", "version.svg")

parser = argparse.ArgumentParser()
parser.add_argument("--output-file", type=str, default=DEFAULT_BADGE_FILEPATH)
args = parser.parse_args()

b = Badge(left_txt="version", right_txt=str(test_binary_sdk.__version__), color="green")
b.write_to(args.output_file, use_shields=False)
