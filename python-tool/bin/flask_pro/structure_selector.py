# -*- coding: UTF-8 -*-
# structure_selector.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# gen_flask_pro is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gen_flask_pro is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2018, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class StructureSelector(object):
    """
        Define class StructureSelector with attribute(s) and method(s).
        Selecting type of project structure.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                Functional - 0 Standard type of Flask project structure
                Divisional - 1 Flask project structure divided in divisions
                Modular    - 2 Flask project structure based on modules
                Cancel     - 3 Cancel option
                __STRUCTURES - Dict representation of structures
            method:
                choose_structure - Selecting type of project structure
    """

    __slots__ = (
        'VERBOSE',
        'Functional',
        'Divisional',
        'Modular',
        'Cancel',
        '__STRUCTURES'
    )
    VERBOSE = 'FLASK_PRO::STRUCTURE_SELECTOR'
    Functional, Divisional, Modular, Cancel = range(4)
    __STRUCTURES = {
        Functional: 'Functional structure',
        Divisional: 'Divisional structure',
        Modular: 'Modular structure',
        Cancel: 'Cancel'
    }

    @classmethod
    def choose_structure(cls):
        """
            Choose project structure
            :return: BaseProject structure type
            :rtype: <int>
            :exceptions: None
        """
        print("\n Structure option list:")
        for key in sorted(StructureSelector.__STRUCTURES):
            print("  {0} {1}".format(key, StructureSelector.__STRUCTURES[key]))
        while True:
            module_type = input(" Select structure: ")
            if module_type not in StructureSelector.__STRUCTURES.keys():
                print(" Not an appropriate choice.")
            else:
                break
        return module_type

