def gcd(a, b):
    # Standard Euclidean Algorithm
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def solve_linear_congruence(a, b, m):
    # Step 1: Calculate GCD(a, m)
    d = gcd(a, m)
    
    # Step 2: Check Existence
    # The equation ax ≡ b (mod m) has solutions ONLY if d divides b
    if b % d != 0:
       
        print("Existence of Solutions: NO")
        print("Reason: GCD({0}, {1}) = {2}, and {2} does not divide {3}.".format(a, m, d, b))
        return
    else:
        print(f"{a}x ≡ {b} (mod {m}) ")
        print("Existence of Solutions: YES")
        print(f"Number of Solutions: {d}")
        
        # Step 3: Find the solutions
        # Your logic: Find the first solution (x0) using a loop
        x0 = -1
        for i in range(m):
            if ((a * i) - b) % m == 0:
                x0 = i
                break
        
        # Calculate the step size (m/d)
        step = m // d
        
        # Generate all 'd' solutions
        solutions = []
        for j in range(d):
            solutions.append(x0 + (step * j))
            
        print(f"Solutions: {solutions}")

# --- Driver Code ---
if __name__ == "__main__":
    try:
        a_in = int(input("Enter a: "))
        b_in = int(input("Enter b: "))
        m_in = int(input("Enter m: "))
        
        solve_linear_congruence(a_in, b_in, m_in)
    except ValueError:
        print("Please enter valid integers.")
