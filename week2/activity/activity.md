# Class activity week2

## Activity 2.1: Logic Tracing Sandbox

### Block A: Evaluation Check

```python

temp = 25
is_raining = True
if temp > 20 and not is_raining:
    print("Perfect day for a picnic!")
elif temp <= 20 or is_raining:
    print("Stay indoors or bring an umbrella!") # Expected output matches here
else:
    print("Unsure about the weather!")

```

### Block B: Vectorized Filter

```python

phrase = "Python 2026 Engine"
consonants = {c.lower() for c in phrase if c.isalpha() and c.lower() not in 'aeiou'}
print(f"Unique consonants: {consonants}")

```

## Activity 2.2: Choose your own adventure architectures
