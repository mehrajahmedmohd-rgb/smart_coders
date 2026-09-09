email="mehrajahmed123@gmail.com"
username=""

for ch in email:
    if ch == '@':
        break

    username= username + ch

print(username)    