from pathlib import Path
import shutil
import argparse
import sys

sys.setrecursionlimit(2000)
def parse_folder(source_path: Path, new_folder: Path = Path("dist")) -> None:
    """Recursively parse the source directory and copy files to a new directory,"""
    if not new_folder.exists():
        new_folder.mkdir(parents=True, exist_ok=True)

    for element in source_path.iterdir():
        if element.is_dir():
            parse_folder(element, new_folder)
        elif element.is_file():
            try:
                file_extension = element.name.split('.')[-1].lower() or 'else'
                folder_name = f"{file_extension}_files"
                target_folder = new_folder / folder_name

                if not target_folder.exists():
                    target_folder.mkdir(parents=True, exist_ok=True)

                target_path = target_folder / element.name
                shutil.copy2(element, target_path)
            except Exception as e:
                print(f"⚠️ Error copying file {element}: {e}")

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Recursively copy files to a new directory sorted by file extension.")
    parser.add_argument("source", type=Path, help="Source directory to parse")
    parser.add_argument("destination", type=Path, nargs='?', default=Path("dist"), help="Destination directory to copy files to")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    source = args.source
    destination = args.destination

    if not source.exists() or not source.is_dir():
        print(f"❌ Source directory '{source}' does not exist or is not a directory.")
        sys.exit(1)

    print(f"📂 Starting to parse folder: {source}")
    parse_folder(source, destination)
    print(f"✅ Files have been sorted and copied to {destination}")
