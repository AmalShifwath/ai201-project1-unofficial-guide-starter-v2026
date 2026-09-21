"""
Your test questions.

Milestone 2 asks you to write five questions your system should be able to
answer from your corpus, specific enough to have a right answer.

  ✗ "What are good dining halls?"          — no right answer
  ✓ "What do students say about wait times at Commons during lunch?"

Fill in `QUESTIONS` below. `expects` is a word or short phrase you'd expect a
correct answer to contain — you'll use it in week 2 when you build a scorer,
and having written it now means you decided what "correct" meant before you saw
any results.

`OUT_OF_SCOPE` holds five questions your documents clearly don't cover. You
need these in Milestone 4 to find where your relevance cutoff belongs, and
again in week 2, where `run_eval.py` runs them through the gate and writes what
happened into your run log — that's the evidence for criterion 3.

Swap them for your own if you like. Keep five of them either way: criterion 3
names a target of "4 of 5", and four of three is not a thing.
"""

'''
question 1: I need a quite place to focus and study especially during the nights before exams. What are some the available suitable places in the campus? and provide the information.
Answer in study_library_hours.txt
Should contain: Library - open until 2am during term, until 10pm during reading week. The third floor is silent and enforced.

question 2: I need to find an on-campus job where there's preferrbaly good pay as well as enough free time for myself to study. What kinds of jobs suit my requirements?
Answer in money_jobs.txt
Should contain: all jobs have similar pay, desk jobs have freedom and time while physical/manual jobs like dining doesn't.

question 3: I'm taking CS340 course and worried about the workload and stress. What's the realistic expectation and requirements of study time and workload for this course overall?
Answer in course_cs_340.txt, course_cs_340_exams.txt, course_cs_340_workload.txt
Should contain: 6 hrs/week workload in the begninning and about 15hrs/week in the last 3 weeks. The first month is loaded because of getting used to the format. Start the project in week 3 instead of 8.

question 4: What are the operating hours for the health centre?
Answer in health_center.txt
Should contain: 8am to 11am walk-in and anytime oustide of those hours is per appointment basis.

question 5: I got my test results for my CS210 class yesterday and I wanna grade appeal. Should I submit my appeal to the department?
Answer in admin_grade_appeals.txt
Should contain: 
'''


QUESTIONS = [
    # {"question": "...", "expects": "..."},
    {"question": "I need a quite place to focus and study especially during the nights before exams. What are some the available suitable places in the campus? and provide the information.",
     "expects": "library, 2 am, 2am, 10pm during reading week, third floor"},
    {"question": "I need to find an on-campus job where there's preferrbaly good pay as well as enough free time for myself to study. What kinds of jobs suit my requirements?",
     "expects": "similar pay, same pay, no difference in pay, desk"},
    {"question": "I'm taking CS340 course and worried about the workload and stress. What's the realistic expectation and requirements of study time and workload for this course overall?",
     "expects": "6 hours, six hours, 15 hours, fifteen hours, Start the project in week 3, Start the project in week three"},
    {"question": "What are the operating hours for the health centre?",
     "expects": "8am to 11am, walk-in, appointment"},
    {"question": "I got my test results for my CS210 class yesterday and I wanna grade appeal. Should I submit my appeal to the department?",
     "expects": "instructor, 15 days, fifteen days"},
]

# Questions from a different world entirely. Your gate should refuse all five.
#
# There are five of these because criterion 3 in criteria.md names a target of
# "at least 4 of 5" — you need five things to try before you can report 4 of 5.
# `run_eval.py` runs these through retrieval and the gate on every eval and
# records what happened, so criterion 3 has evidence in the run log alongside
# the others. They cost no model calls: a refusal never reaches the model.
OUT_OF_SCOPE = [
    "What is the capital of Mongolia?",
    "How do I change the oil in a diesel engine?",
    "Who won the 1994 World Cup?",
    "What is the recommended dosage of ibuprofen for a headache?",
    "How do I write a for loop in Rust?",
]


def answered() -> list[dict]:
    """The questions you've actually filled in."""
    return [q for q in QUESTIONS if q.get("question", "").strip()]
