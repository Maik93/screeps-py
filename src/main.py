from defs import *
from roles.harvester import Harvester

# required for Transcrypt
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

MAX_CREEPS = 15


def main():
    # clean memory died creeps
    for name in Memory.creeps:
        if Game.creeps[name] is None:
            del Memory.creeps[name]

    # " creeps logic "
    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]
        if creep.memory.role == 'upgrader':
            pass
        elif creep.memory.role == 'harvester':
            Harvester(creep).run()
        else:
            Harvester(creep).run()

    # Run each spawn
    for name in Object.keys(Game.spawns):
        spawn = Game.spawns[name]
        if not spawn.spawning:
            # Get the number of our creeps in the room
            num_creeps = _.sum(Game.creeps, lambda c: c.pos.roomName == spawn.pos.roomName)
            # If there are no creeps, spawn a creep once energy is at 250 or more
            if num_creeps < 0 and spawn.room.energyAvailable >= 250:
                spawn.createCreep([WORK, CARRY, MOVE, MOVE])
            # If there are less than 15 creeps but at least one, wait until all spawns and extensions are full before spawning
            elif num_creeps < MAX_CREEPS and spawn.room.energyAvailable >= spawn.room.energyCapacityAvailable:
                # If there's more energy, spawn a bigger creep
                if spawn.room.energyCapacityAvailable >= 350:
                    spawn.createCreep([WORK, CARRY, CARRY, MOVE, MOVE, MOVE])
                else:
                    spawn.createCreep([WORK, CARRY, MOVE, MOVE])


module.exports.loop = main
