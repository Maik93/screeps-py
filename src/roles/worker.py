from defs import *
from roles.base_creep import BaseCreep

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


class Worker(BaseCreep):
    """
    Runs a creep as a generic worker; it could be harvester, upgrader or builder.
    It will collect energy from its closest source, then:
     - the harvester will put it on any structure or upgrade the controller if they're full;
     - the upgrader will directly use it to update the room controller;
     - the builder will use it in incomplete structures.
    """

    def run(self):
        # If we're full, stop filling up and remove the saved source
        if self.creep.memory.filling and self.creep.store.getFreeCapacity() == 0:
            self.creep.memory.filling = False
            del self.creep.memory.source

        # If we're empty, start filling again and remove the saved target
        elif not self.creep.memory.filling and self.creep.store.getUsedCapacity() == 0:
            self.creep.memory.filling = True
            del self.creep.memory.target

        if self.creep.memory.filling:
            self.collect_resource()
        else:
            if self.creep.memory.role == 'upgrader':
                self.update_controller()
            elif self.creep.memory.role == 'builder':
                self.work_on_structure()
            else:  # default option: role 'harvester' or none
                self.refill_deposit()
