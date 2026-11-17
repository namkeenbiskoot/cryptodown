"""
Command-line interface for cnslab.
Allows generating lab program files directly from the terminal without internet.
"""

import argparse
import sys
from pathlib import Path
from .programs import (
    PROGRAMS,
    write_program,
    create_all,
    list_programs,
    get_code,
    create_sample_image,
    normalize_key,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="cnslab",
        description="Offline CNS Lab Program Generator for Lab Exams",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  cnslab 1                 Create '1.py' (Caesar Cipher)
  cnslab 7a                Create '7a.py' (AES ECB)
  cnslab all               Generate all lab programs (1.py - 11.py)
  cnslab list              Show all available lab programs
  cnslab 8 -o rsa.py       Write RSA code to custom filename 'rsa.py'
  cnslab 6 --print         Print DES code to terminal stdout
  cnslab image             Create a dummy 'image.png' for stego testing
        """,
    )

    parser.add_argument(
        "program",
        nargs="?",
        default=None,
        help="Lab number or alias (e.g. 1, 2, 3, 4, 5, 6, 7a, 7b, 8, 9, 10, 11, 'all', 'list', 'image')",
    )
    parser.add_argument(
        "-o", "--output",
        dest="filename",
        default=None,
        help="Custom output filename (e.g. -o solution.py)",
    )
    parser.add_argument(
        "-d", "--dir",
        dest="dest_dir",
        default=None,
        help="Target directory (defaults to current directory)",
    )
    parser.add_argument(
        "-p", "--print",
        action="store_true",
        help="Print code to stdout instead of writing to a file",
    )
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        default=True,
        help="Force overwrite existing files (default: True)",
    )

    args = parser.parse_args()

    # If no argument given, print help or list
    if not args.program:
        list_programs()
        return

    arg_lower = args.program.strip().lower()

    if arg_lower in ("list", "-l", "--list"):
        list_programs()
        return

    if arg_lower in ("all", "*"):
        create_all(dest_dir=args.dest_dir, overwrite=args.force)
        return

    if arg_lower in ("image", "sample_image", "img"):
        out_fn = args.filename or "image.png"
        create_sample_image(filename=out_fn, dest_dir=args.dest_dir)
        return

    try:
        if args.print:
            code = get_code(arg_lower)
            print(code, end="")
        else:
            write_program(
                arg_lower,
                filename=args.filename,
                dest_dir=args.dest_dir,
                overwrite=args.force,
            )
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
