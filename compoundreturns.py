#!/usr/bin/env python
""" Compound return calculator. """
from argparse import ArgumentParser
import locale

def compound(initial_equity, compound_rate, duration_years):
    """Calculates the compound return.

    Args:
        initial_equity (int): Initial equity value, e.g. 100.
        compound_rate (float): Compounding rate per annum, e.g. 0.1.
        duration_years (int): Duration of investment in years.

    Yields:
        compounded_equity (float): Final value of compounded equity.

    Examples:
        >>> print compound(1000, 0.1, 25)
        ["The value of $1,000.00 after 25 years at 10% rate is: $9,849.73."]
    """

    compounded_equity = initial_equity

    for _ in range(1, duration_years):
        annual_return = compounded_equity * compound_rate
        compounded_equity = compounded_equity + annual_return

    return compounded_equity

def main():
    """Main program function."""

    parser = ArgumentParser(description='Compound return calculator.')
    parser.add_argument('initial_equity', type=int,
                            help='Initial equity value, e.g. 100.')
    parser.add_argument('compound_rate', type=float,
                            help='Compounding rate per annum, e.g. 0.1.')
    parser.add_argument('duration_years', type=int,
                            help='Duration of investment in years.')
    args = parser.parse_args()

    locale.setlocale(locale.LC_ALL, '')

    final_equity = compound(args.initial_equity,
                            args.compound_rate,
                            args.duration_years)

    print ('The value of %s after %d years at %d%% rate is: %s.' %
               (locale.currency(args.initial_equity, grouping=True),
                args.duration_years,
                args.compound_rate * 100,
                locale.currency(final_equity, grouping=True)))

if __name__ == '__main__':
    main()
