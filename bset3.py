a = str(input())
arr = ["a","e","i","o","u"]
if len(a)<2:
    if a in arr:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
