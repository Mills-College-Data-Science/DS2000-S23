OK_FORMAT = True
test = {
  'name': 'q56',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If you're stuck, here's a hint: You want to multiply the count;
          >>> # sold in each box by the per-item price of fruits in that box.;
          >>> # You can use elementwise multiplication for that.;
          >>> # Then you want the sum of those products.  Use sum().;
          >>> np.isclose(total_revenue, 106.85)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
