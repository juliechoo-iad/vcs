class Computer:
    pass
    class Computer:
        def __init__(self, OS_version, processor_speed, memory_capacity):
            self.OS_version = OS_version
            self.processor_speed = processor_speed
            self.memory_capacity = memory_capacity

        def playGame(self, game):
            print("The computer is in play game mode now"+game)

    apple = Computer ('10.14.6', '2.5GHz' ,'16GB')
    print(apple.OS_version)
    print(apple.processor_speed)
    print(apple.memory_capacity)

    apple.playGame("pack-man")
