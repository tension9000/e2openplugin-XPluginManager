from distutils.core import setup

pkg = 'SystemPlugins.XPluginManager'
setup (name = 'enigma2-plugin-systemplugins-xpluginmanager',
	version = '1.0',
	description = 'XXX plugins manager',
	packages = [pkg],
	package_dir = {pkg: 'plugin'},
)
