# -*- coding: UTF-8 -*-
# modular_builder.py
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
from inspect import stack

try:
    from flask_pro.project_builder.base_builder import Builder
    from ats_utilities.console_io.verbose import verbose_message
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


class ModularBuilder(Builder):
    """
        Define class ModularBuilder with attribute(s) and method(s).
        
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
            method:
                __init__ - Initial constructor
                generate_structure - Generate project structure
    """

    __slots__ = ('VERBOSE')
    VERBOSE = 'FLASK_PRO::MODULAR_BUILDER'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            ModularBuilder.VERBOSE, verbose, 'Initial modular builder'
        )
        super(ModularBuilder, self).__init__()
        self.new_project()

    def generate_structure(self, project_name, project_schema_path):
        """
            :param project_name: BaseProject name (root folder)
            :type project_name: <str>
            :param project_schema_path: Absolute path of schema
            :type project_schema_path: <str>
            :return: Boolean status, return True (success) else False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, status = stack()[0][3], False
        project_name_txt = 'Argument: expected project_name <str> object'
        project_name_msg = "{0} {1} {2}".format('def', func, project_name_txt)
        schema_path = 'Argument: expected project_schema_path <str> object'
        schema_path_msg = "{0} {1} {2}".format('def', func, schema_path)
        if project_name is None or not project_name:
            raise ATSBadCallError(project_name_msg)
        if not isinstance(project_name, str):
            raise ATSTypeError(project_name_msg)
        if project_schema_path is None or not project_schema_path:
            raise ATSBadCallError(schema_path_msg)
        if not isinstance(project_schema_path, str):
            raise ATSTypeError(schema_path_msg)
        self.project.prepare_structure(project_name, project_schema_path)
        status = self.project.load_schema()
        return True if status else False

