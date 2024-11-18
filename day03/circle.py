pi=3.141592653589793
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--radius', help='Input radius', required=True, type=int)
args = parser.parse_args()
radius=args.radius
print("The area of the circle is", pi*radius**2, "and the circumference is", 2*pi*radius,".")       