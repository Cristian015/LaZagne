# name => Name of a class
# category => windows / browsers / etc
# options => dictionary
#	 - command
#	 - action
#	 - dest
#	 - help
#	ex: ('-s', action='store_true', dest='skype', help='skype')
#		options['command'] = '-s'
#		options['action'] = 'store_true'
#		options['dest'] = 'skype'
#		options['help'] = 'skype'

class ModuleInfo():
	def __init__(self, name, category, options, suboptions=[], need_high_privileges=False, need_system_privileges=False, need_to_be_in_env=True, cannot_be_impersonate_using_tokens=False):
		self.name = name
		self.category = category
		self.options = options
		self.suboptions = suboptions
		self.need_high_privileges = need_high_privileges
		self.need_system_privileges = need_system_privileges
		self.need_to_be_in_env = need_to_be_in_env
		self.cannot_be_impersonate_using_tokens = cannot_be_impersonate_using_tokens