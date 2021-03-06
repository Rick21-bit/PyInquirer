# -*- coding: utf-8 -*-
import textwrap

from .helpers import create_example_fixture, keys


example_app = create_example_fixture('examples/checkbox.py')


def test_checkbox(example_app):
    example_app.expect(textwrap.dedent("""\
        š Select toppings  (<up>, <down> to move, <space> to select, <a> to toggle, <i>
          = The Meats =
         āÆā Ham
          ā Ground Meat
          ā Bacon
          = The Cheeses =
          ā Mozzarella
          ā Cheddar
          ā Parmesan
          = The usual =
          ā Mushroom
          ā Tomato
          ā Pepperoni
          = The extras =
          ā Pineapple
          - Olives (out of stock)
          ā Extra cheese"""))
    example_app.write(' ')
    example_app.expect('\n\nā ')
    example_app.write(keys.ENTER)
    example_app.expect(textwrap.dedent("""\
        š Select toppings  done (2 selections)
        {'toppings': ['Ham', 'Mozzarella']}
        """))
