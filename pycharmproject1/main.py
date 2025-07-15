def reverse_str(s):
    return s[::-1]

def is_palandrome(s):
    rstr = reverse_str(s).lower()
    if s.lower() == rstr:
        return True
    else:
        return False

def count_vovel(s):
    v = "aeiou"
    count = 0
    for char in s.lower():
        if char in v:
            count+=1
    return count

def is_anagrame(s,s1):
    return sorted(s) == sorted(s1)


print(count_vovel("aeighijkolnu"))
print(is_anagrame("carreverse","revesecar"))

