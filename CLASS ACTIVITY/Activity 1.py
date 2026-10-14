import re
text = """Ravi's phone number is 9876543210.
His email is ravi@gmail.com.
Priya's phone number is 9123456780.
Her email is priya@gmail.com."""
phones = re.findall(r'\d{10}', text)
emails = re.findall(r'\w+@\w+\.\w+', text)
words = re.findall(r'\bphone\b', text, re.IGNORECASE)
print("Phone Numbers:", phones)
print("Email Addresses:", emails)
print("Number of times 'phone' appears:", len(words))
