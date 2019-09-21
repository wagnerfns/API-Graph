from abc import ABCMeta, abstractclassmethod


class AbsStrategy(object):
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def directed(self):
        """Create graph"""
    @abstractclassmethod
    def adj_type(self):
        """Create graph"""
