

def guesser(firstName, lastName, domain):
    guesses = []
    guesses.append(f"{firstName}{lastName}@{domain}")
    guesses.append(f"{firstName}.{lastName}@{domain}")
    guesses.append(f"{firstName}_{lastName}@{domain}")
    guesses.append(f"{firstName[0]}{lastName}@{domain}")
    guesses.append(f"{firstName[0]}.{lastName}@{domain}")
    guesses.append(f"{firstName[0]}_{lastName}@{domain}")
    guesses.append(f"{firstName}{lastName[0]}@{domain}")
    guesses.append(f"{firstName}.{lastName[0]}@{domain}")
    guesses.append(f"{firstName}_{lastName[0]}@{domain}")
    guesses.append(f"{lastName}{firstName}@{domain}")
    guesses.append(f"{lastName}.{firstName}@{domain}")
    guesses.append(f"{lastName}_{firstName}@{domain}")
    guesses.append(f"{lastName}{firstName[0]}@{domain}")
    guesses.append(f"{lastName}.{firstName[0]}@{domain}")
    guesses.append(f"{lastName}_{firstName[0]}@{domain}")
    guesses.append(f"{firstName}@{domain}")
    guesses.append(f"{lastName}@{domain}")
    guesses.append(f"{firstName[0]}@{domain}")
    guesses.append(f"{lastName[0]}@{domain}")
    guesses.append(f"{firstName[0]}{lastName[0]}@{domain}")
    guesses.append(f"{firstName[0]}.{lastName[0]}@{domain}")
    guesses.append(f"{firstName[0]}_{lastName[0]}@{domain}")
    guesses.append(f"{lastName[0]}{firstName[0]}@{domain}")
    guesses.append(f"{lastName[0]}.{firstName[0]}@{domain}")
    guesses.append(f"{lastName[0]}_{firstName[0]}@{domain}")
    return guesses


print(guesser('sachin', "tripathi", "domain.ai"))
