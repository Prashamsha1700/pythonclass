#f = open("myfile.txt", "x")
with open("myfile.txt", "w") as f:
    f.write("Woops! I have deleted!")
with open("myfile.txt", "r") as f:   
    print(f.read())
with open("myfile.txt", "a") as f:   
    f.write("These are hello world!")

with open("myfile.txt", "a") as f:
    f.write(f"{1},{2}\n")
