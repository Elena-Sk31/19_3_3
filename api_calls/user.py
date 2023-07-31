from requests.compat import urljoin

from . import RS, BASE_URL

BASE_URL = urljoin(BASE_URL, 'user/')


def run():

    # Create user
    user = {
      'username': 'БОЧ',
      'firstName': 'рВФ',
      'lastName': '260602',
      'email': 'boch@260602.rvf',
      'password': 'qwerty123',
      'phone': '322223'
    }

    resp = RS.post(url=BASE_URL, json=user)

    print('Create user')
    print(resp.json())
    print()

    # Logs user into the system
    resp = RS.get(url=urljoin(BASE_URL, 'login/'), data={'username': user['username'], 'password': user['password']})

    print('Logs user into the system')
    print(resp.json())
    print()

    # Get user by user name
    resp = RS.get(url=urljoin(BASE_URL, user['username']))

    print('Get user by user name')
    print(resp.json())
    print()

    # Updated user
    user['status'] = 1
    resp = RS.put(url=urljoin(BASE_URL, user['username']), json=user)

    print('Updated user')
    print(resp.json())
    print()

    # Creates list of users with given input array
    users = [
        {
            "username": "user1",
            "firstName": "firstName1",
            "lastName": "lastName1",
            "email": "email1@localhost",
            "password": "password1",
            "phone": "phone1"
        },
        {
            "username": "user2",
            "firstName": "firstName2",
            "lastName": "lastName2",
            "email": "email2@localhost",
            "password": "password2",
            "phone": "phone2"
        }
    ]

    resp = RS.post(url=urljoin(BASE_URL, 'createWithArray/'), json=users)

    print('Creates list of users with given input array')
    print(resp.json())
    print()

    # Creates list of users with given input array
    resp = RS.post(url=urljoin(BASE_URL, 'createWithList/'), json=users)

    print('Creates list of users with given input array')
    print(resp.json())
    print()

    # Logs out current logged in user session
    resp = RS.get(url=urljoin(BASE_URL, 'logout/'))

    print('Logs out current logged in user session')
    print(resp.json())
    print()

    # Delete user
    resp = RS.delete(url=urljoin(BASE_URL, user['username']))

    print('Delete user')
    print(resp.json())
    print()
