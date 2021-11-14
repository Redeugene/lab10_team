with open('proxies.txt') as file:
    proxies = file.read().splitlines()


with open('useragents.txt') as file:
    useragents = file.read().splitlines()


headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.228.0 Safari/537.36'})
