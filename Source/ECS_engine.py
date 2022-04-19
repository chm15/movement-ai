'''
Classes for ECS engine.
Copyright 2022 Connor H. McLaughlan
cmclaughlan15@gmail.com
'''


# Holds the three managers
class ECSEngine:
    _entity_manager = EntityManager(self)
    _component_manager = ComponentManager(self)
    _system_manager = SystemManager(self)

    def __init__(self):
        pass


# Controls distribution of entity ids
class EntityManager:
    _current_ID = 0
    _entities = []
    _ecs_engine

    def __init__(self, ecs_engine):
        self.ecs_engine = ecs_engine
        return

    def new_entity() -> Entity:
        e = Entity(_current_ID)
        self._entities.append(e)
        self._current_ID += 1
        return e


# Maintain dictionary of lists, where each list contains all components of a particular type.
# Manages component ids.
class ComponentManager:
    _components = {}  # { __class__ : [Component Type] }
    _ecs_engine

    def __init__(self, ecs_engine):
        self.ecs_engine = ecs_engine
        return

    def add_component(component: Component):
        comp_list = self._components.get(component.__class__)
        if comp_list != None:
            comp_list.append(c)
        else:
            comp_list = [c]
        return


class SystemManager:
    _ecs_engine

    def __init__(self, ecs_engine):
        self.ecs_engine = ecs_engine
        return


# Maintains a dictionary of it's component ids
class Entity:
    _components = {}  # { __class__ : int }  where int is the id of a component.
    _ecs_engine

    def __init__(self, ID, ecs_engine, components = {}):
        self._entity_ID = ID
        self._ecs_engine = ecs_engine

        for c in components:
            c.set_ID(ID)
            self.add_component(c)
        return

    def add_component(component: Component):
        component.set_ID(self.
        self._components[component.__class__] = component
        # TODO: Add component to list of components in comp. man.
        return


# Base class for any components
class Component:
    _entity_ID = -1

    def __init__(self, entity_ID, component_ID):
        self.ID = component_ID
        self.entity_ID = entity_ID
        return


