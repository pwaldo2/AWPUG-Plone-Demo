from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from awpug.content import contentMessageFactory as _



class IBeer(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    beer_type = schema.TextLine(
        title=_(u"Beer Type"),
        required=False,
        description=_(u"Select what kind of beer thiis is"),
    )
#
