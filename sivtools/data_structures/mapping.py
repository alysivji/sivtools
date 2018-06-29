"""Mapping like data structures"""

from collections import abc


class DotDict:
    """
    Dictionary that allows for the retrival of items via dot notation

    Can only access keys that are valid identifiers as defined by
    ``str.isidentifier``
    """

    def __init__(self, mapping):
        if isinstance(mapping, abc.MutableMapping):
            self.__dict = dict(mapping)
        else:
            raise TypeError("Requires mapping type")

        self.unallowed_attributes = []
        for name in mapping.keys():
            if name.isidentifier():
                value = self.__dict[name]

                # if the element is a dict, recurse
                if isinstance(value, abc.MutableMapping):
                    value = DotDict(value)

                setattr(self, name, value)
            else:
                self.unallowed_attributes.append(name)

    def __repr__(self):  # pragma: no cover
        return str(self.__dict)
