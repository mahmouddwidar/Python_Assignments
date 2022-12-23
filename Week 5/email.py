#input

email = input("Enter your Email: ").strip().lower()

#process

firstName = email[:email.index("@")].capitalize()
site = email[email.index("@") +1 :email.index(".")]
domain = email[email.index("."):] 

#output

print(f"Your User Name Is {firstName}")
print(f"Email Service Provider Is {site}")
print(f"Top Level Domain Is {domain}")