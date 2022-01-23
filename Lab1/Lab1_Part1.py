# Python II – Lab 1 – Kevin Young

def is_palindrome(text: str) -> bool:
    text_len = len(text)
    for x in range(text_len):
        first = text[x]
        last = text[text_len - x - 1]
        if first != last:
            return False

    return True


if __name__ == '__main__':
    reply = input('Enter a string:')
    lowered_reply = reply.lower()
    print(f"Is '{reply}' a palindrome? {is_palindrome(lowered_reply)}")

