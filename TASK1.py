import hashlib
def register():
    f = open("f.txt", "a")
    name = input("Enter your name:")
    passwd = input("Enter your password:")
    nh = hashlib.sha256(name.encode('UTF-8')).hexdigest()
    ph = hashlib.sha256(passwd.encode('UTF-8')).hexdigest()
    f.write(nh + '\n')
    f.write(ph + '\n')
    return nh,ph
def login():
  with open('f.txt', 'r') as fl:
    file_content = fl.read()
  name = input("Enter your name:")
  passwd = input("Enter your password:")
  nh = hashlib.sha256(name.encode('UTF-8')).hexdigest()
  ph = hashlib.sha256(passwd.encode('UTF-8')).hexdigest()
  if nh in file_content and ph in file_content:
    print("Successfully logined in.")
  else:
    print("Wrong credentials.")
    
#__main__
f = True
while f==True:
  print("1.Register\n2.Login\n3.Exit")
  ch = int(input("Enter your choice:"))
  if ch == 1:
    register()
  elif ch == 2:
    login()
  else:
    f = False
