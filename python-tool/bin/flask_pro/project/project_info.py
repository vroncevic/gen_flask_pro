# -*- coding: UTF-8 -*-
# project_info.py
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
    from flask_pro.project import BaseProject
    from ats_utilities.config.json.json2object import Json2Object
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


class ProjectInfo(BaseProject):
    """
        Define class ProjectInfo with attribute(s) and method(s).
        Loading project configuration - structure (schema) from json file.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
            method:
                __init__ - Initial constructor
                load_schema - Loading schema with project configuration
    """

    __slots__ = ('VERBOSE')
    VERBOSE = 'FLASK_PRO::PROJECT::PROJECT_INFO'

    def __init__(self, project_name, project_config_file, verbose=False):
        """
            Initial constructor.
            :param project_name: Project name
            :type project_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        project_name_txt = 'Argument: expected project_name <str> object'
        project_name_msg = "{0} {1} {2}".format('def', func, project_name_txt)
        project_cfg_txt = 'Argument: expected project_config_file <str> object'
        project_cfg_msg = "{0} {1} {2}".format('def', func, project_cfg_txt)
        if project_name is None or not project_name:
            raise ATSBadCallError(project_name_msg)
        if not isinstance(project_name, str):
            raise ATSTypeError(project_name_msg)
        if project_config_file is None or not project_config_file:
            raise ATSBadCallError(project_cfg_msg)
        if not isinstance(project_config_file, str):
            raise ATSTypeError(project_cfg_msg)
        verbose_message(ProjectInfo.VERBOSE, verbose, 'Initial project info')
        BaseProject.__init__(self, verbose=verbose)
        self.name = project_name
        self.schema_path = project_config_file

    def load_schema(self, verbose=False):
        """
            Loading schema with project configuration from json file.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Configuration object | None
            :rtype: <Python object(s)> | <NoneType>
            :exceptions: None
        """
        verbose_message(
            ProjectInfo.VERBOSE, verbose, 'Loading project configuration'
        )
        schema_loader = Json2Object(self.schema_path)
        self.schema = schema_loader.read_configuration(verbose=verbose)
        schema_not_empty = bool(self.schema)
        return self.schema if schema_not_empty else None

