def generator_count(String):
    for i in String:
        if i == "s":
            yield i

String = input()
ans = 0
print("The number of 's' in word is : ", end="")
String = String.strip()
for j in generator_count(String):
    ans = ans + 1
print(ans)