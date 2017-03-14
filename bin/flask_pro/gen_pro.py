# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

import tarfile
from os import getcwd, mkdir, system
from os.path import dirname, realpath

class GenPro:
	"""
	Define class GenPro with attribute(s) and method(s).
	Generate flask project structure.
	It defines:
		attribute:
			None
		method:
			gen_pro - Generate project structure
	"""

	__PROJECT_TEMPLATE_ARCHIVE = "../../conf/template/flask_pro.tar.gz"

	@classmethod
	def gen_pro(cls, project_name):
		"""
		:arg: project_name - Project name
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		if project_name:
			current_dir = getcwd()
			local_dir = dirname(realpath(__file__))
			template_file = "{0}/{1}".format(
				local_dir, GenPro.__PROJECT_TEMPLATE_ARCHIVE
			)
			tar = tarfile.open(template_file, "r:gz")
			project_dir = "{0}/{1}/".format(current_dir, project_name)
			mkdir(project_dir)
			tar.extractall(path=project_dir)
			tar.close()
			cmd = "chmod -R 777 {0}".format(project_dir)
			system(cmd)
			return True
		return False
