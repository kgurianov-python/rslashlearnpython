import itertools

teams = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
teams = ['01', '02', '03', '04']
match_possibilities = itertools.combinations(teams, 2)
round_possibilities = itertools.combinations(match_possibilities, int(len(teams)/2))

print(teams)
print(f"{list(match_possibilities)=}")
print(*round_possibilities)
