"""Definition of the Beer Folder content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from awpug.content.interfaces import IBeerFolder
from awpug.content.config import PROJECTNAME

BeerFolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

BeerFolderSchema['title'].storage = atapi.AnnotationStorage()
BeerFolderSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    BeerFolderSchema,
    folderish=True,
    moveDiscussion=False
)


class BeerFolder(folder.ATFolder):
    """Description of the Example Type"""
    implements(IBeerFolder)

    meta_type = "BeerFolder"
    schema = BeerFolderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(BeerFolder, PROJECTNAME)
