JSON_A = [{"Id": 12345, "SeqNumber": "759860", "SchoolName": "GHS", "ClgName": "IITKGP", "AccountNumber": "ACC1234"},
          {"Id": 12345, "SeqNumber": "759862", "SchoolName": "LFS", "ClgName": "VTU", "AccountNumber": "ACC5678"}]

JSON_B = [{"info": {"account_number": "ACC1234", "created_dt": "2022-03-11T17:33:38Z", "_id": "12345",
                    "system_id": "SYS12345", "status": "active"}},
          {"info": {"account_number": "ACC5678", "created_dt": "2022-03-11T17:33:37Z", "_id": "12345",
                       "system_id": "SYS12345",
                       "status": "active"}},
          {"info": {"account_number": "ACC5671011", "created_dt": "2022-03-11T17:33:37Z", "_id": "12345",
                    "system_id": "SYS12345",
                    "status": "active"}}]


def main():
    print(f'{type(JSON_A)=}')
    print(f'{type(JSON_B)=}')

    accounts_a = [item['AccountNumber'] for item in JSON_A]
    accounts_b = [element['account_number'] for element in [item['info'] for item in JSON_B]]
    print(f'{accounts_a=}')
    print(f'{accounts_b=}')

    print(f'Lists Intersection: {accounts_a or accounts_b}')

    intersection = [item for item in set(accounts_a + accounts_b) if (item in accounts_a) and (item in accounts_b) ]
    print(f'Intersection from comprehension: {intersection}: ')

    diff = [item for item in set(accounts_a + accounts_b) if (item not in accounts_a) or (item not in accounts_b) ]
    print(f'Diff: {diff}')



if __name__ == '__main__':
    main()

