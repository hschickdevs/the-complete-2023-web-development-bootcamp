from pathlib import Path

if __name__ == "__main__":
    for i in range(41):
        path = Path(f"section-{i + 1}")
        if not path.exists():
            path.mkdir()