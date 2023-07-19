from typing import List


class Car:
    def __init__(self, size: str, color: str, type: str):
        self._size = size
        self._color = color
        self._type = type

    def describe(self):
        return f"{self._size} {self._color} {self._type}"


class ParkingLot:
    def __init__(self, number_of_spots: int):
        self._parking_spots: List[Car] = [None for _ in range(number_of_spots)]

    def park_car(self, car: Car, parking_spot: int):
        next_available_spot = self.find_next_available(parking_spot)
        if self._parking_spots[next_available_spot] is not None:
            self._parking_spots[next_available_spot] = car

    def remove_car(self, parking_spot: int):
        if not self.isSpotEmpty(parking_spot):
            self._parking_spots[parking_spot] = None

    def print_parking_spot(self, parking_spot: int):
        if not self.isSpotEmpty(parking_spot):
            return self._parking_spots[parking_spot].describe()

        return "Empty"

    def print_all_free_parking_spots(self):
        total_free_spots = 0
        for parking_spot in self._parking_spots:
            if self._parking_spots[parking_spot] is None:
                total_free_spots += 1
        return total_free_spots

    def find_next_available(self, current_spot):
        n = len(self._parking_spots)
        last_spot = n + current_spot

        while current_spot < last_spot:
            if self.isSpotEmpty(current_spot):
                break
            current_spot += 1

        return current_spot

    def isSpotEmpty(self, parking_spot):
        return self._parking_spots[parking_spot] is None


def parking_system(n: int, instructions: List[List[str]]) -> List[str]:
    return []


if __name__ == "__main__":
    n = int(input())
    instructions = [input().split() for _ in range(int(input()))]
    res = parking_system(n, instructions)
    for line in res:
        print(line)
