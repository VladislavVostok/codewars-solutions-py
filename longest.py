def longest(a1, a2):
    return "".join(sorted(list(set(a1 + a2))))

print(longest("aretheyhere", "yestheyarehere"))
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))