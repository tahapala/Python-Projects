def password_security_test(password):
    # Step 1: Length Check
    if len(password) < 8:
        return "Weak: Your password must be at least 8 characters long."
    
    # Step 2: Initialize control flags as False at the beginning.
    has_upper_case = False
    has_lower_case = False
    has_digit = False
    
    # Step 3: Check each character in the password one by one with a loop.
    for char in password:
        if char.isupper():  # Is the character an uppercase letter?
            has_upper_case = True
        elif char.islower():  # Is the character a lowercase letter?
            has_lower_case = True
        elif char.isdigit():  # Is the character a digit?
            has_digit = True
            
    # Step 4: Notify the user of any missing requirements.
    if has_upper_case == False:
        return "Medium: Your password is not secure. Please add at least one UPPERCASE letter."
    
    if has_lower_case == False:
        return "Medium: Your password is not secure. Please add at least one LOWERCASE letter."
        
    if has_digit == False:
        return "Medium: Your password is not secure. Please add at least one NUMBER (digit)."
        
    # If the code reaches this point, it means the password meets all conditions.
    return "Strong: Great! Your password is very secure."

# --- Program Execution Section ---
print("--- Welcome to the Password Security Test ---")
user_input = input("Please enter the password you want to test: ")

# Call the function and print the returned result to the screen
result = password_security_test(user_input)
print("Status:", result)