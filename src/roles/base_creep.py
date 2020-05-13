from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


class BaseCreep:

    def __init__(self, creep: Creep):
        self.creep = creep

    def collect_resource(self):
        # If we have a saved source, use it
        if self.creep.memory.source:
            source = Game.getObjectById(self.creep.memory.source)  # TODO: store position directly?
        else:
            # first look for dropped sources
            source = self.creep.pos.findClosestByPath(FIND_DROPPED_RESOURCES)
            if source is not None:
                self.creep.memory.recover_dropped_source = True
            else:
                # Get the closest source and store it as the chosen one
                source = self.creep.pos.findClosestByPath(FIND_SOURCES, {"filter": lambda s: s.energy > 0})
                if source is None:
                    return
            self.creep.memory.source = source.id

        # If we're near the source, harvest it - otherwise, move to it.
        if self.creep.pos.isNearTo(source):  # TODO: it's better to check isNearTo or try to harvest and check ERR_NOT_IN_RANGE?
            if self.creep.memory.recover_dropped_source:
                result = self.creep.pickup(source)
                del self.creep.memory.recover_dropped_source
                del self.creep.memory.source
            else:
                result = self.creep.harvest(source)
        else:
            result = self.creep.moveTo(source)

        if result != OK:
            del self.creep.memory.recover_dropped_source
            del self.creep.memory.source

    def refill_deposit(self):
        # If we have a saved target, use it
        if self.creep.memory.target:
            target = Game.getObjectById(self.creep.memory.target)
        else:
            # Get the new target as the closest one
            target = self.creep.pos.findClosestByPath(FIND_STRUCTURES, {
                "filter": lambda s: (s.structureType == STRUCTURE_SPAWN or
                                     s.structureType == STRUCTURE_EXTENSION) and s.energy < s.energyCapacity})
            # if all structures are full, go to upgrade the controller
            if target is None:
                target = self.creep.pos.findClosestByPath(FIND_STRUCTURES, {
                    "filter": lambda s: s.structureType == STRUCTURE_CONTROLLER})
            self.creep.memory.target = target.id

        # If we are targeting a spawn or extension, we need to be directly next to it - otherwise, we can be 3 away.
        if target.energyCapacity:
            is_close = self.creep.pos.isNearTo(target)
        else:
            is_close = self.creep.pos.inRangeTo(target, 3)

        if is_close:
            # If we are targeting a spawn or extension, transfer energy. Otherwise, use upgradeController on it
            if target.energyCapacity:
                result = self.creep.transfer(target, RESOURCE_ENERGY)
                if result == OK or result == ERR_FULL:
                    del self.creep.memory.target
                else:
                    print("[{}] Unknown result from self.creep.transfer({}, {}): {}".format(
                        self.creep.name, target, RESOURCE_ENERGY, result))
            else:
                result = self.creep.upgradeController(target)
                if result != OK:
                    print("[{}] Unknown result from self.creep.upgradeController({}): {}".format(self.creep.name, target, result))
                # Let the creeps get a little bit closer than required to the controller, to make room for other creeps
                if not self.creep.pos.inRangeTo(target, 2):
                    self.creep.moveTo(target)
        else:
            self.creep.moveTo(target)

    def update_controller(self):
        # If we have a saved target, use it
        if self.creep.memory.target:
            target = Game.getObjectById(self.creep.memory.target)
        else:
            # go to upgrade the controller
            target = self.creep.pos.findClosestByPath(FIND_STRUCTURES, {
                "filter": lambda s: s.structureType == STRUCTURE_CONTROLLER})
            self.creep.memory.target = target.id

        is_close = self.creep.pos.inRangeTo(target, 3)
        if is_close:
            result = self.creep.upgradeController(target)
            if result != OK:
                print("[{}] Unknown result from creep.upgradeController({}): {}".format(self.creep.name, target, result))
            # Let the creeps get a little bit closer than required to the controller, to make room for other creeps.
            if not self.creep.pos.inRangeTo(target, 2):
                self.creep.moveTo(target)
        else:
            self.creep.moveTo(target)

    def work_on_structure(self):
        # If we have a saved target, use it
        if self.creep.memory.target:
            target = Game.getObjectById(self.creep.memory.target)
        else:
            # go to the closest incomplete structure
            target = self.creep.pos.findClosestByPath(FIND_CONSTRUCTION_SITES)
            # otherwise check if there's some structure to repair
            if target is None:
                target = self.creep.pos.findClosestByPath(FIND_STRUCTURES, {
                    "filter": lambda s: (s.structureType == STRUCTURE_WALL) or
                                        (s.structureType == STRUCTURE_RAMPART) or
                                        (s.structureType == STRUCTURE_CONTAINER) or
                                        (s.structureType == STRUCTURE_ROAD) and s.hits < s.hitsMax})
                self.creep.memory.is_repairing = True
            else:
                del self.creep.memory.is_repairing
            if target is None:
                self.refill_deposit()
                return
            self.creep.memory.target = target.id

        is_close = self.creep.pos.inRangeTo(target, 3)
        if is_close:
            if self.creep.memory.is_repairing:
                result = self.creep.repair(target)
            else:
                result = self.creep.build(target)
            if result != OK:
                print("[{}] Unknown result from creep.upgradeController({}): {}".format(self.creep.name, target, result))
            # Let the creeps get a little bit closer than required to the controller, to make room for other creeps.
            if not self.creep.pos.inRangeTo(target, 2):
                self.creep.moveTo(target)
        else:
            self.creep.moveTo(target)
