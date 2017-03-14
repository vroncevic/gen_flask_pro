# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

import sys
from app.cfg_base import CfgBase
from flask_pro.gen_pro import GenPro
from os.path import dirname, realpath, isdir
from datetime import datetime

class GenFlaskPro(CfgBase):
	"""
	Define class GenFlaskPro with attribute(s) and method(s).
	Load a settings, create a CL interface and run operation.
	It defines:
		attribute:
			__CONFIG - Configuration file path
			__OPS -  Tool options (list)
		method:
			__init__ - Initial constructor
			process - Process and run tool option
	"""

	__CONFIG = "/../conf/gen_flask_pro.cfg"
	__OPS = ["-g", "--gen", "-h", "--version"]

	def __init__(self):
		current_dir = dirname(realpath(__file__))
		base_config_file = "{0}{1}".format(current_dir, GenFlaskPro.__CONFIG)
		CfgBase.__init__(self, base_config_file)
		if self.get_tool_status():
			self.add_new_option(
				GenFlaskPro.__OPS[0], GenFlaskPro.__OPS[1], dest="pro",
				help="generate flask project"
			)

	def process(self):
		if self.get_tool_status():
			tool = "[{0}]".format(self.get_name())
			ver = "version {0}".format(self.get_version())
			print("\n{0} {1} {2}".format(tool, ver, datetime.now().date()))
			if len(sys.argv) > 1:
				option = sys.argv[1]
				if option not in GenFlaskPro.__OPS:
					sys.argv = []
					sys.argv.append("-h")
			else:
				sys.argv.append("-h")
			opts, args = self.parse_args(sys.argv)
			if len(args) == 1 and opts.pro and not isdir(opts.pro):
				console_txt = "generating flask project"
				print("{0} {1} [{2}]".format(tool, console_txt, opts.pro))
				if GenPro.gen_pro(opts.pro):
					print("{0} {1}".format(tool, "done!\n"))
				else:
					console_txt = "failed to generate project!\n"
					print("{0} {1}".format(tool, console_txt))
			else:
				console_txt = "project already exist in local folder!\n"
				print("{0} {1}".format(tool, console_txt))
		else:
			console_txt = "tool is not operational!\n"
			print("[{0}] {1}".format("dist_py_module", console_txt))
