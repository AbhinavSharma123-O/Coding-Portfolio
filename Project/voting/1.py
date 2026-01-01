candidates ={"Nitish":0, "Rahul":0, "Lalu":0}
print("Candidates")
i=1
for name in candidates:
    print(f"{i}.{name}")
    i+=1
number_of_voters=int(input("Enter the number of voters:"))
for voter in range(number_of_voters):
    print(f"\nVoter {voter + 1}:")
    print("Enter the number of the candidates you want to vote for:")
    i=1
    for name in candidates:
        print(f"{i}.{name}")
        i+=1
    choice = int(input("Your choice: "))
    candidate_names = list(candidates.keys())
    if 1 <= choice <= len(candidate_names):
        selected_candidate = candidate_names[choice - 1]
        candidates[selected_candidate] += 1
        print(f"You voted for {selected_candidate}")
    else:
        print("Invalid choice. Vote not counted.")
print("Voting Results:")
for name in candidates:
    print(f"{name}: {candidates[name]} vote(s)")
