from pathlib import Path

def get_input_from_file(path: str) -> str:
    with Path(path).open() as f:
        return [line.replace("\n", "") for line in f.readlines()]