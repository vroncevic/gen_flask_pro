# -*- coding: UTF-8 -*-
# __init__.py
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


class BaseProject(object):
    """
        Define class BaseProject with attribute(s) and method(s).
        BaseProject is super class for project info.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __name - Name of project
                __schema_path - Path of schema file (json) - project structure
                __schema - Schema object in json format
            method:
                __init__ - Initial constructor
                set_name - Getting/Setting project name
                schema_path - Getting/Setting absolute path of template
                schema - Getting/Setting schema object with project structure
    """

    __slots__ = (
        'VERBOSE',
        '__name',
        '__schema_path',
        '__schema'
    )
    VERBOSE = 'FLASK_PRO::PROJECT::BASE_PROJECT'

    def __init__(self, verbose=False):
        """
            Initial constructor.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(BaseProject.VERBOSE, verbose, 'Initial base project')
        self.__name = None
        self.__schema_path = None
        self.__schema = None

    @property
    def name(self):
        """
            Public property getter.
            :return: Name of project | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
            Setting project name.
            :param name: Name of project
            :type name: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        name_txt = 'Argument: expected name <str> object'
        name_msg = "{0} {1} {2}".format('def', func, name_txt)
        if name is None or not name:
            raise ATSBadCallError(name_msg)
        if not isinstance(name, str):
            raise ATSTypeError(name_msg)
        self.__name = name

    @property
    def schema_path(self):
        """
            Public property getter.
            :return: Path of schema file with project structure | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        """
        return self.__schema_path

    @schema_path.setter
    def schema_path(self, schema_path):
        """
            Setting schema path.
            :param schema_path: Path of schema file with project structure
            :type schema_path: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        schema_path_txt = 'Argument: expected schema_path <str> object'
        schema_path_msg = "{0} {1} {2}".format('def', func, schema_path_txt)
        if schema_path is None or not schema_path:
            raise ATSBadCallError(schema_path_msg)
        if not isinstance(schema_path, str):
            raise ATSTypeError(schema_path_msg)
        self.__schema_path = schema_path

    @property
    def schema(self):
        """
            Public property getter.
            :return: Schema object with project structure | None
            :rtype: <dict> | <NoneType>
            :exceptions: None
        """
        return self.__schema

    @schema.setter
    def schema(self, schema):
        """
            Setting schema for project.
            :param schema: Schema object with project structure
            :type schema: <dict>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        schema_txt = 'Argument: expected schema <dict> object'
        schema_msg = "{0} {1} {2}".format('def', func, schema_txt)
        if schema is None or not schema:
            raise ATSBadCallError(schema_msg)
        if not isinstance(schema, dict):
            raise ATSTypeError(schema_msg)
        self.__schema = schema

