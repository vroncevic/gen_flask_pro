# -*- coding: UTF-8 -*-
# read_template.py
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
    from pathlib import Path

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


class ReadTemplate(object):
    """
        Define class ReadTemplate with attribute(s) and method(s).
        Read a template file and return a template content.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __TEMPLATE_DIR - Prefix path to templates
                __template_dir - Absolute template dir path
            method:
                __init__ - Initial constructor
                read - Read a template and return a content or None
    """

    __slots__ = ('VERBOSE', '__TEMPLATE_DIR', '__template_dir')
    VERBOSE = 'GEN_PRO::READ_TEMPLATE'
    __TEMPLATE_DIR = '../../conf/template/'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(ReadTemplate.VERBOSE, verbose, 'Initial reader')
        current_dir = Path(__file__).parent
        self.__template_dir = "{0}{1}".format(
            current_dir, ReadTemplate.__TEMPLATE_DIR
        )

    def read(self, template_module):
        """
            Read a template and return a content or None
            :param template_module: File name
            :type: <str>
            :return: Template modular content | None
            :rtype: <str> | <NoneType>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        module_content, func, template_file = None, stack()[0][3], None
        module_txt = 'Argument: expected template_module <str> object'
        module_msg = "{0} {1} {2}".format('def', func, module_txt)
        if template_module is None or not template_module:
            raise ATSBadCallError(module_msg)
        if not isinstance(template_module, str):
            raise ATSTypeError(module_msg)
        file_path = "{0}/{1}".format(self.__template_dir, template_module)
        if file_path:
            with open(file_path, "r") as template_file:
                module_content = template_file.read()
                template_file.close()
        return module_content

