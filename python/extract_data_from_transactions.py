import gzip
import json
import bisect


def get_price_in_minute():
    with open('../dataset/BTC_USD_2021_minute.csv') as file:
        records = [record.split(',') for record in file.readlines()]
    records = [(int(record[0]), float(record[1])) for record in records]
    records.reverse()
    return records


def extract_data_from_transactions(price_in_minute, year, month, day):
    date = f"{year}" + str(month).zfill(2) + str(day).zfill(2)
    with gzip.open(f'../dataset/transactions_{date}.txt.gz') as input_file:
        transactions = json.load(input_file)
    print(f'Found {len(transactions)} transactions')
    price_in_minute_timetamps = [x[0] for x in price_in_minute]

    time_value_pair = []
    for transaction in transactions:
        transaction_id = transaction['hash']
        transaction_time = int(transaction['time'])
        inputs = transaction['inputs']
        outputs = transaction['out']

        idx = bisect.bisect_left(price_in_minute_timetamps, transaction_time)
        btc_price = price_in_minute[idx][1]
        transaction_value_in_usd = sum([x['value'] for x in outputs]) / 1e8 * btc_price
        time_value_pair.append((transaction_time, transaction_value_in_usd))
    return time_value_pair


if __name__ == '__main__':
    price_in_minute = get_price_in_minute()

    for i in range(1, 14):
        time_value_pair = extract_data_from_transactions(price_in_minute, 2021, 11, i)
        with open(f'../dataset/data_202111{str(i).zfill(2)}.txt', 'w') as output_file:
            for t, v in time_value_pair:
                output_file.write("{} {}\n".format(t, v))
