OK_FORMAT = True
test = {
  'name': 'q21',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you wrote:;
          >>> #   some_numbers.item(3);
          >>> # But the third element has index 2, not 3.;
          >>> third_element != -10
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> third_element
          -6
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
