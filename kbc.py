que=["how many hours in a day? ", '22', '30', '24', '33']

print(que[0])

print(f"a. {que[1]}          b. {que[2]} ")
print(f"c. {que[3]}          d. {que[4]} ")
reply=input(("select your ans: "))

if reply==que[3]:
    print("you win")
else:
    print("you lose")