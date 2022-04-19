



def main():
    ecs = ECSEngine()
    
    # Add systems (order matters)
    ecs.add_system(PlayerControllerSystem())
    ecs.add_system(PhysicsSystem())
    ecs.add_system(GraphicsSystem())


    # Create entities
    player = ecs.new_entity()
    
    player.add_component(PositionComponent())  # Make prefab class
    player.add_component(MeshComponent())
    player.add_component(PlayerControllerComponent())

