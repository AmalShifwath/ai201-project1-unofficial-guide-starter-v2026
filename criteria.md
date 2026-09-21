# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in week 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next week costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
The questions I framed asks for a very specific information mostly present in only 1 document in within 1-3 sentences.  

<!-- e.g. "One of my questions is about a topic only two documents mention, so
     I expect that one to be hard." -->

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.


**Why this target:**
Because the answers is (and needs to be) verifiable and grounded with evidence since build_prompt() labels all the chunks. Also because every single answer to the questions about campus life asks requires for information that is specific to the campus life topics which are present only in the sources/documents (mostly 1 document or chunk).

<!-- Why all five and not four? What about your setup makes that achievable —
     or what would have to go wrong for it not to be? -->

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
This target makes sure that the generated responses are grounded in evidence documents and factual basis, and to avoid LLM's hallucinations and mis-information.
<!-- What did your distances look like when you set the cutoff in Milestone 4?
     Was there a clean gap, or did the two groups overlap? -->

---

## 4. Something about your chunks

Every chunk contains at most 7-8 full sentences and atleast 1 sentence each, and all the sentences in each chunk has specific key information is fully scoped to only one certain topic or subject.

<!-- YOU WRITE THIS ONE.

     How would you know if your chunks were the right size? Name something
     countable or observable.

     Examples of the right shape — don't copy these, they should come from
     what you actually saw in Milestone 3:
       - "At least 4 of 5 sampled chunks read as a complete thought, with no
          sentence cut in half at either end."
       - "No chunk is shorter than 200 characters, since anything below that
          in my corpus turned out to be a heading with no content under it." -->



**Why this target:**
Because almost all of the documents contain the useful or key information is usually in a single sentence or very few sentences. All the content in a single document pertains to a specific topic of information/adivce, and all of the documents are self-contained.


---

## 5. Your choice

The correct documents is retrieved even when the query asks for specific information that's rare in the documents corpus and contains the info in paraphrased wording, which makes it harder and more unlikely to match and find. Atleast 2 of 2 rare-topic/paraphrased questions retrieve the correct chunk. (ex: Q4 health center is rare;  second one is Q1)

<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. It could be about
     speed, about refusals, about a particular kind of question your corpus
     handles badly, about source attribution being correct rather than merely
     present — anything, as long as it names a number or an observable
     outcome. -->



**Why this target:**
This tests that all the key information and topics in the corpus is identified and isn't ignored/filtered/missed out even if the key information is only in a small piece of text and is rare compared to other topics of information.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     WEEK 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in week 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
