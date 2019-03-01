import hashlib
import urllib.request
from concurrent import futures

BASE_PATH = 'https://upload.wikimedia.org/wikipedia/commons/thumb/'
NAME_FMT = '{h0}/{h01}/{name}/200px-{name}.png'

def build_path(filename):
    md5 = hashlib.md5(filename.encode('utf-8')).hexdigest()
    return BASE_PATH + NAME_FMT.format(h0=md5[0], h01=md5[:2], name=filename)


def download_one(name):
    url = build_path(name)
    print(url)
    with urllib.request.urlopen(url) as response:
        svg = response.read()
    save_name = name.replace('.svg', '.png')
    with open(save_name, 'wb') as fp:
        fp.write(svg)
    return name

def main():
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    names = [f'{rank}{suit}.svg' for rank in ranks for suit in 'SDCH']
    with futures.ThreadPoolExecutor(10) as executor:
        res = executor.map(download_one, names)

    print(len(list(res)), 'cards downloaded.')


if __name__=='__main__':
    main()
