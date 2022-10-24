class Minimum(object):
    def minimum_number(self, vals):
        minimum = int(vals[0])

        for value in vals:
            if value < minimum:
                minimum = value
        return minimum

    def is_integer(self, vals):
        numbers = [int(number) for number in vals]

        return numbers


if __name__ == '__main__':
    min = Minimum()
