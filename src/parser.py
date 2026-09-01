from pathlib import Path


# Find the main Magic Juice project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Location of the knowledge files
KNOWLEDGE_DIR = BASE_DIR / "knowledge"


def load_knowledge():
    """
    Automatically reads all .txt files inside the knowledge folder.
    """

    if not KNOWLEDGE_DIR.exists():
        raise FileNotFoundError(
            f"Knowledge folder not found: {KNOWLEDGE_DIR}"
        )

    knowledge_files = sorted(KNOWLEDGE_DIR.glob("*.txt"))

    if not knowledge_files:
        raise FileNotFoundError(
            "No .txt files found in the knowledge folder."
        )

    sections = []

    for file_path in knowledge_files:
        content = file_path.read_text(
            encoding="utf-8"
        ).strip()

        if content:
            sections.append(
                f"===== {file_path.name.upper()} =====\n"
                f"{content}"
            )

    if not sections:
        raise ValueError("All knowledge files are empty.")

    return "\n\n".join(sections)


if __name__ == "__main__":
    knowledge = load_knowledge()

    print("MAGIC JUICE KNOWLEDGE BASE")
    print("=" * 50)
    print(knowledge)