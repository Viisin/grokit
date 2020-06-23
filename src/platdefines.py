"""
File: platdefines.py
Author: Raghu Sesha Iyengar (raghu.sesha@gmail.com)
Description: Contains all the platform specific definitions.
In an ideal world, to support on a new platform or different version of tools,
changing this file should be good enough
"""
import platform

if 'Windows' in platform.platform():
	import ntpath

	def convert_to_os_path(path):
		newpath = ntpath.normpath(path)
		return newpath
	if platform.architecture()[0] == '32bit':
		tools_dict = \
		{ 'tomcat' : { 'file_name': 'apache-tomcat-9.0.0.M15.tar.gz',
					   'file_size': 10418920,
					   'extract_path': 'script_path',
					   'extract_dir' : 'apache-tomcat-9.0.0.M15',
					   'bin_file': '.bat'
					  },
		'opengrok' : { 'file_name' : 'opengrok-1.3.6.tar.gz',
					   'file_size': 53600922,
					   'extract_path': 'script_path',
					   'extract_dir' : 'opengrok-1.3.6',
					   'bin_file': 'opengrok.jar'
					  },
		'jre': { 'file_name' : 'jre-8u121-windows-i586.tar.gz',
				 'file_size': 62043176,
				 'extract_path': 'script_path',
				 'extract_dir' : 'jre1.8.0_121',
				 'bin_file': 'java.exe'
				},
		'ctags': { 'file_name' : 'exuberant-ctags.zip',
				   'file_size': 2171942,
				   'extract_path': 'script_path',
				   'extract_dir' : 'ctags58',
				   'bin_file': 'ctags.exe'
				  }
		}
	elif platform.architecture()[0] == '64bit':
		tools_dict = \
		{ 'tomcat' : { 'file_name': 'apache-tomcat-9.0.0.M15.tar.gz',
					   'file_size': 10418920,
					   'extract_path': 'script_path',
					   'extract_dir' : 'apache-tomcat-9.0.0.M15',
					   'bin_file': '.bat'
					  },
		'opengrok' : { 'file_name' : 'opengrok-1.3.6.tar.gz',
					   'file_size': 53600922,
					   'extract_path': 'script_path',
					   'extract_dir' : 'opengrok-1.3.6',
					   'bin_file': 'opengrok.jar'
					  },
		'jre': { 'file_name' : 'jre-8u121-windows-x64.tar.gz',
				 'file_size': 65704280,
				 'extract_path': 'script_path',
				 'extract_dir' : 'jre1.8.0_121',
				 'bin_file': 'java.exe'
				},
		'ctags': { 'file_name' : 'exuberant-ctags.zip',
				   'file_size': 2171942,
				   'extract_path': 'script_path',
				   'extract_dir' : 'ctags58',
				   'bin_file': 'ctags.exe'
				  }
		}

elif 'Linux' in platform.platform():
	import posixpath
	def convert_to_os_path(path):
		newpath = posixpath.normpath(path)
		return newpath

	tools_dict = \
	{ 'tomcat' : { 'file_name': 'apache-tomcat-8.0.8.tar.gz',
				   'file_size': 9098084,
				   'extract_dir' : 'apache-tomcat-8.0.8',
				   'bin_file': '.sh'
				  },
	  'opengrok' : { 'file_name' : 'opengrok-0.13-rc5.tar.gz',
					 'file_size': 16113249,
					 'extract_path': 'script_path',
					 'extract_dir' : 'opengrok-0.13-rc5',
					 'bin_file': 'opengrok.jar'
					},
	  'jre': { 'file_name' : 'jre-8u121-linux-x64.tar.gz',
			   'file_size': 73676107,
			   'extract_dir' : 'jre1.7.0_65',
			   'bin_file': 'java'
			  },
	  'ctags': { 'file_name' : 'exuberant-ctags.tar',
				 'file_size': 921600,
				 'extract_dir' : 'ctags58',
				 'bin_file': 'ctags'
				}
	}

