# dictionary
d = [
    {'name': "Ram", 'phone': '9434141414', 'email': "ram@gmail.com"}, 
    {'name': 'Laksman', 'phone': '8434151515', 'email': None}, 
    {'name': 'Bharat', 'phone': '7474161616', 'email': 'bharat@gmail.com'},  
    {'name': "Satrughna", 'phone': '9478171717', 'email': "satrughna@gmail.com"}
]

def main():
    # (a) All users whose phone number ends in 5
    print("Users whose phone number ends in 5:")
    for user in d:
        if user['phone'][-1] == '5':
            print(user['name'])

    # (b) All users that don't have an email address listed
    print("\nUsers without email addresses:")
    for user in d:
        if user['email'] is None:
            print(user['name'])

    # (c) All users whose phone number starts with 9
    print("\nUsers whose phone number starts with 9:")
    for user in d:
        if user['phone'].startswith('9'):
            print(user['name'])

if __name__ == "__main__":
    main()
