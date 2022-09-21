import sys


def get_clients():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
               'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    return set(clients)


def get_participants():
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                    'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    return set(participants)


def get_recipients():
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return set(recipients)


def call_center():
    clients = get_clients()
    clients.update(get_participants())
    return list(clients - get_recipients())


def potential_clients():
    participants = get_participants()
    participants.update(get_recipients())
    return list(participants - get_clients())


def loyalty_program():
    clients = get_clients()
    clients.update(get_recipients())
    return list(clients - get_participants())


def marketing(command):
    if command == "call_center":
        print(call_center())
    elif command == "potential_clients":
        print(potential_clients())
    elif command == "loyalty_program":
        print(loyalty_program())
    else:
        raise NameError


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            marketing(sys.argv[1])
        except NameError:
            print("unknown command")
    else:
        print('invalid argv')
