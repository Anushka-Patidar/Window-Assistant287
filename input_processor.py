import re


# ─── Number Word Tables ───────────────────────────────────────────────────────

# words that map directly to a single integer (no follow-up token needed)
SINGULAR_NUMS = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen", "hundred"
]

# words that are multiples of ten and may be followed by a singular num word
POSSIBLE_DOUBLE_NUMS = [
    "twenty", "thirty", "forty", "fifty", "sixty",
    "seventy", "eighty", "ninety"
]

# complete word -> integer lookup (covers 1–100, plus all compound tens)
WORD_TO_NUM = {
    "one": 1,   "two": 2,   "three": 3,  "four": 4,  "five": 5,
    "six": 6,   "seven": 7, "eight": 8,  "nine": 9,  "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,
    "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,

    "twenty one": 21,   "twenty two": 22,   "twenty three": 23,
    "twenty four": 24,  "twenty five": 25,  "twenty six": 26,
    "twenty seven": 27, "twenty eight": 28, "twenty nine": 29,
    "thirty one": 31,   "thirty two": 32,   "thirty three": 33,
    "thirty four": 34,  "thirty five": 35,  "thirty six": 36,
    "thirty seven": 37, "thirty eight": 38, "thirty nine": 39,
    "forty one": 41,    "forty two": 42,    "forty three": 43,
    "forty four": 44,   "forty five": 45,   "forty six": 46,
    "forty seven": 47,  "forty eight": 48,  "forty nine": 49,
    "fifty one": 51,    "fifty two": 52,    "fifty three": 53,
    "fifty four": 54,   "fifty five": 55,   "fifty six": 56,
    "fifty seven": 57,  "fifty eight": 58,  "fifty nine": 59,
    "sixty one": 61,    "sixty two": 62,    "sixty three": 63,
    "sixty four": 64,   "sixty five": 65,   "sixty six": 66,
    "sixty seven": 67,  "sixty eight": 68,  "sixty nine": 69,
    "seventy one": 71,  "seventy two": 72,  "seventy three": 73,
    "seventy four": 74, "seventy five": 75, "seventy six": 76,
    "seventy seven": 77,"seventy eight": 78,"seventy nine": 79,
    "eighty one": 81,   "eighty two": 82,   "eighty three": 83,
    "eighty four": 84,  "eighty five": 85,  "eighty six": 86,
    "eighty seven": 87, "eighty eight": 88, "eighty nine": 89,
    "ninety one": 91,   "ninety two": 92,   "ninety three": 93,
    "ninety four": 94,  "ninety five": 95,  "ninety six": 96,
    "ninety seven": 97, "ninety eight": 98, "ninety nine": 99,
    "hundred": 100,
}


# ─── Main Function ────────────────────────────────────────────────────────────

def input_processor(command: str) -> list:
    text = command.lower()

    # strip punctuation — but keep a minus sign that directly precedes a digit
    # step 1: preserve negative numbers by temporarily replacing "-digit" with a placeholder
    text = re.sub(r'-(\d)', r'MINUS\1', text)

    # step 2: strip ALL punctuation cleanly
    text = re.sub(r'[!"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]', "", text)

    # step 3: restore negative numbers
    text = re.sub(r'MINUS(\d)', r'-\1', text)

    
    if not text:
        return []       # no command provided!

    # remove extra spaces + convert string -> list
    tokens = text.strip().split()

    # ── Number word → integer conversion ─────────────────────────────────────
    i = 0
    while i < len(tokens):
        current = tokens[i]

        if current in SINGULAR_NUMS:
            tokens[i] = WORD_TO_NUM[current]

        elif current in POSSIBLE_DOUBLE_NUMS:
            # check if the next token forms a compound number (a double digit number) (e.g. "twenty" + "one")
            if (i + 1) < len(tokens) and tokens[i + 1] in SINGULAR_NUMS:        # always check for outofbound index
                tokens[i] = current + " " + tokens[i + 1]                       # concatenate both words for proper 
                tokens.pop(i + 1)
            tokens[i] = WORD_TO_NUM[tokens[i]]

        elif current.lstrip("-").isdigit():     # check for digits (ignore any leading hypher - sign before it!)
            tokens[i] = int(current)            # converts both positive and negative digits

        i += 1

    return tokens
