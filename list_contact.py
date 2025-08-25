# def function list_contact() that will be  used to list down the contacts
def list_contact(a):
    if not a:
        print("No Contact found")
        return
    for i, b in enumerate(a, 1):
        print(f"{i}. {b["name"]} - {b["phone"]}")