# f = open("demo.txt", "a")

# f.write("\nafter that next.js")

# f.close()

# f =open("sample.txt", "w")
# f.close()

#with syntax 

with open("demo.txt", "r") as f:
    data=f.read()
    print(data)

with open("demo.txt", "r") as f:
    f.write("new data")