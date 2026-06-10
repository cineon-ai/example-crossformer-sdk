import argparse
import os

from genbadge import Badge

import python_template

DEFAULT_BADGE_FILEPATH = os.path.join("badges", "version.svg")

parser = argparse.ArgumentParser()
parser.add_argument("--output-file", type=str, default=DEFAULT_BADGE_FILEPATH)
args = parser.parse_args()

b = Badge(left_txt="version", right_txt=str(python_template.__version__), color="green")
b.write_to(args.output_file, use_shields=False)
