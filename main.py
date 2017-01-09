from solver import solver
import argparse

parser = argparse.ArgumentParser(description="Pogress Pie Facebook Hacker Cup")
parser.add_argument("--import", dest="filename", help="Import file", required=True)
parser.add_argument("--rad", dest="rad", help="Rad", type=int, default=50)

args = parser.parse_args()


ifile = open(args.filename, "r")
lines = list(map(lambda line: list(map(lambda n: int(n), line.split(" "))), ifile.read().splitlines()[1:]))

for index, result in enumerate(solver(args.rad, lines), start=1):
  print("Case #%d: %s" % (index, result))

