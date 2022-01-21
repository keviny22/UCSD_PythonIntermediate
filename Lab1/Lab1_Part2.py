# Python II – Lab 1 – Kevin Young

def grade_password(password: str) -> int:
    score = 0
    if len(password) > 7:
        score += 1
    if len(password) > 8:
        score += 1
    if len(password) >= 16:
        score += 1
    if contains_upper(password):
        score += 1
    if contains_lower(password):
        score += 1
    if contains_number(password):
        score += 1
    if contains_symbol(password):
        score += 1

    return score


def contains_lower(text: str) -> bool:
    for x in text:
        if x.islower():
            return True
    return False


def contains_upper(text: str) -> bool:
    for x in text:
        if x.isupper():
            return True
    return False


def contains_number(text: str) -> bool:
    for x in text:
        if x.isnumeric():
            return True
    return False


def contains_symbol(text: str) -> bool:
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
    for x in text:
        if x in symbols:
            return True
    return False


if __name__ == '__main__':
    password = input('Enter a password:')
    print(f"Your password score is: {grade_password(password)}")
