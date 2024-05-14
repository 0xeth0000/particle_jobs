ef water(wallet_, proxies):
    wallet_address = wallet_['address']
    private_key = wallet_['private_key']
    try:
        headers = {
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'origin': 'https://www.bsquared.network',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.bsquared.network/',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': Faker().chrome(),
        }

        url = f'https://task-openapi.bsquared.network/v1/faucet?is_aa=false&to_address={wallet_address}'

        res = requests.get(url=url, proxies=proxies, headers=headers, impersonate="chrome120", verify=False,
                           timeout=15).json()
    except Exception as err:
        print(e)
    #https://pioneer-api.particle.network/users
    #https://pioneer-api.particle.network/users/bind
    #https://universal-api.particle.network/'
