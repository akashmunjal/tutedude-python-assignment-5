try:
    dict = {'john':89, 'mike':90, 'neha':92, 'naruto':75}
    name = input("Enter student's name: ")
    print(name,"'s marks: ", dict[name])
except:
    print("Student not found")
