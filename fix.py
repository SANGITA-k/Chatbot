# Fix 1: "scholarship" keyword triggers "scholarship" in greeting_keywords? No.
# "scholarship for merit" — "merit" is in scholarship keywords. Let's debug.
import sys
sys.path.insert(0, '.')
from responses import FAQ_DATA, GREETING_KEYWORDS
from utils import clean_input, find_best_match, is_greeting

q = "scholarship for merit"
print("clean:", clean_input(q))
print("is_greeting:", is_greeting(q, GREETING_KEYWORDS))
match = find_best_match(q, FAQ_DATA)
print("match:", match["topic"] if match else None)
