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
    """
    Runs a creep as a generic harvester.
    It will collect energy from its closest source, then put it on any structure or upgrade the controller if they're full.
    """

    def __init__(self, creep: Creep):
        self.creep = creep

    def _go_to_source_and_collect(self):
        creep = self.creep
        # If we have a saved source, use it
        if creep.memory.source:
            source = Game.getObjectById(creep.memory.source)  # TODO: store position directly?
        else:
            # first look for dropped sources
            source = creep.pos.findClosestByPath(FIND_DROPPED_RESOURCES)
            if source is not None:
                creep.memory.recover_dropped_source = True
            else:
                # Get the closest source and store it as the chosen one
                source = creep.pos.findClosestByPath(FIND_SOURCES, {"filter": lambda s: s.energy > 0})
            creep.memory.source = source.id

        # If we're near the source, harvest it - otherwise, move to it.
        if creep.pos.isNearTo(source):  # TODO: it's better to check isNearTo or try to harvest and check ERR_NOT_IN_RANGE?
            if creep.memory.recover_dropped_source:
                creep.pickup(source)
                del creep.memory.recover_dropped_source
            result = creep.harvest(source)
            if result != OK:
                print(f"[{creep.name}] Unknown result from creep.harvest({source}): {result}")
        else:
            creep.moveTo(source)


class Harvester(BaseCreep):
    def _go_to_deposit(self):
        creep = self.creep
        # If we have a saved target, use it
        if creep.memory.target:
            target = Game.getObjectById(creep.memory.target)
        else:
            # Get the new target as the closest one
            target = creep.pos.findClosestByPath(FIND_STRUCTURES, {
                "filter": lambda s: (s.structureType == STRUCTURE_SPAWN or
                                     s.structureType == STRUCTURE_EXTENSION) and s.energy < s.energyCapacity})
            # if all structures are full, go to upgrade the controller
            if target is None:
                target = creep.pos.findClosestByPath(FIND_STRUCTURES, {
                    "filter": lambda s: s.structureType == STRUCTURE_CONTROLLER})
            creep.memory.target = target.id

        # If we are targeting a spawn or extension, we need to be directly next to it - otherwise, we can be 3 away.
        if target.energyCapacity:
            is_close = creep.pos.isNearTo(target)
        else:
            is_close = creep.pos.inRangeTo(target, 3)

        if is_close:
            # If we are targeting a spawn or extension, transfer energy. Otherwise, use upgradeController on it
            if target.energyCapacity:
                result = creep.transfer(target, RESOURCE_ENERGY)
                if result == OK or result == ERR_FULL:
                    del creep.memory.target
                else:
                    print("[{}] Unknown result from creep.transfer({}, {}): {}".format(
                        creep.name, target, RESOURCE_ENERGY, result))
            else:
                result = creep.upgradeController(target)
                if result != OK:
                    print("[{}] Unknown result from creep.upgradeController({}): {}".format(
                        creep.name, target, result))
                # Let the creeps get a little bit closer than required to the controller, to make room for other creeps.
                if not creep.pos.inRangeTo(target, 2):
                    creep.moveTo(target)
        else:
            creep.moveTo(target)

    def run(self):
        creep = self.creep
        " decide whether to go to collect sources or to deposit them "
        # If we're full, stop filling up and remove the saved source
        if creep.memory.filling and creep.store.getFreeCapacity() == 0:
            creep.memory.filling = False
            del creep.memory.source
        # If we're empty, start filling again and remove the saved target
        elif not creep.memory.filling and creep.store.getUsedCapacity() == 0:
            creep.memory.filling = True
            del creep.memory.target

        " source collection logic "
        if creep.memory.filling:
            self._go_to_source_and_collect()
        else:
            " target deposit logic "
            self._go_to_deposit()
