OK_FORMAT = True
test = {
  'name': 'q33',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(correct_products, np.array([66234, 6661248, 66900162648, -394250]))
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
