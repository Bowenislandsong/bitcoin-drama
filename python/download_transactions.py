import datetime
import time
import requests
import gzip
import json
import os


def download_block_of_day(year, month, day, hour, minute, second):
    date = datetime.datetime(year, month, day, hour, minute, second)
    unix_time = time.mktime(date.timetuple())
    url = f"https://blockchain.info/blocks/{int(unix_time * 1000)}?format=json"  # Time in milliseconds
    print(url)
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)
    file_id = date.strftime("%Y%m%d")
    file_name = f'../dataset/blocks_{file_id}.txt'
    with open(file_name, 'w') as out_file:
        json.dump(response.json(), out_file)
    return file_id


def download_transactions_in_block(file_id, output_gzip=True):
    file_name = f'../dataset/blocks_{file_id}.txt'
    with open(file_name, 'r') as input_file:
        block_list = json.load(input_file)
    print(f'Fetch {len(block_list)} blocks on {file_id}')

    transactions = []
    for i, block in enumerate(block_list):
        block_id = block['hash']
        url = f"https://blockchain.info/rawblock/{block_id}"
        print(f"block {i+1}/{len(block_list)}:")
        print(url)
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)
        block_info = response.json()
        transactions += block_info['tx']

    print('Number of transactions: ', len(transactions))
    if output_gzip:
        with gzip.open(f'../dataset/transactions_{file_id}.txt.gz', 'wt', encoding='UTF-8') as zipfile:
            json.dump(transactions, zipfile)
    else:
        with open(f'../dataset/transactions_{file_id}.txt', 'w') as output_file:
            json.dump(transactions, output_file)


def download_bitcoin_price(year):
    url = f"https://www.cryptodatadownload.com/cdd/Bitstamp_BTCUSD_{year}_minute.csv"
    with requests.get(url, stream=True, verify=False) as r:
        r.raise_for_status()
        file_name = f'../dataset/Bitstamp_BTCUSD_{year}_minute.csv'
        with open(file_name, 'wb') as out_file:
            for chunk in r.iter_content(chunk_size=8192):
                out_file.write(chunk)

    # Convert and save to BTC_USD_2021_minute.csv
    with open(f'../dataset/Bitstamp_BTCUSD_{year}_minute.csv') as file:
        price_per_timestamp = [record.split(',')[:4] for record in file.readlines()[2:]]
    with open(f'../dataset/BTC_USD_{year}_minute.csv', 'w') as file:
        for record in price_per_timestamp:
            file.write(record[0] + ',' + record[3] + '\n')


if __name__ == '__main__':
    if not os.path.isdir('../dataset'):
        try:
            os.makedirs('../dataset')
        except OSError as err:
            raise SystemExit(err)

    download_bitcoin_price(2021)

    for day in range(1, 14):
        # Download all blocks in a day in '../dataset/blocks_*.txt'
        file_id = download_block_of_day(2021, 11, day, 0, 0, 0)
        # Download all transactions in a day in '../dataset/transactions_*.txt' based on block_*.txt
        download_transactions_in_block(file_id)
