# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none, because the grader can't
> read it.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Week 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

I chose the campus_life corpa. The campus_life has posts about student life. The corpus has 88 documents of 1–3 paragraphs each. Each document/post in campus_life is self-contained, it has all the relevant and related information for each topic (Ex: The health centre's hours and counseling. Or the "Laundry in Old Brewhouse"). The useful or key information is usually found in a single sentence or very few sentences. The topics include administration, advising, course, dining, health, housing, money/job, study groups/library, transit, etc. 

## Chunking Strategy

**Chunk size:** 
Chunk by splitting per sentences (approx. 5-6 sentences maxiumum, 500-600 characters for now).

**Overlap:** 
1 sentence - (approx. 60-65 characters for now).

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

 The total content in a document often contains only 1-3 setences which captures the whole advice and each sentence usually contains a very-specific, key or useful information about the document's topic. The whole advice/information content in each document is completely dedicated to the same specific topic.


## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: admin_add_drop_deadline.txt#0  `` — produced by: chunker.py::split_documents``

```
======================================================================
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: course_biol_160_workload.txt#0  `` — produced by: chunker.py::split_documents``

```
======================================================================
Chunk 2  |  source: course_biol_160_workload.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Workload for BIOL 160 Cell Biology

People keep asking so: 9 to 11 hours a week, the heaviest first-year course by reputation. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 3** — source: course_phys_130.txt#0 `` — produced by: chunker.py::split_documents``

```
======================================================================
Chunk 3  |  source: course_phys_130.txt#0  |  produced by: chunker.py::split_documents
======================================================================
PHYS 130 Mechanics

Just finished a year in this building. Format is lecture with a compulsory lab that meets fortnightly. Assessment: three midterms, no final, plus a lab practical. Not curved, but the lowest midterm is dropped.

Expect 7 hours a week, plus 3 on lab weeks.

The one piece of advice: the lab practical is worth 20% and almost nobody prepares for it.
```

**Chunk 4** — source: dining_verrill_street_grill_followup.txt#0 `` — produced by: chunker.py::split_documents``

```
======================================================================
Chunk 4  |  source: dining_verrill_street_grill_followup.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Re: Verrill Street Grill

Adding to what people have said about Verrill Street Grill. The wait figure of up to 30 minutes on Friday evenings matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: one register, so the queue is a single line no matter how busy. Nobody tells you this at orientation.
```

**Chunk 5** — source: housing_morrow_house.txt#1 `` — produced by: chunker.py::split_documents``

```
======================================================================
Chunk 5  |  source: housing_morrow_house.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Morrow House — what it's actually like

The bad: known damp problem on the ground floor; two rooms were taken offline in 2024.

Laundry costs $1.50 wash, $1.25 dry, coin or card. On noise: loud until about 1am on weekends, no enforced quiet hours.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**

> I got my test results for my CS210 class yesterday and I wanna grade appeal. Should I submit my appeal to the department?
  (best distance 0.373, cutoff 0.6)

**Answer:**

```

No, you should not submit your appeal directly to the department. A grade appeal must start with the instructor and be raised within fifteen days of the grade posting; skipping the instructor step will result in the appeal being returned. 

Source: `admin_grade_appeals.txt`

Sources retrieved: admin_grade_appeals.txt, course_cs_210.txt, course_cs_210_exams.txt, course_stat_150.txt, course_stat_150_exams.txt

```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
|  I need a quite place to focus and study especially during the nights before exams. What are some the available suitable places in the campus? and provide the information. | yes | best distance 0.592 |
| I need to find an on-campus job where there's preferrbaly good pay as well as enough free time for myself to study. What kinds of jobs suit my requirements? | Yes | 0.494 |
| I'm taking CS340 course and worried about the workload and stress. What's the realistic expectation and requirements of study time and workload for this course overall? | Yes | 0.343 |
| What are the operating hours for the health centre? | Yes | 0.284 |
| I got my test results for my CS210 class yesterday and I wanna grade appeal. Should I submit my appeal to the department? | Yes | 0.373 |
|What is the capital of Mongolia?|No| 0.825 |
|How do I change the oil in a diesel engine?|No| 0.934 |
|Who won the 1994 World Cup?|No| 0.886 |
|What is the recommended dosage of ibuprofen for a headache?|No| 0.844 |
|How do I write a for loop in Rust?|No| 0.896 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->


**1.**

I asked Claude to write the chunking function for split_documents based on
my strategy (group by paragraph, cap at 5-6 sentences, 1-sentence overlap).
The first version it gave me only kept a document's title/heading in the
*first* chunk of a split document so when a document like
housing_morrow_house.txt split into two chunks, the second chunk started with "The bad: known damp problem on the ground floor..." with no indication of which building it was even about. I caught this by comparing it against another chunking approach I'd written myself, which did repeat the heading on every chunk, and asked Claude to merge that fix into my sentence-based version. Without that, a retrieved chunk from a split document would've been
unanswerable on its own exactly the "could someone answer a question using
only this" test the brief asks for.

**2.**

I asked Claude to pressure-test my five acceptance criteria before I
committed them. It found two real problems I'd missed: criterion 4 said "at
most 5 full sentences" per chunk, but when it actually counted sentences
across all 88 of my documents, 25 of them (28%) run 6-7 sentences meaning
that cap would fail on real data.
I raised the chunking cap to match. Separately, my criterion 5 talked about "2
rare-topic/paraphrased questions" without saying which 2 of my 5 test
questions that meant, which made it untestable as written nobody could
actually run the check from the sentence alone. I fixed this by giving the concrete example.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Week 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     week 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk shape (≤7-8 sentences, one topic) | every chunk | 96/96, 8/8 | same | same | MET |
| 5. Rare-topic/paraphrased (Q1 + Q4) | 2 of 2 | 2/2 | 2/2 | 2/2 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

Test outputs for each criteria:  
**Criterion 1** (`store.py::search`) :  study_library_hours.txt chunk retrieved for Q1 contains "2am," "10pm," "third floor" all three facts, confirmed by reading the source document directly.  

**Criterion 2** (`generate.py::answer_from_chunks`): every one of 15 outputs (5 questions × 3 runs) ended with an explicit "Source: ..." line. Example from results/run_2026-09-23_1841_before.md:
"No, you should not submit your appeal directly to the department... Source: `admin_grade_appeals.txt`"
  

**Criterion 3** (`gate.py::check`) :  from results/run_2026-09-23_1841_before.md: refused 5 of 5, distances 0.825–0.934, all above the 0.7 cutoff. 
  iteria 4 - about chunk shape  .
  
**Criterion 4: about chunk shapes: ** 
 
  
 ```  
python app.py chunks -n 8
(myenv) PS C:\Users\ashaik  
\Desktop\codepath\AI201\ai201-project1-unofficial-guide-starter-v2026> python app.py chunks -n 8
96 chunks total. Showing 8, spread across the corpus.


======================================================================
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

======================================================================
Chunk 2  |  source: admin_study_abroad.txt#0  |  produced by: chunker.py::split_documents
======================================================================
On the study abroad

Applications open in October for the following academic year. The financial aid package travels with you, which is the single most misunderstood fact about the programme — most students assume it doesn't and rule themselves out.

======================================================================
Chunk 3  |  source: course_cs_340_exams.txt#0  |  produced by: chunker.py::split_documents
======================================================================
CS 340 Databases — assessment

One midterm and a final, both open-book. Lightly curved, usually two or three points.

Start the term project in week three, not week eight; everyone learns this the hard way.

======================================================================
Chunk 4  |  source: course_math_220_exams.txt#0  |  produced by: chunker.py::split_documents
======================================================================
MATH 220 Linear Algebra — assessment

Two midterms and a cumulative final. Curved to a b- median.

The problem sets are the course; the lectures make sense afterwards rather than during.

======================================================================
Chunk 5  |  source: dining_north_kitchen.txt#0  |  produced by: chunker.py::split_documents
======================================================================
North Kitchen

Second-year here. Wait times: none, it seats 60 and is rarely more than half full. The thing worth going for is the rotating regional menu, which changes fortnightly and is ambitious. The thing to know is that closed all summer and during reading week.

Hours are 11:00am to 7:00pm weekdays. Costs one meal swipe, or $13.00 cash.

======================================================================
Chunk 6  |  source: housing_aldridge_hall.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Aldridge Hall — what it's actually like

The bad: the elevator is out roughly one week per semester.

Laundry costs $1.75 wash, $1.50 dry, card only. On noise: quiet floors on 3 and 4 are genuinely enforced.

======================================================================
Chunk 7  |  source: housing_innisfree_hall.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Innisfree Hall — what it's actually like

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.

======================================================================
Chunk 8  |  source: housing_tamsin_court.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Tamsin Court — what it's actually like

The bad: the most expensive tier by a wide margin, and isolating if you're new.

Laundry costs in-unit washer-dryer. On noise: quiet, structurally — concrete floors between units.

For each one, ask: could someone answer a question using only this,
without reading what came before or after?  
```
  

  
**Criterion 5** :  Q4 (health_center.txt, only health-tagged doc in the corpus) and Q1 (paraphrased as "quiet place to focus" vs. the document's actual wording "silent... enforced") both retrieved chunks containing the correct answer  
  
## Verdicts
  


  
<!-- MET or MISSED for each of the five, against the target you wrote last
     week — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | Checked the actual chunk text for all 5 questions against the source documents directly  4 of 5 have a single chunk containing the complete expected answer. Q3 (CS340 workload) is a borderline case: the workload numbers and the "start in week 3" advice landed in two different retrieved chunks rather than one, so no single chunk has the full answer — I'm counting that as not meeting the strict reading of "one chunk contains the answer," which still leaves 4/5. |
| 2 | Every answer names a source | MET | All 15 outputs (5 questions × 3 runs) named a source explicitly. |
| 3 | Gate stops out-of-corpus questions | MET | 5 of 5 refused, well clear of the 0.7 cutoff (closest was 0.825). |
| 4 | Chunk shape | MET | Checked sentence count across all 96 chunks (not just a sample, since the criterion says "every chunk") — max was 6, none exceeded the 7-8 cap. Separately sampled 8 chunks for the "one topic" check by eye — all 8 stayed on one subject, though the North Kitchen chunk (6 sentences covering wait times, menu, hours, and cost) is the densest case and the one I'd watch if I tightened this later. |
| 5 | Rare-topic/paraphrased | MET | Both named questions (Q4, Q1) retrieved a chunk containing the correct fact. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

  
I missed none of my five criteria. But there are two things worth mentioning that cause flaws/faults:

- Criterion 4's cap ("at most 7-8 sentences") is looser than my chunker's limit of 6, so it was never at risk of failing. It doesn't test the criteria..
- Generation stage: the CS340 answer (Q3) left out the "start the project in week 3" advice in 3 of 3 runs, even though the chunk containing it (course_cs_340_exams.txt) was retrieved every time. Retrieval was identical across runs, so the model had the fact in the sources but didn't mention it. The prompt also tells it to "be brief," which likely competes with combining facts from two chunks.
# The Improvement

**What I changed:**
  

**What I changed:** In generate.py's GROUNDING_INSTRUCTION, I replaced "Be brief" with an instruction to include every relevant fact from all documents that contain part of the answer.  
**Why I picked it:** It targets the generation-stage diagnosis above (Q3   
<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk shape (≤7-8 sentences, one topic) | every chunk | 96/96, 8/8 | same | same | MET |
| 5. Rare-topic/paraphrased (Q1 + Q4) | 2 of 2 | 2/2 | 2/2 | 2/2 | MET |
| Extra: Q3 includes the week-3 advice | n/a | 1/1 | 1/1 | 1/1 | MET 0/3 before, 3/3 after |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->
  

Yes, for what it targeted. Q3 now includes the advice to start project in 3rd week,,  in 3 of 3 runs (0 of 3 before), and Q1 now includes the 2am hours in 3 of 3 (2 of 3 before). No criterion changed, since none of the five measures generation completeness.  
  
Costs: output tokens roughly doubled (930 to 1,939 across the same 15 calls), and a few answers added true but off-question detail (Q1 run 2 added textbook reserve, Q2 run 2 added the work-study aid rule). I changed two prompt lines at
once, so I can't say which did the work, and Q1's improvement could be noise.  
## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

  
No criterion was missed, so nothing is broken against my own targets. A few weaknesses that still remain are:  
(1) I have no scorer, so completeness is judged by reading;  
(2) answers are longer and sometimes drift off-question; 

(3) criterion 3's five out-of-scope questions are all far from my corpus (best distances 0.825+), so passing them says little about near-miss questions.  

## What I'd Do Differently
  <!-- Knowing what you know now — which of your five criteria would you write      differently, and why?     Milestone 5. -->   

- Criterion 4: set the cap to 6, my chunker's real limit, so it can fail.
- Criterion 1: it measures retrieval, but my real problem was generation   expectsfrom  or advices from the sources  
- Criterion 3: add near-miss questions, such as campus topics my documents - Criterion 5: "2 of 2" is too small a sample to mean much.