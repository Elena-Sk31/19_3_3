from requests.compat import urljoin

from . import RS, BASE_URL

BASE_URL = urljoin(BASE_URL, 'store/')


def run():
    # Returns pet inventories by status
    resp = RS.get(url=urljoin(BASE_URL, 'inventory'))

    print('Returns pet inventories by status')
    print(resp.json())
    print()

    # Place an order for a pet
    resp = RS.post(url=urljoin(BASE_URL, 'order/'), json={'status': 'placed', 'complete': False})

    print('Place an order for a pet')
    print(resp.json())
    print()

    # Find purchase order by ID
    resp = RS.get(url=urljoin(BASE_URL, 'order/8/'))

    print('Find purchase order by ID')
    print(resp.json())
    print()

    # Delete purchase order by ID
    resp = RS.delete(url=urljoin(BASE_URL, 'order/8/'))

    print('Delete purchase order by ID')
    print(resp.json())
    print()

# {'sold': 2, 'string': 756, 'good pet': 1, 'do not touch': 1, 'pending': 3, 'available': 200}