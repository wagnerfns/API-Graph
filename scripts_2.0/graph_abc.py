from abc import ABCMeta, abstractclassmethod


class AbsStrategy(object):
    '''
    This class is interfacing to the graph. This class is using the strategy
    pattern to implement all the graph type.
    '''
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def directed(self):
        """Return if is directed or not"""
    @abstractclassmethod
    def graph_type(self):
        """Return if is array or list"""
