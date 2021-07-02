a = ["a","b"]
print("[")
for i in a:
    print("{" + "\n"+ "\"mode\""+":"+"\"NULLABLE\""+","+"\n"+"\"name\""+":"+"\""+i.split()[0]+"\""+","+"\n"+"\"type\""+":"+"\"STRING\""+"\n"+"},")
print("]")