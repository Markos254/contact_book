# def function search_contact() that will be used to search for a contact
def search_contact(a):
    search_name=input("Enter name to search: ")
    found=None
    for b in a:
        if b["name"].lower()==search_name.lower():
            found=b
            break
    if found:
        print("FOund",b["name"],"-",b["phone"])
    else: 
        print("Contact not found!")
