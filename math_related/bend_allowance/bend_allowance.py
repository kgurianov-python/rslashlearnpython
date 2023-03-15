"""
https://www.reddit.com/r/learnpython/comments/11ryws6/comment/jcb3340/?context=3

Bend Allowance = Angle * (PI / 180) * (Radius + K-factor * Thickness)
"""
import math
from typing import NamedTuple


class Limits(NamedTuple):
    """ Provide means to limits for user input"""
    low: float
    high: float

    def __str__(self):
        return f"{self.low} ... {self.high} "


def get_user_float_value(msg: str, limits: Limits) -> float:
    """
    Get user impuit and validtes it agaist the limit of lower and higher values
    :param msg: Tesxt message to display
    :type msg: str
    :param limits: Defined lowe r anf higher bounds acceptable for the inout value
    :type limits: Limits
    :rtype float
    :return User provided value
    """
    while True:
        result = float(input(f"{msg}: "))
        if limits is not None and not (limits.low < result < limits.high):
            print(f"Provided value {result} is outside of limits {limits} \nTry again.")
            continue
        else:
            break

    return result


def get_user_input() -> tuple[float, float, float, float]:
    """
    Get user inputs
    """
    angle = get_user_float_value("Please provide angle, in degrees", Limits(0, 180))
    radius = get_user_float_value("Please provide bend radius, in mm", None)
    thickness = get_user_float_value("Please provide material thickness, in mm", None)
    kfactor = get_user_float_value("Please provide material kfactor, value between 0 and 1", Limits(0, 1))

    return angle, radius, thickness, kfactor


def calc_bend_allowance(angle: float, radius: float, thickness: float, kfactor: float) -> float:
    """
    Bend Allowance = Angle * (PI / 180) * (Radius + K-factor * Thickness)
    """
    return (angle * (math.pi / 180)) * (radius + (kfactor * thickness))


def main():
    """ A main function"""
    values = get_user_input()
    print(f"Resulted bend allowance is {calc_bend_allowance(*values):.4} mm")


if __name__ == '__main__':
    main()
