import random
import string

def generate_password(length):
    # all lower case letters, uppercase lettes, digits, and special letters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # no. of each type of character
    num_lowercase = random.randint(2, min(length // 2, len(lowercase_letters)))
    num_uppercase = random.randint(1, min(length // 2, len(uppercase_letters)))
    num_digits = random.randint(1, min(length // 4, len(digits))) 
    num_special = length - num_lowercase - num_uppercase - num_digits

    # Generate password by randomly sampling each character
    password = (
        ''.join(random.sample(lowercase_letters, num_lowercase)) +
        ''.join(random.sample(uppercase_letters, num_uppercase)) +
        ''.join(random.sample(digits, num_digits)) +
        ''.join(random.sample(special_characters, num_special))
    )

    # shuffle the password around
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

password_length = random.randint(10, 20)  # length between 10 and 16 for now 
generated_password = generate_password(password_length)
print("Password:", generated_password)