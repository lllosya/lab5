import random
import string


def get_random_password(n) -> str:
    pull_ = string.digits + string.ascii_letters
    return random.sample(pull_, n)


print(get_random_password(8))
