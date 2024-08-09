'''
[]
{'name':'mamad', 'phone':'09128797654', 'email' : 'mamadgholi@gmail.com'},
{'name':'ali', 'phone':'0937879567'},
{},
]

'''

import re, json

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
contacts = []
names=[]
phones=[]
emails=[]
try:
    with open('contacts.json', 'r') as file:
        contacts = json.load(file)
except FileNotFoundError:
    pass

for i in contacts:
    names.append(i['name'])
for i in contacts:
    phones.append(i['phone'])
for i in contacts:
    emails.append(i['email'])


def get_phone():
    phone = input('Enter contacts phone: ')
    if re.match(r'^09[0-9]{9}$', phone) or re.match(r'^00989[0-9]{9}$', phone) or re.match(r'^\+989[0-9]{9}$', phone):
        return phone
    else:
        print('Please enter a valid input!')
        get_phone()

def get_email():
    email = input('Enter contacts email: ')
    if re.match(email_regex, email):
        return email
    else:
        print('Please enter a valid input!')
        get_email()

def add_new():
    #add new and valida
    name = input('Enter contacts name: ')
    phone = get_phone()
    email = get_email()
    if name not in names:
        contacts.append({'name':name,'phone':phone,'email':email,})
        names.append(name)
        phones.append(phone)
        emails.append(email)


def edit(name, newname,newphone,newemail):
    global contacts
    if name in names:
        contact = contacts[names.index(name)]
        contact['name'] = newname
        contact['phone'] = newphone
        contact['email'] = newemail
    else:
        print(f'There is no contact named {name}')

def delete():
    global contacts
    name = input("Enter contact to delete: ")
    if name in names:
        contact = contacts.pop(names.index(name))
        print(f'Contact named {contact['name']} removed from your contacts')


def show_all():
    print('name  |  phone  |  email')
    for i in range(len(names)):
        print(f"{i+1}- {names[i]}  |   {phones[i]}  |  {emails[i]}")

def sort():
    global contacts
    contacts = sorted(contacts, key=lambda x: x['name'])
    print('Succesfully sorted!')

def save():
    global contacts
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)
        print("Data has been saved to contacts.json")

def start():
        mode = {1 : add_new ,2 : edit ,3 : delete ,4 : show_all ,5: sort ,6 : save ,}
        mode_ch = input(
'''Welcome to contact manager select your mode:
1.Add new contact
2.Edit contact
3.Delete by name
4.Show all contacts
5.Sort by name
6.Save
7.Exit
---> '''
)
        if mode_ch != '7':
            mode[int(mode_ch)]()
            start()


if __name__ == "__main__":
    start()



