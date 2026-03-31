def input_processor(command: str) -> list:
    # all lower case letters and strip of all side-whitespaces
    text = command.lower().strip()
    if not text:
        return []

    # tokenization
    tokens = text.split()
    return tokens