from functools import reduce


class Converter:
    # def compose(f, g):
    #     def a(x):
    #         return g(f(x))
    #     return a
    def compose(*functions):
        return reduce(lambda f, g: lambda x: g(f(x)), functions)

    def milesToYards(value):
        """
        Converts miles to yards 1760
        """
        return value * 1760

    def yardsToMiles(value):
        """
        Inverse of milesToYards 0.0005681818181818
        """
        return value * 0.0005681818181818

    def yardsToFeet(value):
        """
        Converts yards to feet 3
        """
        return value * 3

    def feetToYards(value):
        """
        Inverse of yardsToFeet 0.3333333333333333
        """
        return value * 0.3333333333333333

    def feetToInches(value):
        """
        Converts feet to inches 12
        """
        return value * 12

    def inchesToFeet(value):
        """
        Inverse of feetToInches 0.0833333333333333
        """
        return value * 0.0833333333333333

    def inchesToCm(value):
        """
        Converts inches to centimeters 2.54
        """
        return value * 2.54

    def cmToInches(value):
        """
        Inverse of inchesToCm 0.3937007874015748
        """
        return value * 0.3937007874015748

    def cmToMeters(value):
        """
        Converts centimeters to meters 0.01
        """
        return value * 0.01

    def metersToCm(value):
        """
        Inverse of cmToMeters 100
        """
        return value * 100

    def metersToKm(value):
        """
        Converts meters to kilometers 0.001
        """
        return value * 0.001

    def kmToMeters(value):
        """
        Inverse of metersToKm 1000
        """
        return value * 1000

    def kmToAu(value):
        """
        Converts kilometers to astronomical units (average distance from Earth to Sun) 6.68459E-09
        """
        return value * 0.000000006684587122268445

    def auToKm(value):
        """
        Inverse of kmToAu 149597870.700
        """
        return value * 149597870.700

    def auToLy(value):
        """
        Converts AUs to light years (distance light travels in a year in a vacuum) 1.58125E-05
        """
        return value * 0.00001581250740982065847572

    def lyToAu(value):
        """
        Inverse of auToLy 63241.07708426628026865358
        """
        return value * 63241.07708426628026865358