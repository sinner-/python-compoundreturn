#!/usr/bin/env python
from argparse import ArgumentParser
import locale

def compound(initial_equity, compound_rate, duration_years):

  compounded_equity = initial_equity

  for year in range(1,duration_years):
    annual_return = compounded_equity * compound_rate
    compounded_equity = compounded_equity + annual_return

  return compounded_equity

if __name__ == '__main__':
  parser = ArgumentParser(description='Compound return calculator.')
  parser.add_argument('initial_equity', type=int, help='Initial equity value, e.g. 100 for $100.')
  parser.add_argument('compound_rate', type=float, help='Forecast compounding rate per annum, e.g. 0.1 for 10 percent.')
  parser.add_argument('duration_years', type=int, help='Duration of investment in years.')
  args = parser.parse_args()

  locale.setlocale(locale.LC_ALL, '')

  final_equity = compound(args.initial_equity, args.compound_rate, args.duration_years)

  print 'The compounded value of %s after %d years at %d%% rate is: %s.' % (locale.currency(args.initial_equity, grouping=True), args.duration_years, args.compound_rate * 100, locale.currency(final_equity, grouping=True))
