from typing import Tuple
from concurrent.futures import ThreadPoolExecutor

import requests

URL = 'http://code.qqmber.wtf/guess/'


def guess_password(password: str) -> Tuple[bool, str, requests.Response]:
    print(password)
    response = requests.post(URL, json={'password': password})
    return response.status_code == 200, password, response


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=32) as executor:
        for success, password, response in executor.map(guess_password, (str(i).zfill(3) for i in range(1000))):
            print(f'Check: {password}, {response}')
            if success:
                print(f'Done, password is {password}')
                break
