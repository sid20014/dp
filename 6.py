def brute_force_attack(password):
  chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{};':\"\\|,.<>/? "
  for i in range(1, len(password) + 1):
    for attempt in generate_combinations(chars, i):
      if attempt == password:
        return attempt
  return None


def generate_combinations(chars, length):
  if length == 0:
    yield ""
  else:
    for char in chars:
      for combo in generate_combinations(chars, length - 1):
        yield char + combo


password = input("Enter a Password: ")
result = brute_force_attack(password)
if result:
  print("Password cracked:", result)
else:
  print("Password not found")