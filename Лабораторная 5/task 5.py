import random
import string


def get_random_password() -> str:
    pull_ = string.digits + string.ascii_letters
    return random.sample(pull_, 8)


print(get_random_password())
