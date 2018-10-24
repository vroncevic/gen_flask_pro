# -*- coding: UTF-8 -*-
# base_builder.py
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

try:
    from flask_pro.project.project_info import ProjectInfo
    from ats_utilities.abstract import abstract_method
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


class Builder(object):
    """
        Define class Builder with attribute(s) and method(s).
        Abstract class Builder modular.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                project - Project product object
            method:
                __init__ - Initial constructor
                new_project - Create new BaseProject object
                generate_structure - Generate project (Abstract method)
    """

    __slots__ = ('VERBOSE', 'project')

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(Builder.VERBOSE, verbose, 'Initial base builder')
        self.project = None

    def new_project(self, project_name, project_schema_path):
        """
            Create new BaseProject object
            :param project_name: Enable/disable verbose option
            :type project_name: <str>
            :param project_schema_path: 
            :type project_schema_path: 
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, status = stack()[0][3], False
        project_name_txt = 'Argument: expected project_name <str> object'
        project_name_msg = "{0} {1} {2}".format('def', func, project_name_txt)
        pro_sch_txt = 'Argument: expected project_schema_path <str> object'
        pro_sch_msg = "{0} {1} {2}".format('def', func, pro_sch_txt)
        if project_name is None or not project_name:
            raise ATSBadCallError(project_name_msg)
        if not isinstance(project_name, str):
            raise ATSTypeError(project_name_msg)
        if structure_type is None or not structure_type:
            raise ATSBadCallError(project_name_msg)
        if not isinstance(structure_type, int):
            raise ATSTypeError(project_name_msg)
        self.project = ProjectInfo(project_name, project_schema_path)

    @abstract_method
    def generate_structure(self):
        """
            Generate project (Abstract method)
        """
        pass

