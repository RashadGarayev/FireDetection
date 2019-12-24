import os
import argparse
from PIL import Image
DEFAULT_SIZE = (150, 150)
def resize_image(input_dir, infile, output_dir="resized", size=DEFAULT_SIZE):
    outfile = os.path.splitext(infile)[0] + "fire"
    extension = os.path.splitext(infile)[1]
    try:
        img = Image.open(input_dir + '/' + infile)
        img = img.resize((size[0], size[1]), Image.LANCZOS)

        new_file = output_dir + "/" + outfile + extension
        img.save(new_file)
    except IOError:
        print("unable to resize image {}".format(infile))
if __name__ == "__main__":
    dir = os.getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', help='Full Input Path')
    parser.add_argument('-o', '--output_dir', help='Full Output Path')
    parser.add_argument('-w', '--width', help='Resized Width')
    parser.add_argument('-t', '--height', help='Resized Height')
    args = parser.parse_args()
    if args.input_dir:
        input_dir = args.input_dir
    else:
        input_dir = dir + '/images'
    if args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = dir + '/resized'
    if args.width and args.height:
        size = (int(args.width), int(args.height))
    else:
        size = DEFAULT_SIZE
    if not os.path.exists(os.path.join(dir, output_dir)):
        os.mkdir(output_dir)
    try:
        for file in os.listdir(input_dir):
            resize_image(input_dir, file, output_dir, size=size)
    except OSError:
        print('file not found')


