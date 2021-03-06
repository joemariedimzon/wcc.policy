from collective.grok import gs
from zope.interface import implements
from Products.CMFQuickInstallerTool.interfaces import INonInstallable
from zope.i18nmessageid import MessageFactory

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('wcc.policy')


class HiddenProducts(object):
    """This hides the upgrade profiles from the quick installer tool."""
    implements(INonInstallable)

    def getNonInstallableProducts(self):
        return [
            'wcc.policy.upgrades'
        ]
