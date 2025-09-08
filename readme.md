Get the password input

Prompt the user to type in a password.

Define the rules for strength

Length (e.g., at least 8 or 12 characters).

Contains lowercase letters.

Contains uppercase letters.

Contains digits.

Contains special characters (!, @, #, etc.).

Check each rule

Loop through the characters in the password and see what categories are present.

Keep flags/booleans (like has_upper, has_digit, etc.).

Score the password

You could give 1 point for each rule it passes.

Example:

Length ≥ 12 → +1

Has uppercase → +1

Has lowercase → +1

Has number → +1

Has special → +1

Give feedback

If score is low → print “Weak password: add numbers/symbols.”

Medium score → “Okay, but could be stronger.”

High score → “Strong password.”

(Optional) Add extra features later

Check against a list of common weak passwords.

Estimate “time to crack” using rough math.

Suggest improvements to the user.