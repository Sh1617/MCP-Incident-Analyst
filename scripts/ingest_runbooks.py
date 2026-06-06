import sys
from pathlib import Path

# Add project root to Python path
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from backend.app.vectorstore.chroma_client import chroma_manager


def ingest_runbooks():

    runbook_dir = ROOT / "runbooks"

    if not runbook_dir.exists():
        print("Runbooks directory not found")
        return

    count = 0

    for file in runbook_dir.glob("*.md"):

        text = file.read_text(
            encoding="utf-8"
        )

        chroma_manager.collection.add(
            documents=[text],
            ids=[file.stem]
        )

        count += 1

        print(f"Ingested: {file.name}")

    print(f"\nSuccessfully ingested {count} runbook(s)")


if __name__ == "__main__":
    ingest_runbooks()