"""Definition of the Beer content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from awpug.content import contentMessageFactory as _

from awpug.content.interfaces import IBeer
from awpug.content.config import PROJECTNAME

BeerSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'beer_type',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Beer Type"),
            description=_(u"Select what kind of beer thiis is"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

BeerSchema['title'].storage = atapi.AnnotationStorage()
BeerSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(BeerSchema, moveDiscussion=False)


class Beer(base.ATCTContent):
    """Description of the Example Type"""
    implements(IBeer)

    meta_type = "Beer"
    schema = BeerSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    beer_type = atapi.ATFieldProperty('beer_type')


atapi.registerType(Beer, PROJECTNAME)
