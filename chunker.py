"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from itertools import groupby

from dataclasses import dataclass

import config
from ingest import Document

@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in week 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split documents into chunks. ⚠️ REPLACE THE BODY OF THIS IN MILESTONE 3.

    Right now it just calls the fallback. That is the plain, generic behaviour
    the brief is talking about.

    When you write your own strategy, set `produced_by` to
    "chunker.py::split_documents" so your README's Sample Chunks section names
    the right function. `app.py chunks` prints that string for you.

    Things worth thinking about before you write any code:
      - Are your documents short posts or long guides?
      - Is the useful information in one sentence, or spread over a paragraph?
      - Would splitting on paragraph breaks keep more thoughts intact than
        splitting on a character count?
    """
    # return fallback_split(documents)

    # ── Milestone 3: sentence-based chunking ────────────────────────────────────

    '''
        Milestone 3: sentence-based chunking. Grounded in the real sentence counts
        across all 88 campus_life documents (2-7 sentences, avg ~4.2) — a cap of 6
        covers nearly every document as a single chunk and only splits the handful
        of longer housing_* posts.
        
        Fill chunks paragraph by paragraph, up to MAX_SENTENCES sentences, and
        only split inside a paragraph if that paragraph alone is too long.
        Carries the last OVERLAP_SENTENCES sentence(s) of a chunk into the next
        one when a document has to split, so a fact that leans on the sentence
        before it isn't orphaned at the seam. 
        
        The document title/heading is added at the top of every chunk a document 
        produces, so a chunk is never missing which post/document it's from.
    '''
    
    MAX_SENTENCES = 6
    OVERLAP_SENTENCES = 1

    _SENTENCE_SPLIT = re.compile(r'(?<=[.!?])\s+')

    def _sentences(paragraph: str) -> list[str]:
        """Split one paragraph into sentences, keeping punctuation attached."""
        return [s.strip() for s in _SENTENCE_SPLIT.split(paragraph.strip()) if s.strip()]


    def _paragraphs(text: str) -> list[str]:
        """Split on blank lines — where a campus_life post marks a new thought."""
        return [p.strip() for p in text.split("\n\n") if p.strip()]


    def _render(tagged_sentences: list[tuple[int, str]]) -> str:
        """Join sentences back into text, keeping paragraph breaks intact so a
        chunk reads like the source post instead of one flattened run-on."""
        out = []
        last_p = None
        for p_idx, s in tagged_sentences:
            if last_p is not None and p_idx != last_p:
                out.append("\n\n")
            elif out:
                out.append(" ")
            out.append(s)
            last_p = p_idx
        return "".join(out).strip()

    chunks: list[Chunk] = []

    for doc in documents:
        paragraphs = _paragraphs(doc.text)
        if not paragraphs:
            continue

        # First paragraph is the post's title/heading. It's excluded from the
        # sentence budget and instead repeated at the top of every chunk this
        # document produces, so a chunk is never missing which post it's from
        # — "The bad: no air conditioning" means nothing without knowing
        # which building.
        if len(paragraphs) > 1:
            heading, body_paragraphs = paragraphs[0], paragraphs[1:]
        else:
            heading, body_paragraphs = None, paragraphs

        tagged: list[tuple[int, str]] = []
        for p_idx, para in enumerate(body_paragraphs):
            for s in _sentences(para):
                tagged.append((p_idx, s))

        para_groups = [list(g) for _, g in groupby(tagged, key=lambda t: t[0])]

        current: list[tuple[int, str]] = []
        index = 0

        def flush():
            nonlocal current, index
            if not current:
                return
            body = _render(current)
            if body:
                text = f"{heading}\n\n{body}" if heading else body
                chunks.append(Chunk(
                    text=text, source=doc.source, index=index,
                    produced_by="chunker.py::split_documents",
                ))
                index += 1

        for group in para_groups:
            if current and len(current) + len(group) > MAX_SENTENCES:
                flush()
                current = current[-OVERLAP_SENTENCES:] if OVERLAP_SENTENCES else []

            if len(group) > MAX_SENTENCES:
                for item in group:
                    current.append(item)
                    if len(current) >= MAX_SENTENCES:
                        flush()
                        current = current[-OVERLAP_SENTENCES:] if OVERLAP_SENTENCES else []
            else:
                current.extend(group)

        flush()

    return chunks
    

def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
