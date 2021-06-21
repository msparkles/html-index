import argparse
from pathlib import Path

from lib import icon_manager
from lib.assets import Assets
from lib.index import Index
from lib.writer import Writer


def main():
    parser = argparse.ArgumentParser(description='Generates index.html files for file indexing.')

    parser.add_argument(
        'path', type=str,
        help='the path to the directory you want to index'
    )
    parser.add_argument(
        '--title', type=str,
        default="Index of #DIR",
        help='change the title of the index. (`#DIR`: the directory path)'
    )
    parser.add_argument(
        '--parent_dir', type=str,
        default="parent directory",
        help='change the name of the "parent directory" button in the index. (default: "parent directory")'
    )
    parser.add_argument(
        '--filename', type=str,
        default="File Name",
        help='change the name of the field "File Name" in the table. (default: "File Name")'
    )
    parser.add_argument(
        '--size', type=str,
        default="Size",
        help='change the name of the field "Size" in the table. (default: "Size")'
    )
    parser.add_argument(
        '--modified', type=str,
        default="Size",
        help='change the name of the field "Last Modified" in the table. (default: "Last Modified")'
    )

    args = parser.parse_args()

    # init
    root = Path(__file__).parent
    assets = Assets(root.joinpath('assets'))

    icon_manager.read_icons(assets)

    # actual program
    path = Path(args.path)
    index = Index.read_from_path(path)
    writer = Writer(
        assets,
        args.title, args.parent_dir, args.filename, args.size, args.modified
    )
    writer.write_deep([index])


if __name__ == "__main__":
    main()
