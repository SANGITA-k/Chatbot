# =============================================================================
# responses.py
# FAQ Response Bank — College Help Desk Chatbot
# Contains all keyword patterns and corresponding answers (20 FAQs)
# =============================================================================

FAQ_DATA = [
    {
        "id": 1,
        "topic": "Admission",
        "keywords": ["apply", "admission", "enroll", "enrolment", "join", "register", "application"],
        "answer": (
            "To apply for admission:\n"
            "  1. Visit our official college website and click 'Apply Now'.\n"
            "  2. Fill in the application form with your academic details.\n"
            "  3. Upload required documents: marksheets, ID proof, passport photos.\n"
            "  4. Pay the application fee online (Rs. 500).\n"
            "The admission office reviews applications within 5-7 working days.\n"
            "For queries, email: admissions@college.edu"
        )
    },
    {
        "id": 2,
        "topic": "Fees & Payments",
        "keywords": ["fee", "fees", "payment", "pay", "tuition", "cost", "charges", "challan", "due date"],
        "answer": (
            "Fee Payment Information:\n"
            "  * Pay online via Student Portal -> Finance -> Pay Fees.\n"
            "  * Accepted modes: Net Banking, UPI, Debit/Credit Cards.\n"
            "  * Semester 1 due date: June 30\n"
            "  * Semester 2 due date: December 31\n"
            "  * Late payment penalty: Rs. 500/month.\n"
            "For receipts or queries, contact: finance@college.edu"
        )
    },
    {
        "id": 3,
        "topic": "Timetable",
        "keywords": ["timetable", "time table", "schedule", "class timing", "lecture", "slot", "when is class"],
        "answer": (
            "Your class timetable is available at:\n"
            "  Student Portal -> Academics -> My Timetable\n"
            "It is updated each semester before classes begin.\n"
            "If you notice any timetable conflicts, report them to your\n"
            "Department Coordinator within the first week of classes."
        )
    },
    {
        "id": 4,
        "topic": "Scholarships",
        "keywords": ["scholarship", "financial aid", "bursary", "merit", "stipend", "waiver"],
        "answer": (
            "Available Scholarships:\n"
            "  1. Merit Scholarship   - Top 5% of each batch -> 50% tuition waiver.\n"
            "  2. Need-Based Aid      - Family income < Rs. 3L/year -> up to 100% waiver.\n"
            "  3. Sports/Cultural     - State/national achievers -> 25% waiver.\n"
            "Apply via: Student Portal -> Finance -> Scholarships\n"
            "Last date to apply: July 15 every year."
        )
    },
    {
        "id": 5,
        "topic": "ID Card",
        "keywords": ["id card", "identity card", "college id", "student card", "identity"],
        "answer": (
            "ID Card Information:\n"
            "  * New ID cards issued during Orientation Week.\n"
            "  * For a replacement card, visit:\n"
            "    Admin Office, Block A, Room 102\n"
            "    Bring: 1 passport photo + Rs. 100 fee.\n"
            "  * Cards are ready within 3 working days."
        )
    },
    {
        "id": 6,
        "topic": "Hostel",
        "keywords": ["hostel", "accommodation", "dorm", "dormitory", "room allotment", "stay", "residential", "boarding", "hostel application"],
        "answer": (
            "Hostel Admission:\n"
            "  * Applications open every May via: Portal -> Hostel -> Apply\n"
            "  * Preference given to outstation students.\n"
            "  * Room allotment announced in July.\n"
            "  Fees per year:\n"
            "    AC Room:     Rs. 48,000 (meals included)\n"
            "    Non-AC Room: Rs. 32,000 (meals included)\n"
            "Contact: hostel.warden@college.edu"
        )
    },
    {
        "id": 7,
        "topic": "Examinations",
        "keywords": ["exam", "examination", "test", "assessment", "finals", "midterm", "hall ticket", "exam date"],
        "answer": (
            "Examination Schedule:\n"
            "  * Mid-Semester Exams: September & February\n"
            "  * End-Semester Exams: November & April\n"
            "  * Full schedule posted 4 weeks before exams:\n"
            "    Portal -> Academics -> Examinations\n"
            "  * Hall tickets available 1 week before exams.\n"
            "For exam-related issues: examcell@college.edu"
        )
    },
    {
        "id": 8,
        "topic": "Faculty Contact",
        "keywords": ["faculty", "professor", "teacher", "lecturer", "staff", "contact faculty", "instructor"],
        "answer": (
            "To contact faculty:\n"
            "  * Faculty Directory: Portal -> Academics -> Faculty Directory\n"
            "  * Email format: firstname.lastname@college.edu\n"
            "  * Office hours are posted on department notice boards.\n"
            "For urgent matters, contact the Department Office directly."
        )
    },
    {
        "id": 9,
        "topic": "Library",
        "keywords": ["library", "book", "borrow", "return", "library card", "reading", "e-library", "digital library"],
        "answer": (
            "Library Services:\n"
            "  * Hours: Monday-Saturday, 8 AM - 8 PM\n"
            "  * Borrow up to 4 books for 14 days using your college ID.\n"
            "  * E-Library (10,000+ resources): Portal -> Library -> E-Resources (24/7)\n"
            "  * Fine for late return: Rs. 5/day per book.\n"
            "Contact: library@college.edu"
        )
    },
    {
        "id": 10,
        "topic": "Wi-Fi & Internet",
        "keywords": ["wifi", "internet", "network", "wi-fi", "connection", "connect", "broadband"],
        "answer": (
            "Campus Wi-Fi:\n"
            "  * SSID: CollegeNet\n"
            "  * Login: Your Student ID + Portal Password\n"
            "  * Available across all campus buildings 24/7.\n"
            "For connectivity issues:\n"
            "  IT Help Desk - Block C, Room 201\n"
            "  Email: itsupport@college.edu"
        )
    },
    {
        "id": 11,
        "topic": "Certificates & Documents",
        "keywords": ["certificate", "bonafide", "migration", "character certificate", "transcript", "document", "letter"],
        "answer": (
            "Document Requests:\n"
            "  Apply via: Portal -> Documents -> Request Certificate\n"
            "  Available certificates:\n"
            "    - Bonafide Certificate\n"
            "    - Character Certificate\n"
            "    - Migration Certificate\n"
            "    - Official Transcripts\n"
            "  Processing time: 3-5 working days (abroad: 7-10 days).\n"
            "  Collect from Admin Office, Block A."
        )
    },
    {
        "id": 12,
        "topic": "Sports Facilities",
        "keywords": ["sports", "gym", "ground", "basketball", "football", "cricket", "swimming", "fitness"],
        "answer": (
            "Sports Facilities:\n"
            "  * Gymnasium, Cricket Ground\n"
            "  * Basketball & Badminton Courts\n"
            "  * Swimming Pool\n"
            "  All facilities are FREE for students with a valid ID.\n"
            "Register for sports teams via:\n"
            "  Sports Office (Block D) or Portal -> Activities -> Sports"
        )
    },
    {
        "id": 13,
        "topic": "Clubs & Events",
        "keywords": ["club", "society", "fest", "event", "cultural", "activity", "extracurricular", "utsav"],
        "answer": (
            "Student Clubs & Events:\n"
            "  * 30+ clubs: Coding, Drama, Debate, Music, Robotics & more.\n"
            "  * Join via: Portal -> Activities -> Clubs\n"
            "  * Annual Fest 'Utsav' is held in February.\n"
            "    Auditions open in December.\n"
            "Contact: studentcouncil@college.edu"
        )
    },
    {
        "id": 14,
        "topic": "Transport & Bus",
        "keywords": ["transport", "bus", "commute", "shuttle", "route", "pick up", "drop", "bus pass"],
        "answer": (
            "College Transport:\n"
            "  * 12 bus routes across the city.\n"
            "  * Routes & timings: Portal -> Transport\n"
            "  * Bus pass cost: Rs. 6,000/semester\n"
            "  * Apply by June 20 for Semester 1.\n"
            "  * Lost pass replacement: Rs. 200 at Transport Office."
        )
    },
    {
        "id": 15,
        "topic": "Medical & Health",
        "keywords": ["medical", "health", "sick", "doctor", "clinic", "hospital", "infirmary", "medicine", "injury"],
        "answer": (
            "Health Centre:\n"
            "  * Location: Block B, Ground Floor\n"
            "  * Hours: Monday-Saturday, 9 AM - 5 PM\n"
            "  * Free OPD consultations for all registered students.\n"
            "  * 24/7 emergency care for hostel residents.\n"
            "  * Ambulance: Ext. 1122\n"
            "Contact: healthcentre@college.edu"
        )
    },
    {
        "id": 16,
        "topic": "Portal & Login",
        "keywords": ["password", "login", "portal", "forgot password", "reset", "account", "username", "sign in"],
        "answer": (
            "Student Portal Access:\n"
            "  URL: https://portal.college.edu\n"
            "  * Forgot password? Click 'Forgot Password' and enter your registered email.\n"
            "  * Reset link arrives within 5 minutes.\n"
            "  * For account lockouts:\n"
            "    IT Help Desk - Block C, Room 201\n"
            "    Email: itsupport@college.edu"
        )
    },
    {
        "id": 17,
        "topic": "Results & Grades",
        "keywords": ["result", "marks", "grade", "cgpa", "gpa", "score", "revaluation", "recheck"],
        "answer": (
            "Exam Results:\n"
            "  * Published within 30 days of exam completion.\n"
            "  * Check at: Portal -> Academics -> Results\n"
            "  * Discrepancy? Apply for re-evaluation:\n"
            "    Portal -> Academics -> Revaluation\n"
            "    Deadline: Within 15 days of result declaration.\n"
            "    Fee: Rs. 500/subject."
        )
    },
    {
        "id": 18,
        "topic": "Attendance",
        "keywords": ["attendance", "absent", "leave", "shortage", "condonation", "proxy", "bunk"],
        "answer": (
            "Attendance Policy:\n"
            "  * Minimum 75% attendance required to appear in final exams.\n"
            "  * Check attendance: Portal -> Academics -> Attendance\n"
            "  * Medical/genuine leave: Apply through your Faculty Advisor.\n"
            "  * Condonation requests (with valid proof): Submit to Dean's Office.\n"
            "  Attendance is updated every 48 hours."
        )
    },
    {
        "id": 19,
        "topic": "Grievances & Complaints",
        "keywords": ["complaint", "grievance", "issue", "problem", "report", "concern", "feedback"],
        "answer": (
            "Grievance Redressal:\n"
            "  * Raise a complaint: Portal -> Support -> Submit Grievance\n"
            "  * Grievance cell meets every Friday.\n"
            "  * Response guaranteed within 7 working days.\n"
            "  * Urgent matters: grievance@college.edu\n"
            "  * Anonymous complaints: Suggestion boxes outside each department."
        )
    },
    {
        "id": 20,
        "topic": "Internships & Placements",
        "keywords": ["internship", "placement", "job", "recruit", "company", "campus placement", "career", "hire"],
        "answer": (
            "Placement & Internship Cell:\n"
            "  * Register at: Portal -> Placements -> Register\n"
            "  * Internship drives: January-March each year.\n"
            "  * Campus placements: August-November (final year students).\n"
            "  * Resume workshops & mock interviews offered.\n"
            "  Contact: placements@college.edu | Block E, Room 305"
        )
    },
]

# ---------------------------------------------------------------------------
# Special response sets
# ---------------------------------------------------------------------------

FALLBACK_RESPONSES = [
    "I'm sorry, I didn't quite understand that. Could you rephrase your question?",
    "I'm sorry, I don't have information on that topic. Try asking about admissions, fees, exams, or hostel.",
    "I'm sorry, that's outside my knowledge base. For detailed help, visit the Admin Office or call 1800-XXX-XXXX.",
    "I'm sorry, I couldn't match your query. Please contact the helpdesk at help@college.edu.",
]

GREETING_KEYWORDS  = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "howdy", "greetings"]
FAREWELL_KEYWORDS  = ["bye", "goodbye", "exit", "quit", "see you", "thanks bye", "tata"]
THANKS_KEYWORDS    = ["thank", "thanks", "thank you", "thx", "ty", "appreciated"]

GREETING_RESPONSE = (
    "Hello! Welcome to the College Help Desk!\n"
    "I can help you with topics like:\n"
    "  admissions, fees, timetable, scholarships, hostel,\n"
    "  exams, results, attendance, library, and much more!\n\n"
    "What would you like to know today? (type 'help' for a topic list)"
)

FAREWELL_RESPONSE = "Thank you for using the College Help Desk! Have a great day! Come back anytime."
THANKS_RESPONSE   = "You're welcome! Is there anything else I can help you with?"

HELP_RESPONSE = (
    "Here are the topics I can help you with:\n"
    + "\n".join(f"  {i+1:>2}. {faq['topic']}" for i, faq in enumerate(FAQ_DATA))
    + "\n\nJust type your question naturally and I'll find the best answer!"
)
