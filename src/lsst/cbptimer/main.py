import argparse
import importlib.metadata


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version", action="version", version=f"{parser.prog} {importlib.metadata.version('lsst-cbptimer')}"
    )
    parser.parse_args()
    parser.print_help()
