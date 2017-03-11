from Screens.Screen import Screen
from Screens.ParentalControlSetup import ProtectedScreen
from Screens.PluginBrowser import *

from Components.ActionMap import ActionMap, NumberActionMap
from Components.PluginComponent import plugins
from Components.PluginList import *
from Plugins.Plugin import PluginDescriptor

class XPluginBrowser(PluginBrowser):
	skin = """
	<screen name="XPluginBrowser" position="fill" title="X Plugin browser" flags="wfNoBorder">
    		<panel name="PigTemplate"/>
		<widget name="list" position="640,145" size="540,420" scrollbarMode="showOnDemand"/>
	</screen>"""

	def __init__(self, session):
		PluginBrowser.__init__(self, session)

		self["PluginDownloadActions"] = ActionMap(["ColorActions"],
		{
			"red": self.close
		})

	def isProtected(self):
		return config.ParentalControl.setuppinactive.value and (not config.ParentalControl.config_sections.main_menu.value or hasattr(self.session, 'infobar') and self.session.infobar is None) and config.ParentalControl.config_sections.xplugin_browser.value

	def updateList(self):
		self.list = []
		pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_XPLUGINMENU)[:]
		for x in config.misc.pluginbrowser.plugin_order.value.split(","):
			plugin = list(plugin for plugin in pluginlist if plugin.path[24:] == x)
			if plugin:
				self.list.append(PluginEntryComponent(plugin[0], self.listWidth))
				pluginlist.remove(plugin[0])
		self.list = self.list + [PluginEntryComponent(plugin, self.listWidth) for plugin in pluginlist]
		self["list"].l.setList(self.list)

	def run(self):
		if len(self.list):
			plugin = self["list"].l.getCurrentSelection()[0]
			plugin(session=self.session)

pname = "X-Plugin"
pdesc = "List and browse XXX plugins"

def start_from_mainmenu(menuid):
    #starting from main menu
    if menuid == "mainmenu":
        return [(pname, start_plugin, "xpluginbrowser", 90)]
    return []

def start_plugin(session,**kwargs):
    session.open(XPluginBrowser)

def Plugins(path,**kwargs):
    return [PluginDescriptor(name=pname, description=pdesc,  where = PluginDescriptor.WHERE_MENU, fnc = start_from_mainmenu)]
