import datetime, random

def generateBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomDay = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomDay
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for a, birthdayA in enumerate(birthdays):
        for birthdayB in birthdays[a + 1:]:
            if birthdayA == birthdayB:
                return birthdayA
    return None

MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

while True:
    response = input("< ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numberOfBD = int(response)
        break
    
birthdays = generateBirthdays(numberOfBD)

for i, birthday in enumerate(birthdays):
    if i != 0:
        print("", end="")
    monthDate = MONTHS[birthday.month - 1]
    textDate = f"{monthDate} {birthday.day}"
    print(textDate, end=" ")

match = getMatch(birthdays)

if match is not None:
    monthDateMatch = MONTHS[match.month - 1]
    textDateMatch = f"{monthDateMatch} {match.day}"
    print(f"\nMatch found: {textDateMatch}")
else:
    print("\nThere are no matching birthdays.")

print("\nGenerating", numberOfBD, "birthdays 100,000 times")
input("Press Enter to begin...")

simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "Simulation run...")
    birthdays = generateBirthdays(numberOfBD)
    if getMatch(birthdays) is not None:
        simMatch += 1

probability = round(simMatch / 100_000 * 100, 2)
print(f"\nOut of 100,000 simulations, there was a matching birthday {simMatch} times.")
print(f"This means the probability of a shared birthday is {probability}%.")
