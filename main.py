import argparse
from viewer import config, Viewer


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pattern', default=config.DEFAULT_PATTERN,
                        help='Path to the initial pattern.')
    parser.add_argument('-i', '--iterations', type=int,
                        default=config.DEFAULT_ITERATIONS,
                        help='Number of iterations to perform.')
    parser.add_argument('-f', '--fps', type=int,
                        default=config.FPS,
                        help='Frames per seconds to render.')

    args = parser.parse_args()

    Viewer(args.pattern, args.iterations, args.fps).run()
