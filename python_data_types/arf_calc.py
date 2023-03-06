from math import inf

BASE = 20000
BASE_RATES = [1, 1.4, 1.9, 2.5, 3.2]
CAR_ARF_RATES_POST_FEB_15 = {20000: 1.0, 40000: 1.4, 60000: 1.9, 80000: 2.5, float(inf): 3.2}
CAR_ARF_RATES_PRE_FEB_15 = {20000: 1.0, 50000: 1.4, 80000: 1.8, float(inf): 2.2}
MOTO_ARF_RATES = {5000: 0.15, 10000: 0.5, float(inf): 1.0}


def calc_arf_formula(omv: float, formula: {float: float}) -> float:
    result = 0.0
    lower_limit = 0.0
    omv_remainder = omv
    for higher_limit, tax in formula.items():
        taxable_body = min(omv_remainder, higher_limit - lower_limit)
        result += taxable_body * tax

        omv_remainder = max(0.0, omv_remainder - taxable_body)
        if omv_remainder <= 0.0:
            break

        lower_limit = higher_limit

    return result


def calc_arf(omv: float) -> float:
    print(f"Calculating for {omv}:")
    if omv <= BASE:
        return omv
    result = 0
    rate_index = 0
    while rate_index < len(BASE_RATES) - 1 and omv > BASE:
        result += BASE * BASE_RATES[rate_index]
        omv = omv - BASE
        rate_index += 1

    result += omv * BASE_RATES[rate_index]
    return result

cost = 90000

print(calc_arf(cost))
print(calc_arf_formula(cost, CAR_ARF_RATES_POST_FEB_15))
print(calc_arf_formula(cost, CAR_ARF_RATES_PRE_FEB_15))
print(calc_arf_formula(cost, MOTO_ARF_RATES ))
