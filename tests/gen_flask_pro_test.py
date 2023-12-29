# -*- coding: UTF-8 -*-

'''
Module
    gen_flask_pro_test.py
Copyright
    Copyright (C) 2016 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_flask_pro is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_flask_pro is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class GenFlaskProTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenFlaskPro.
Execute
    python3 -m unittest -v gen_flask_pro_test
'''

import sys
from typing import List
from os import makedirs, rmdir
from unittest import TestCase, main

try:
    from gen_flask_pro import GenFlaskPro
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_flask_pro'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_flask_pro/blob/dev/LICENSE'
__version__ = '1.2.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenFlaskProTestCase(TestCase):
    '''
        Defines class GenFlaskProTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenFlaskPro.
        GenFlaskPro unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create is not None.
                | test_missing_args - Missing args.
                | test_process - Generate project.
                | test_tool_not_operational - Generate project not operational.
                | test_pro_already_exists - Generate already existing project.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create is not None'''
        generator: GenFlaskPro = GenFlaskPro()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Missing args'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_flask_pro_run.py')
        generator: GenFlaskPro = GenFlaskPro()
        self.assertFalse(generator.process())

    def test_wrong_arg(self) -> None:
        '''Generate project'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_flask_pro_run.py')
        sys.argv.insert(2, '-d')
        sys.argv.insert(3, 'wrong')
        generator: GenFlaskPro = GenFlaskPro()
        self.assertFalse(generator.process())

    def test_process(self) -> None:
        '''Generate project'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_flask_pro_run.py')
        sys.argv.insert(2, '-g')
        sys.argv.insert(3, 'latest')
        generator: GenFlaskPro = GenFlaskPro()
        self.assertTrue(generator.process())

    def test_tool_not_operational(self) -> None:
        '''Generate project not operational'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_flask_pro_run.py')
        sys.argv.insert(2, '-g')
        sys.argv.insert(3, 'fresh')
        generator: GenFlaskPro = GenFlaskPro()
        generator.tool_operational = False
        self.assertFalse(generator.process())

    def test_pro_already_exists(self) -> None:
        '''Generate already existing project'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_flask_pro_run.py')
        sys.argv.insert(2, '-g')
        sys.argv.insert(3, 'fresh_new')
        generator: GenFlaskPro = GenFlaskPro()
        makedirs('fresh_new')
        self.assertFalse(generator.process())
        rmdir('fresh_new')


if __name__ == '__main__':
    main()
