from PiIterator import LeibnizPiIterator, iterations, pi50, NilakanthaPiGenerator
from Converter import *

if __name__ == '__main__':
    print(f"\nPart I")
    print(f"==================================")
    counter = 0
    for x in LeibnizPiIterator():
        counter += 1
        if counter >= iterations: break
    print(f"\nLeibnizPi after {counter} iterations: {x:.50f}")
    diff = pi50 - x
    print(f"Difference: {diff:0.50f}")

    print(f"\nPart II")
    print(f"==================================")
    counter = 0
    for x in NilakanthaPiGenerator.NilakanthaPiGenerator():
        counter += 1
        if counter >= 100000: break
    print(f"\nNilakanthaPi after {counter} iterations: {x:.50f}")
    diff = pi50 - x
    print(f"Difference: {diff:0.50f}")

    counter = 0
    for x in NilakanthaPiGenerator.NilakanthaPiGenerator():
        counter += 1
        if counter >= 10000000: break
    print(f"\nNilakanthaPi after {counter} iterations: {x:.50f}")
    diff = pi50 - x
    print(f"Difference: {diff:0.50f}")

    print(f"\nPart III")
    print(f"==================================")


    print(f"\nConvert 2 miles to inches (result: 126720)")
    convertMilesToInches = Converter.compose(Converter.milesToYards, Converter.yardsToFeet, Converter.feetToInches)
    print(convertMilesToInches(2))

    print(f"\nConvert 5 feet to meters (result: 1.524)")
    convertFeetToMeters = Converter.compose(Converter.feetToInches, Converter.inchesToCm, Converter.cmToMeters)
    print(convertFeetToMeters(5))

    print(f"\nConvert 1 meter to inches (result: 39.37007874015748)")
    convertMeterToInches = Converter.compose(Converter.metersToCm, Converter.cmToInches)
    print(convertMeterToInches(1))

    print(f"\nConvert 10 miles to kilometers (result: 16.09344)")
    convertMilesToKM = Converter.compose(Converter.milesToYards,
                                         Converter.yardsToFeet,
                                         Converter.feetToInches,
                                         Converter.inchesToCm,
                                         Converter.cmToMeters,
                                         Converter.metersToKm)
    print(convertMilesToKM(10))

    print(f"\nConvert 1 kilometer to miles (result: 0.6213711922373341)")
    convertKmToMiles = Converter.compose(Converter.kmToMeters,
                                         Converter.metersToCm,
                                         Converter.cmToInches,
                                         Converter.inchesToFeet,
                                         Converter.feetToYards,
                                         Converter.yardsToMiles)
    print(convertKmToMiles(1))

    print(f"\nConvert 12.7 kilometers to inches (result: 500000.0)")
    convertKmToInches = Converter.compose(Converter.kmToMeters,
                                          Converter.metersToCm,
                                          Converter.cmToInches)
    print(convertKmToInches(12.7))

    print(f"\nConvert 500000 inches to kilometers (result: 12.7)")
    convertInchesToKM = Converter.compose(Converter.inchesToCm,
                                          Converter.cmToMeters,
                                          Converter.metersToKm)
    print(convertInchesToKM(500000))

    print(f"\nConvert 9,460,730,472,580,800 meters to light years (result: 1)")
    convertInchesToKM = Converter.compose(Converter.metersToKm, Converter.kmToAu, Converter.auToLy)
    print(convertInchesToKM(9460730472580800))
