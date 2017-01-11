
print("--------------read write file-------------------")
fw = open("simple.txt", "w", encoding="utf-8")
fw.write("Writing some stuff in my text file\n")
fw.write("I 喜欢 milk\n")
fw.close()

fr = open("simple.txt", "r", encoding="utf-8")
text = fr.read()
print(text)