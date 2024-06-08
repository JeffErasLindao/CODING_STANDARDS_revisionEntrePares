import builtins


class myclass:
    def __init__(self):
        self.my_fav = {'Paris': 500, 'New York City': 600}

    def get_extra_cost(self, dist):
        return self.my_fav.get(dist, 0)

    def valid_this(self, dist):
        if dist not in ['Paris', 'New York City']:
            raise builtins.ValueError(f"Destination '{dist}' not supported")
        return True


class passanger:
    def __init__(self, num):
        self.num = num

    def valid_number(self):
        if not isinstance(self.num, int) or not 0 < self.num <= 80:
            raise ValueError("Error: El número de pasajeros debe ser un entero"
                             "entre 1 y 80.")
        return True

    def discount_for_passenger(self):
        if not isinstance(self.num, int):
            raise ValueError("Error: El número de pasajeros debe ser entero")
        if 4 < self.num < 10:
            return 0.1
        elif self.num >= 10:
            return 0.2
        else:
            return 0.0


class TotalTime:
    def __init__(self, dur):
        self.dur = dur

    def is_valid_total_time(self):
        if not isinstance(self.dur, int) or self.dur <= 0:
            raise ValueError("Error: La duración total debe ser un "
                             "entero mayor que cero.")
        return True

    def get_fee(self):
        if not self.is_valid_total_time():
            return 0
        return 200 if self.dur < 7 else 0

    def get_promotion_policy(self):
        if not self.is_valid_total_time():
            return 0
        return 200 if self.dur > 30 else 0


class Vacation:
    base_cost = 1000

    def __init__(self, dist, num, dur):
        self.myclass = myclass()
        self.passanger = passanger(num)
        self.totaltime = TotalTime(dur)
        self.dist = dist

    def sum(self):
        try:
            if not self.myclass.valid_this(self.dist):
                return -1
            if not self.passanger.valid_number():
                return -1
            if not self.totaltime.is_valid_total_time():
                return -1
        except ValueError as e:
            print(f"Error: {e}")
            return -1
        subtotal = self.base_cost
        subtotal += self.myclass.get_extra_cost(self.dist)
        subtotal += self.totaltime.get_fee()
        subtotal -= self.totaltime.get_promotion_policy()

        discount = self.passanger.discount_for_passenger()
        subtotal -= subtotal * discount

        return max(int(subtotal), 0)


def main():
    # Inputs
    dist = "Paris"
    num = 4
    dur = 25

    # Calculate vacation package cost
    calculator = Vacation(dist, num, dur)
    cost = calculator.sum()

    # Outputs
    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")


if __name__ == "__main__":
    main()