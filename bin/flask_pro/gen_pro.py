# -*- coding: UTF-8 -*-
# gen_pro.py
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

import sys
from os.path import dirname, realpath
from inspect import stack

try:
    from flask_pro.structure_selector import StructureSelector
    from flask_pro.divisional.divisional_builder import DivisionalBuilder
    from flask_pro.functional.functional_builder import FunctionalBuilder
    from flask_pro.modular.modular_builder import ModularBuilder
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.success import success_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2018, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class GenPro(object):
    """
        Define class GenPro with attribute(s) and method(s).
        Generate Flask project structure.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __TEMPLATE_DIR - Template dir location
                __STRUCTURAL_SCHEMES - Schemas
                __builder - Base project builder
            method:
                __init__ - Initial constructor
                __macro_builder - Invoke builder generator method
                gen_pro - Prepare project structure parameters
    """

    __slots__ = (
        'VERBOSE',
        '__TEMPLATE_DIR',
        '__STRUCTURAL_SCHEMES',
        '__builder'
    )
    VERBOSE = 'FLASK_PRO::GEN_PRO'
    __TEMPLATE_DIR = '/../../conf/template'
    __STRUCTURAL_SCHEMES = {
        StructureSelector.Functional : 'struct_function.json',
        StructureSelector.Divisional : 'struct_division.json',
        StructureSelector.Modular : 'struct_module.json'
    }

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(GenPro.VERBOSE, verbose, 'Initial Flask project')
        self.__builder = None

    def __macro_builder(self, project_name, structure_type, verbose=False):
        """
            Invoke builder generator method.
            :param project_name: Project name
            :type project_name: <str>
            :param structure_type: Project structure type
            :type structure_type: <int>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Boolean status
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, status = stack()[0][3], False
        project_name_txt = 'Argument: expected project_name <str> object'
        project_name_msg = "{0} {1} {2}".format('def', func, project_name_txt)
        structure_type_txt = 'Argument: expected structure_type <str> object'
        structure_type_msg = "{0} {1} {2}".format(
            'def', func, structure_type_txt
        )
        if project_name is None or not project_name:
            raise ATSBadCallError(project_name_msg)
        if not isinstance(project_name, str):
            raise ATSTypeError(project_name_msg)
        if structure_type is None or not structure_type:
            raise ATSBadCallError(project_name_msg)
        if not isinstance(structure_type, int):
            raise ATSTypeError(project_name_msg)
        if structure_type == StructureSelector.Divisional:
            self.__builder = DivisionalBuilder()
        elif structure_type == StructureSelector.Functional:
            self.__builder = FunctionalBuilder()
        elif structure_type == StructureSelector.Modular:
            self.__builder = ModularBuilder()
        else:
            return status
        local_dir = dirname(realpath(__file__))
        structure_schema_path = "{0}{1}/{2}".format(
            local_dir, GenPro.__TEMPLATE_DIR,
            GenPro.__STRUCTURAL_SCHEMES[structure_type]
        )
        status = self.__builder.generate_structure(
            project_name, structure_schema_path
        )
        return True if status else False

    def gen_pro(self, project_name, verbose=False):
        """
            Prepare project structure parameters.
            :param project_name: Project name
            :type project_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Boolean status
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, status = stack()[0][3], False
        project_name_txt = 'Argument: expected project_name <str> object'
        project_name_msg = "{0} {1} {2}".format('def', func, project_name_txt)
        if project_name is None or not project_name:
            raise ATSBadCallError(project_name_msg)
        if not isinstance(project_name, str):
            raise ATSTypeError(project_name_msg)
        structure_type = StructureSelector.choose_structure()
        if structure_type != StructureSelector.Cancel:
            if structure_type in GenPro.__STRUCTURAL_SCHEMES.keys():
                verbose_message(
                    GenPro.VERBOSE, verbose, 'Generating project', project_name
                )
                status = self.__macro_builder(project_name, structure_type)
            else:
                error_message(GenPro.VERBOSE, 'Failed to select structure!')
        return True if status else False

