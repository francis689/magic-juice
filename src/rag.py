from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).resolve().parent.parent / "knowledge"


def load_knowledge():
    """Load all text files from the Magic Juice knowledge folder."""

    documents = []

    if not KNOWLEDGE_DIR.exists():
        raise FileNotFoundError(
            f"Knowledge folder not found: {KNOWLEDGE_DIR}"
        )

    for file_path in sorted(KNOWLEDGE_DIR.glob("*.txt")):
        content = file_path.read_text(encoding="utf-8").strip()

        if content:
            documents.append({
                "source": file_path.name,
                "content": content
            })

    return documents


def retrieve(query, documents, top_k=3):
    """Find the most relevant knowledge files."""

    query_words = set(query.lower().split())

    scored_documents = []

    for document in documents:
        content = document["content"].lower()

        score = sum(
            1
            for word in query_words
            if len(word) > 2 and word in content
        )

        if score > 0:
            scored_documents.append((score, document))

    scored_documents.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        document
        for score, document in scored_documents[:top_k]
    ]


def get_context(query, top_k=3):
    """Get relevant information from the Magic Juice knowledge base."""

    documents = load_knowledge()

    results = retrieve(
        query,
        documents,
        top_k
    )

    if not results:
        return "No relevant information was found in the Magic Juice knowledge base."

    context_parts = []

    for document in results:
        context_parts.append(
            f"Source: {document['source']}\n"
            f"{document['content']}"
        )

    return "\n\n---\n\n".join(context_parts)
