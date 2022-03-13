
class IntToRoman:
    def __init__(self):
        pass

    @staticmethod
    def to_roman(num: int) -> str:
        """
        Convert integer to roman
        :param num: number to be converted to roman
        :return: roman equivalent of the num
        """
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        to_thousand = thousands[num // 1000]
        to_hundred = hundreds[(num % 1000) // 100]
        to_ten = tens[(num % 100) // 10]
        to_one = ones[num % 10]

        return to_thousand + to_hundred + to_ten + to_one


if __name__ == "__main__":
    # Demo usage
    IntToRoman.to_roman(9)
