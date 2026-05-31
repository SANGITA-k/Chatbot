# College Help Desk — Rule-Based FAQ Chatbot

A beginner-level Python project demonstrating Natural Language Processing (NLP)
fundamentals through a rule-based FAQ chatbot for a college help desk scenario.

---

## Project Overview

| Field       | Detail                               |
|-------------|--------------------------------------|
| Title       | Rule-Based FAQ Chatbot               |
| Level       | Beginner                             |
| Language    | Python 3.8+                          |
| Scenario    | College Help Desk                    |
| FAQs Covered| 20 topics                            |

---

## Project Structure

```
faq-chatbot/
│
├── chatbot.py      # Main chatbot logic — conversation loop & dispatcher
├── responses.py    # All Q&A pairs / response bank (20 FAQs + specials)
├── utils.py        # Helper functions: input cleaning, matching, display
├── README.md       # This file — project documentation
└── report.pdf      # Assignment report (see report.pdf)
```

---

## Features

- **20 FAQ topics** covering every major college help desk concern
- **Natural keyword matching** — understands varied phrasings of the same question
- **Special intent detection** — greetings, farewells, gratitude, help requests
- **Graceful fallback** — randomised polite responses for unrecognised queries
- **Session logging** — auto-saves each conversation to `logs/session_<timestamp>.txt`
- **Self-test suite** — run `python chatbot.py --test` to validate all 24 test cases
- **Zero external dependencies** — uses only Python standard library

---

## FAQ Topics Covered

1. Admission & Application
2. Fees & Payments
3. Class Timetable
4. Scholarships & Financial Aid
5. Student ID Card
6. Hostel & Accommodation
7. Examinations & Hall Tickets
8. Faculty Contact
9. Library Services
10. Wi-Fi & Internet
11. Certificates & Documents
12. Sports Facilities
13. Clubs & Cultural Events
14. Transport & Bus Pass
15. Medical & Health Centre
16. Student Portal & Login
17. Exam Results & Grades
18. Attendance Policy
19. Grievances & Complaints
20. Internships & Placements

---

## How to Run

### Requirements
- Python 3.8 or higher
- No external packages needed

### Run the chatbot (normal mode)
```bash
python chatbot.py
```

### Run without session logging
```bash
python chatbot.py --nolog
```

### Run the self-test suite
```bash
python chatbot.py --test
```

---

## Sample Interaction

```
  [HelpDesk Bot]:
  Hello! Welcome to the College Help Desk!
  I can help you with topics like:
    admissions, fees, timetable, scholarships, hostel,
    exams, results, attendance, library, and much more!

  [You          ]: how do i apply for admission?

  [HelpDesk Bot]:
  To apply for admission:
    1. Visit our official college website and click 'Apply Now'.
    2. Fill in the application form with your academic details.
    3. Upload required documents: marksheets, ID proof, passport photos.
    4. Pay the application fee online (Rs. 500).
  The admission office reviews applications within 5-7 working days.
  For queries, email: admissions@college.edu

  [You          ]: what scholarships are available?

  [HelpDesk Bot]:
  Available Scholarships:
    1. Merit Scholarship   - Top 5% of each batch -> 50% tuition waiver.
    2. Need-Based Aid      - Family income < Rs. 3L/year -> up to 100% waiver.
    3. Sports/Cultural     - State/national achievers -> 25% waiver.
  Apply via: Student Portal -> Finance -> Scholarships
  Last date to apply: July 15 every year.
```

---

## How It Works

### 1. Input Cleaning (`utils.py → clean_input`)
Raw user text is normalised:
- Converted to lowercase
- Punctuation removed (except apostrophes)
- Extra whitespace collapsed

### 2. Intent Detection (`utils.py → is_greeting / is_farewell / is_thanks`)
Before FAQ matching, special intents are detected using simple keyword lists.

### 3. Keyword Matching (`utils.py → find_best_match`)
Each FAQ entry has a list of keywords. The bot scores every FAQ by counting
how many of its keywords appear in the cleaned input, and returns the
highest-scoring FAQ. If no keywords match, a fallback is returned.

### 4. Response Delivery (`chatbot.py → get_response`)
The dispatcher runs intents in priority order:
```
Farewell → Greeting → Thanks → Help → FAQ Match → Fallback
```

---

## Concepts Demonstrated

| Concept                    | Location              |
|----------------------------|-----------------------|
| String methods             | utils.py              |
| Regular expressions (re)   | utils.py              |
| Functions & modularity     | utils.py, chatbot.py  |
| Data structures (list/dict)| responses.py          |
| Loops & conditionals       | chatbot.py            |
| File I/O                   | utils.py (logger)     |
| Exception handling         | chatbot.py            |
| Module imports             | chatbot.py            |

---

## Author

Student Assignment — Rule-Based FAQ Chatbot in Python  
Course: Introduction to NLP / Python Programming  
Submitted to: Sangita Kumar  

