class Sim():
    def __init__(self):
        self.running = True
        self.actor_list = []


    def isRunning(self):
        return self.running

    def update(self):
        for actor in self.actor_list:
            actor.update()

    def add_actor(self):
        print(0)

#Create a simulation        
sim = Sim()

#Main loop
while sim.isRunning():
    sim.update()