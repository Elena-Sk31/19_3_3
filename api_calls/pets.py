from requests.compat import urljoin
from pathlib import Path

from . import RS, BASE_URL

BASE_URL = urljoin(BASE_URL, 'pet/')
current_dir = Path(__file__).parent


pet = {
    'id': None,
    'category': {
        'id': None,
        'name': 'category'
    },
    'name': 'doggie',
    'photo_urls': [
        'https://img.freepik.com/free-photo/crazy-happy-husky-companion-dog-is-posing-cute-playful-white-grey-doggy-pet-playing-white-studio-background-concept-motion-action-movement-pets-love-looks-happy-delighted-funny_155003-33972.jpg?w=1380&t=st=1690636499~exp=1690637099~hmac=0ad4e939e1e18a3b56c5bd4284754a7533460cf3950c46660db1ac12b6e0ce7a'
    ],
    'tags': [
        {
            'id': None,
            'name': 'tag'
        }
    ],
    'status': 'available'
}


def run():
    print('Add a new pet to the store')
    resp = RS.post(url=BASE_URL, json=pet)
    resp_json = resp.json()
    print(resp_json)
    print()

    pet_id = resp_json['id']

    # Find pet by ID
    resp = RS.get(url=urljoin(BASE_URL, str(pet_id)))

    print('Find pet by ID')
    print(resp.json())
    print()

    # Update an existing pet
    pet['name'] = 'DoggieDoggie'
    resp = RS.put(BASE_URL, json=pet)

    print('Update an existing pet')
    print(resp.json())
    print()

    # Uploads an image
    files = {'file': open(current_dir / 'img/dog.jpg', 'rb')}
    resp = RS.post(url=urljoin(BASE_URL, f'{pet_id}/uploadImage'), files=files)

    print('Uploads an image')
    print(resp.text)
    print()

    # # Finds Pets by status
    resp = RS.get(url=urljoin(BASE_URL, 'findByStatus'), params={'status': 'sold'})

    print('Finds Pets by status "sold"')
    print(resp.json())
    print()

    # Updates a pet in the store with form data
    resp = RS.post(url=urljoin(BASE_URL, str(pet_id)), data={'petId': pet_id, 'name': 'Dog', 'status': 'sold'})

    print('Updates a pet in the store with form data')
    print(resp.json())
    print()

    # Deletes a pet
    resp = RS.delete(url=urljoin(BASE_URL, str(pet_id)))

    print('Deletes a pet')
    print(resp.json())
    print()
