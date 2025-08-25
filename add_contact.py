# define a function add_contact() that will be used to add contact details
def add_contact(a):
    name=input("Enter name: ")
    phone=int(input("Enter contact (+254*********): "))
    # empty dict{}
    b={"name": name , "phone": phone}
    # append
    a.append(b)
    print("Contact added successfully!")