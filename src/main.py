from defs import *
from roles.worker import Worker

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

MAX_CREEPS = 6


def main():
    # clean memory died creeps
    for name in Memory.creeps:
        if Game.creeps[name] is None:
            del Memory.creeps[name]

    # " creeps logic "
    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]
        # if name == 'Savannah':
        #     if creep.signController(creep.room.controller, "") == ERR_NOT_IN_RANGE:
        #         creep.moveTo(creep.room.controller)
        Worker(creep).run()

    # Run each spawn
    for name in Object.keys(Game.spawns):
        spawn = Game.spawns[name]
        if not spawn.spawning:
            # Get the number of our creeps in the room
            num_harvesters = _.sum(Game.creeps, lambda c: c.memory.role == 'harvester' and c.pos.roomName == spawn.pos.roomName)
            num_builders = _.sum(Game.creeps, lambda c: c.memory.role == 'builder' and c.pos.roomName == spawn.pos.roomName)
            num_upgraders = _.sum(Game.creeps, lambda c: c.memory.role == 'upgrader' and c.pos.roomName == spawn.pos.roomName)
            # num_creeps = num_harvesters + num_upgraders
            num_creeps = _.sum(Game.creeps, lambda c: c.pos.roomName == spawn.pos.roomName)

            # console.log(f"{name}: {num_harvesters} harv., {num_builders} builders, {num_upgraders} upg., {num_creeps} in total")

            # If there are no harvesters, spawn a creep once energy is at 250 or more
            if num_harvesters == 0 and spawn.room.energyAvailable >= 250:
                spawn.createCreep([WORK, CARRY, MOVE, MOVE], None, {'role': 'harvester'})
                spawn.room.visual.text(f'🛠️ spawning ah harvester!', spawn.pos.x, spawn.pos.y - 1,
                                       {"align": 'bottom', "opacity": 0.8})

            # same for an upgrader
            elif num_upgraders < 2 and spawn.room.energyAvailable >= 250:
                spawn.createCreep([WORK, CARRY, MOVE, MOVE], None, {'role': 'upgrader'})
                spawn.room.visual.text(f'🛠️ spawning an upgrader!', spawn.pos.x, spawn.pos.y - 1,
                                       {"align": 'bottom', "opacity": 0.8})

            # otherwise wait until all spawns and extensions are full before spawning
            elif num_creeps <= MAX_CREEPS and spawn.room.energyAvailable >= spawn.room.energyCapacityAvailable:
                # If there's more energy, spawn a bigger creep
                if spawn.room.energyCapacityAvailable >= 350:
                    spawn.createCreep([WORK, CARRY, CARRY, MOVE, MOVE, MOVE], None, {'role': 'builder'})
                    spawn.room.visual.text(f'🛠️ spawning a builder!', spawn.pos.x, spawn.pos.y - 1,
                                           {"align": 'bottom', "opacity": 0.8})

                elif spawn.room.energyCapacityAvailable >= 300:
                    spawn.createCreep([WORK, CARRY, CARRY, MOVE, MOVE], None, {'role': 'builder'})
                    spawn.room.visual.text(f'🛠️ spawning a builder!', spawn.pos.x, spawn.pos.y - 1,
                                           {"align": 'bottom', "opacity": 0.8})
                else:
                    spawn.createCreep([WORK, CARRY, MOVE, MOVE], None, {'role': 'builder'})
                    spawn.room.visual.text(f'🛠️ spawning a builder!', spawn.pos.x, spawn.pos.y - 1,
                                           {"align": 'bottom', "opacity": 0.8})
        # else:
        #     spawn.room.visual.text(f'🛠️ {spawn.spawning.memory.role}', spawn.pos.x + 1, spawn.pos.y,
        #                            {"align": 'left', "opacity": 0.8})


module.exports.loop = main
