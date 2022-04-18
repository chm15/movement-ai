'''
Classes for ECS engine.
Copyright 2022
'''



# Holds the three managers
class ECSEngine:
    _entity_manager = EntityManager()
    _component_manager = ComponentManager()
    _system_manager = SystemManager()

    def __init__(self):
        pass


# Controls distribution of entity ids
class EntityManager:
    def __init__(self):
        pass


# Maintain dictionary of lists, where each list contains all components of a particular type.
# Manages component ids.
class ComponentManager:
    _components = {}  # { __class__ : [Component Type] }
    def __init__(self):
        pass


class SystemManager:
    def __init__(self):
        pass


# Maintains a dictionary of it's component ids
class Entity:
    _components = {}  # { __class__ : int }  where int is the id of a component.

    def __init__(self, list_of_components):
        pass


# Base class for any components
class Component:
    _ID = -1
    _entity_ID = -1

    def __init__(self, entity_ID, component_ID):
        self.ID = component_ID
        self.entity_ID = entity_ID
        return


