OK_FORMAT = True
test = {
  'name': 'q52',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> inventory.sort(0).column(0).item(0)
          25274
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
