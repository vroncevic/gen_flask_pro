# -*- coding: UTF-8 -*-
# gen_flask_pro.py
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
    from pathlib import Path

    from ats_utilities.cfg_base import CfgBase
    from flask_pro.gen_pro import GenPro
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
    from ats_utilities.console_io.error import error_message
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


class GenFlaskPro(CfgBase):
    """
        Define class GenFlaskPro with attribute(s) and method(s).
        Load a settings, create an interface and run operation.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __CONFIG - Configuration file path
                __OPS -  Tool options (list)
            method:
                __init__ - Initial constructor
                process - Generating Flask project
    """

    __slots__ = ('VERBOSE', '__CONFIG', '__OPS')
    VERBOSE = 'GENERATE_FLASK_PROJECT'
    __CONFIG = '/../conf/gen_flask_pro.cfg'
    __OPS = ['-g', '--gen', '-h', '--version']

    def __init__(self, verbose=False):
        """
            Initial constructor.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(GenFlaskPro.VERBOSE, verbose, 'Initial Flask project')
        module_dir = Path(__file__).parent
        base_config_file = "{0}{1}".format(module_dir, GenFlaskPro.__CONFIG)
        CfgBase.__init__(self, base_config_file, verbose=verbose)
        if self.tool_status:
            self.add_new_option(
                GenFlaskPro.__OPS[0], GenFlaskPro.__OPS[1], dest='pro',
                help='generate flask project'
            )

    def process(self, verbose=False):
        """
            Generating Flask project.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        status = False
        if self.tool_status:
            num_of_args = len(sys.argv)
            self.show_base_info(verbose=verbose)
            if num_of_args > 1:
                option = sys.argv[1]
                if option not in GenFlaskPro.__OPS:
                    sys.argv = []
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            opts, args = self.parse_args(sys.argv)
            project_path = opts.pro
            project_path_dir = Path(project_path).parent
            project_path_exist = project_path_dir.exists()
            if num_of_args == 1 and opts.pro and not project_path_exist:
                generator, gen_status = GenPro(verbose=verbose), False
                verbose_message(
                    GenFlaskPro.VERBOSE, verbose, 'Generating Flask project',
                    project_path
                )
                gen_status = generator.gen_pro(opts.pro)
                if gen_status:
                    success_message(self.name, 'Done')
                    status = True
                else:
                    error_message(self.name, 'Failed to generate project!')
            else:
                error_message(self.name, 'Project already exist!')
        else:
            error_message('gen_flask_pro', 'Tool is not operational')
        return True if status else False

