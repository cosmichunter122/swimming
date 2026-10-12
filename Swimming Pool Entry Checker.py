print("=== Community Pool Access Planner ===")
print("Answer 3 quick questions and I will check the pool rules for you!\n")

age        = int(input("How old are you?: "))
can_swim   = input("Can you swim twenty-five metres? (yes / no): ").strip().lower()
adult_here = input("Is an adult with you? (yes / no): ").strip().lower()

print()
print(f"=== Your Pool Access Plan (Age: {age}) ===")
print("-" * 45)

if not (can_swim == "yes" or can_swim == "no"):
    print("Input error : 'Can swim' answer not recognised. Please type yes or no.")
    swim_known = False
else:
    swim_known = True

if not (adult_here == "yes" or adult_here == "no"):
    print("Input error : 'Adult here' answer not recognised. Please type yes or no.")
    adult_known = False
else:
    adult_known = True

if can_swim == "yes" and adult_here == "yes":
    print("Deep pool   : Allowed - you can swim and an adult is present.")

if age < 12 or can_swim == "no":
    print("Shallow end : Warning - you are under 12 or cannot swim.")

if adult_known and not (adult_here == "yes"):
    print("Lifeguard   : Reminder - no adult is present with you.")

if not swim_known or not adult_known:
    print("Final verdict: Invalid answers provided. Cannot determine pool access.")
elif can_swim == "yes" and adult_here == "yes" and age >= 12:
    print("Final verdict: You have full access to all pool areas!")
elif age < 12 and adult_here == "yes":
    print("Final verdict: Welcome! Enjoy the pool with your accompanying adult.")
else:
    print("Final verdict: Please check with the front desk staff before entering.")

print()
print("Have a safe swim!")