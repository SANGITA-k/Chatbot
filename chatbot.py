#!/usr/bin/env python3
# =============================================================================
# chatbot.py
# Main Chatbot Logic — College Help Desk FAQ Bot
#
# Usage:
#   python chatbot.py            (normal mode)
#   python chatbot.py --nolog    (disable session logging)
#   python chatbot.py --test     (run self-test suite)
#
# Project Structure:
#   chatbot.py    <- YOU ARE HERE  (conversation loop + dispatcher)
#   responses.py  <- FAQ data, keyword lists, special responses
#   utils.py      <- input cleaning, matching, display helpers
#   README.md     <- project documentation
#   report.pdf    <- assignment report
# =============================================================================

import sys

from responses import (
    FAQ_DATA,
    FALLBACK_RESPONSES,
    GREETING_KEYWORDS,
    GREETING_RESPONSE,
    FAREWELL_KEYWORDS,
    FAREWELL_RESPONSE,
    THANKS_KEYWORDS,
    THANKS_RESPONSE,
    HELP_RESPONSE,
)
from utils import (
    find_best_match,
    is_greeting,
    is_farewell,
    is_thanks,
    is_help_request,
    get_fallback,
    print_bot,
    print_user_prompt,
    print_welcome_banner,
    print_goodbye_banner,
    print_separator,
    SessionLogger,
)


# ---------------------------------------------------------------------------
# Core dispatcher
# ---------------------------------------------------------------------------

def get_response(user_input: str) -> tuple[str, bool]:
    """
    Determine the appropriate bot response for a given user input.

    Returns:
        (response_text: str, should_exit: bool)
    """
    if not user_input.strip():
        return "Please type something so I can help you!", False

    # 1. Farewell check — must come before greeting (bye > hi)
    if is_farewell(user_input, FAREWELL_KEYWORDS):
        return FAREWELL_RESPONSE, True

    # 2. Greeting check
    if is_greeting(user_input, GREETING_KEYWORDS):
        return GREETING_RESPONSE, False

    # 3. Gratitude check
    if is_thanks(user_input, THANKS_KEYWORDS):
        return THANKS_RESPONSE, False

    # 4. Help / topic list
    if is_help_request(user_input):
        return HELP_RESPONSE, False

    # 5. FAQ keyword matching
    matched_faq = find_best_match(user_input, FAQ_DATA)
    if matched_faq:
        return matched_faq["answer"], False

    # 6. Fallback
    return get_fallback(FALLBACK_RESPONSES), False


# ---------------------------------------------------------------------------
# Conversation loop
# ---------------------------------------------------------------------------

def run_chatbot(enable_logging: bool = True):
    """Start the interactive chatbot session."""
    print_welcome_banner()
    print_separator()

    logger = SessionLogger(enabled=enable_logging)

    # Initial greeting from bot
    print_bot(GREETING_RESPONSE)
    logger.log("Bot", GREETING_RESPONSE)

    while True:
        try:
            user_input = print_user_prompt()
        except (EOFError, KeyboardInterrupt):
            # Graceful Ctrl+C / EOF handling
            print("\n")
            print_bot(FAREWELL_RESPONSE)
            break

        if not user_input:
            continue

        logger.log("User", user_input)

        response, should_exit = get_response(user_input)

        print_bot(response)
        logger.log("Bot", response)

        if should_exit:
            break

    print_goodbye_banner()
    logger.close()


# ---------------------------------------------------------------------------
# Self-test suite
# ---------------------------------------------------------------------------

def run_tests():
    """
    Quick automated test suite — checks that key queries return relevant answers.
    Run with:  python chatbot.py --test
    """
    print("\n  Running self-test suite...\n")
    test_cases = [
        # (user_query,           expected_topic_substring)
        ("hello",                       "Welcome"),
        ("how do i apply for admission","Admission"),
        ("what are the fees",           "Fee Payment"),
        ("show me my timetable",        "timetable"),
        ("scholarship for merit",       "Merit Scholarship"),
        ("replace my id card",          "ID Card"),
        ("hostel application",          "Hostel"),
        ("when are exams",              "Examination"),
        ("contact professor",           "Faculty Directory"),
        ("library timings",             "Library"),
        ("wifi password",               "Wi-Fi"),
        ("need bonafide certificate",   "Certificate"),
        ("sports gym",                  "Sports"),
        ("college clubs",               "clubs"),
        ("bus route",                   "Transport"),
        ("feeling sick doctor",         "Health"),
        ("forgot portal password",      "password"),
        ("check my result",             "Results"),
        ("attendance shortage",         "75%"),
        ("file a complaint",            "Grievance"),
        ("campus placement",            "Placement"),
        ("thank you",                   "welcome"),
        ("bye",                         "Thank you"),
        ("xyzabc123",                   "sorry"),  # fallback test
    ]

    passed = 0
    failed = 0

    for query, expected_fragment in test_cases:
        response, _ = get_response(query)
        ok = expected_fragment.lower() in response.lower()
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        else:
            failed += 1
        print(f"  [{status}]  Query: '{query}'")
        if not ok:
            print(f"         Expected to contain: '{expected_fragment}'")
            print(f"         Got: '{response[:80]}...'")

    print(f"\n  Results: {passed} passed, {failed} failed out of {len(test_cases)} tests.\n")
    return failed == 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if "--test" in sys.argv:
        success = run_tests()
        sys.exit(0 if success else 1)

    enable_log = "--nolog" not in sys.argv
    run_chatbot(enable_logging=enable_log)
