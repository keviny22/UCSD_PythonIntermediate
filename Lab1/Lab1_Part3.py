# Python II – Lab 1 – Kevin Young

def calculate_interest(principal: float, interest_rate: float) -> float:
    interest = principal * (interest_rate/100)
    return interest


if __name__ == '__main__':
    principal: float = float(input('Enter the principal amount (ex: 1000.00): '))
    interest_rate: float  = float(input('Enter interest rate percentage (ex: 4.5): '))
    term: int = int(input('Enter term in years (ex: 10): '))

    print(f"{'Year':<5}{'Interest':<12}{'Balance':<12}")
    print("============================")

    balance: float = principal
    for x in range(0, term):
        interest = calculate_interest(balance, interest_rate)
        balance = interest + balance
        print(f"{x + 1:>2}{'$':>4}{interest:>8,.2f}{'$':>4}{balance:>10,.2f}")


