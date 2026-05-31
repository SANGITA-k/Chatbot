# =============================================================================
# utils.py
# Helper / Utility Functions — College Help Desk Chatbot
# Handles: input cleaning, keyword matching, logging, display formatting
# =============================================================================

import re
import random
import datetime


# ---------------------------------------------------------------------------
# Input Cleaning
# ---------------------------------------------------------------------------

def clean_input(text: str) -> str:
    """
    Normalise raw user input:
      - Strip leading/trailing whitespace
      - Convert to lowercase
      - Remove punctuation except apostrophes
      - Collapse multiple spaces
    """
    text = text.strip().lower()
    text = re.sub(r"[^\w\s']", " ", text)   # remove punctuation (keep apostrophes)
    text = re.sub(r"\s+", " ", text)         # collapse whitespace
    return text


def tokenize(text: str) -> list:
    """Split cleaned text into individual word tokens."""
    return text.split()


# ---------------------------------------------------------------------------
# Keyword Matching
# ---------------------------------------------------------------------------

def find_best_match(user_input: str, faq_data: list) -> dict | None:
    """
    Score each FAQ entry by counting how many of its keywords appear
    in the cleaned user input.  Returns the FAQ with the highest score,
    or None if no keywords matched at all.
    """
    cleaned = clean_input(user_input)
    best_faq   = None
    best_score = 0

    for faq in faq_data:
        score = 0
        for keyword in faq["keywords"]:
            if keyword.lower() in cleaned:
                score += 1
        if score > best_score:
            best_score = score
            best_faq   = faq

    return best_faq if best_score > 0 else None


def is_greeting(text: str, greeting_keywords: list) -> bool:
    """
    Return True only if the entire cleaned input is a greeting phrase,
    or a single greeting token, or a short greeting (<=3 tokens total).
    This prevents substrings like 'hi' inside 'scholarship' from matching.
    """
    cleaned = clean_input(text)
    tokens  = tokenize(cleaned)

    # Only trigger greeting if the message is short (1-3 tokens)
    # and at least one token or phrase is a known greeting keyword.
    if len(tokens) > 3:
        return False

    # Check single-word tokens
    for word in tokens:
        if word in greeting_keywords:
            return True

    # Check multi-word greeting phrases (e.g. "good morning")
    for phrase in greeting_keywords:
        if " " in phrase and phrase == cleaned:
            return True

    return False


def is_farewell(text: str, farewell_keywords: list) -> bool:
    """Return True if the cleaned text matches a farewell keyword."""
    cleaned = clean_input(text)
    for phrase in farewell_keywords:
        if phrase in cleaned:
            return True
    return False


def is_thanks(text: str, thanks_keywords: list) -> bool:
    """Return True if the cleaned text contains a gratitude expression."""
    cleaned = clean_input(text)
    for phrase in thanks_keywords:
        if phrase in cleaned:
            return True
    return False


def is_help_request(text: str) -> bool:
    """Return True if the user typed 'help', 'topics', 'menu', or '?'."""
    cleaned = clean_input(text)
    help_triggers = {"help", "topics", "menu", "list", "options", "what can you do", "?"}
    return cleaned in help_triggers or any(t in cleaned for t in help_triggers)


def get_fallback(fallback_responses: list) -> str:
    """Return a random fallback message so repeated unknowns feel less robotic."""
    return random.choice(fallback_responses)


# ---------------------------------------------------------------------------
# Display / Formatting Helpers
# ---------------------------------------------------------------------------

SEPARATOR = "-" * 60
BOT_TAG   = "  [HelpDesk Bot]"
USER_TAG  = "  [You          ]"


def print_separator():
    print(SEPARATOR)


def format_bot_message(message: str) -> str:
    """Prefix every line of the bot reply with a clean indent."""
    lines = message.split("\n")
    return "\n".join("  " + line if line.strip() else "" for line in lines)


def print_bot(message: str):
    """Print a formatted bot response to the console."""
    print(f"\n{BOT_TAG}:\n{format_bot_message(message)}\n")


def print_user_prompt():
    """Print the user input prompt."""
    return input(f"\n{USER_TAG}: ").strip()


def print_welcome_banner():
    """Print the ASCII welcome banner."""
    banner = r"""
  ============================================================
  |                                                          |
  |        COLLEGE HELP DESK CHATBOT  v1.0                  |
  |        Rule-Based FAQ Assistant                          |
  |        Python 3  |  NLP Assignment                       |
  |                                                          |
  ============================================================
    """
    print(banner)


def print_goodbye_banner():
    print("\n  " + "=" * 58)
    print("  |  Session ended. Thank you for using Help Desk Bot!  |")
    print("  " + "=" * 58 + "\n")


# ---------------------------------------------------------------------------
# Session Logger (optional — saves chat to a .txt file)
# ---------------------------------------------------------------------------

class SessionLogger:
    """Optionally writes the full conversation to a timestamped log file."""

    def __init__(self, enabled: bool = True, log_dir: str = "logs"):
        self.enabled = enabled
        self.log_dir = log_dir
        self.log_file = None

        if enabled:
            import os
            os.makedirs(log_dir, exist_ok=True)
            timestamp  = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename   = f"{log_dir}/session_{timestamp}.txt"
            self.log_file = open(filename, "w", encoding="utf-8")
            self.log_file.write(f"=== Help Desk Chat Session — {timestamp} ===\n\n")

    def log(self, role: str, message: str):
        if self.enabled and self.log_file:
            ts = datetime.datetime.now().strftime("%H:%M:%S")
            self.log_file.write(f"[{ts}] {role}: {message}\n\n")
            self.log_file.flush()

    def close(self):
        if self.enabled and self.log_file:
            self.log_file.write("=== Session ended ===\n")
            self.log_file.close()
