from abc import ABC, abstractmethod

class FilterChain:
    def __init__(self):
        self.filters = []
    
    def add_filter(self, filter):
        self.filters.append(filter)
    
    def apply_filters(self, data):
        for filter in self.filters:
            data = filter.apply(data)
        return data

class Filter(ABC):
    @abstractmethod
    def apply(self, data):
        pass