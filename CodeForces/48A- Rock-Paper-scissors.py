f = input().lower()
m = input().lower()
s = input().lower()
if (f == "rock" and m == "scissors" and s == "scissors") or (f == "paper" and m == "rock" and s == "rock") or (
        f == "scissors" and m == "paper" and s == "paper"):
    print("F")
elif (m == "rock" and f == "scissors" and s == "scissors") or (m == "paper" and f == "rock" and s == "rock") or (
        m == "scissors" and f == "paper" and s == "paper"):
    print("M")
elif (s == "rock" and m == "scissors" and f == "scissors") or (s == "paper" and m == "rock" and f == "rock") or (
        s == "scissors" and m == "paper" and f == "paper"):
    print("S")
else:
    print("?")
