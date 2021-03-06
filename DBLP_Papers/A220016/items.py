from __future__ import absolute_import

import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, Identity, TakeFirst
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image


class PortiaItem(scrapy.Item):
    fields = defaultdict(
        lambda: scrapy.Field(
            input_processor=Identity(),
            output_processor=Identity()
        )
    )

    def __setitem__(self, key, value):
        self._values[key] = value

    def __repr__(self):
        data = str(self)
        if not data:
            return '%s' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, data)

    def __str__(self):
        if not self._values:
            return ''
        string = super(PortiaItem, self).__repr__()
        return string


class AuthorItem(PortiaItem):
    Author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Affiliation = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class ConferenceTableOfContentsItem(PortiaItem):
    Conference = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Paper_Title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Paper_URL = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    Paper_PDF = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    Year = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Authors = scrapy.Field(
        input_processor=MapCompose(Identity()),
        output_processor=Join(),
    )


class PaperInfoItem(PortiaItem):
    Paper_Title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Authors = scrapy.Field(
        input_processor=MapCompose(Identity()),
        output_processor=Join(),
    )

