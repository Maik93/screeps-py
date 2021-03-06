"""
This directory contains mock-up objects for many of Screep's JavaScript game objects.

There are not typings for everything, and some, such as those for `_` (lodash), exist but are incomplete.

I'll continue to add things to this, but if there's something in particular you need, it's very
easy to either add it yourself and submit a PR to this repository, or submit an issue asking
for the class.

A few notes:

- None of the constructors for game objects are accurate. It's not reliable to create these in game,
  but a 'fake' constructor with all attributes as arguments is created to give type checkers correct
  thoughts on what properties should exist.
- All methods and properties are typed with python-3.5+ annotations, and all properties are *also*
  typed with `:type x: y` style types, for editors such as PyCharm which do not fully use annotations
  for type hinting.
"""

# noinspection PyUnboundLocalVariable,PyUnresolvedReferences
__pragma__('skip')

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from transcrypt.modules.org.transcrypt.stubs.browser import __pragma__

from .constants import *
from .classes import *
from .transcrypt import *

# Generated manually using regexes on the sub files
__all__ = [
    # constants
    "OK",
    "ERR_NOT_OWNER",
    "ERR_NO_PATH",
    "ERR_NAME_EXISTS",
    "ERR_BUSY",
    "ERR_NOT_FOUND",
    "ERR_NOT_ENOUGH_ENERGY",
    "ERR_NOT_ENOUGH_RESOURCES",
    "ERR_INVALID_TARGET",
    "ERR_FULL",
    "ERR_NOT_IN_RANGE",
    "ERR_INVALID_ARGS",
    "ERR_TIRED",
    "ERR_NO_BODYPART",
    "ERR_NOT_ENOUGH_EXTENSIONS",
    "ERR_RCL_NOT_ENOUGH",
    "ERR_GCL_NOT_ENOUGH",

    "FIND_EXIT_TOP",
    "FIND_EXIT_RIGHT",
    "FIND_EXIT_BOTTOM",
    "FIND_EXIT_LEFT",
    "FIND_EXIT",
    "FIND_CREEPS",
    "FIND_MY_CREEPS",
    "FIND_HOSTILE_CREEPS",
    "FIND_SOURCES_ACTIVE",
    "FIND_SOURCES",
    "FIND_DROPPED_RESOURCES",
    "FIND_STRUCTURES",
    "FIND_MY_STRUCTURES",
    "FIND_HOSTILE_STRUCTURES",
    "FIND_FLAGS",
    "FIND_CONSTRUCTION_SITES",
    "FIND_MY_SPAWNS",
    "FIND_HOSTILE_SPAWNS",
    "FIND_MY_CONSTRUCTION_SITES",
    "FIND_HOSTILE_CONSTRUCTION_SITES",
    "FIND_MINERALS",
    "FIND_NUKES",
    "FIND_TOMBSTONES",

    "TOP",
    "TOP_RIGHT",
    "RIGHT",
    "BOTTOM_RIGHT",
    "BOTTOM",
    "BOTTOM_LEFT",
    "LEFT",
    "TOP_LEFT",

    "COLOR_RED",
    "COLOR_PURPLE",
    "COLOR_BLUE",
    "COLOR_CYAN",
    "COLOR_GREEN",
    "COLOR_YELLOW",
    "COLOR_ORANGE",
    "COLOR_BROWN",
    "COLOR_GREY",
    "COLOR_WHITE",

    "LOOK_CREEPS",
    "LOOK_ENERGY",
    "LOOK_RESOURCES",
    "LOOK_SOURCES",
    "LOOK_MINERALS",
    "LOOK_STRUCTURES",
    "LOOK_FLAGS",
    "LOOK_CONSTRUCTION_SITES",
    "LOOK_NUKES",
    "LOOK_TERRAIN",

    "OBSTACLE_OBJECT_TYPES",

    "MOVE",
    "WORK",
    "CARRY",
    "ATTACK",
    "RANGED_ATTACK",
    "TOUGH",
    "HEAL",
    "CLAIM",

    "BODYPART_COST",

    "WORLD_WIDTH",
    "WORLD_HEIGHT",

    "CREEP_LIFE_TIME",
    "CREEP_CLAIM_LIFE_TIME",
    "CREEP_CORPSE_RATE",

    "CARRY_CAPACITY",
    "HARVEST_POWER",
    "HARVEST_MINERAL_POWER",
    "REPAIR_POWER",
    "DISMANTLE_POWER",
    "BUILD_POWER",
    "ATTACK_POWER",
    "UPGRADE_CONTROLLER_POWER",
    "RANGED_ATTACK_POWER",
    "HEAL_POWER",
    "RANGED_HEAL_POWER",
    "REPAIR_COST",
    "DISMANTLE_COST",

    "RAMPART_DECAY_AMOUNT",
    "RAMPART_DECAY_TIME",
    "RAMPART_HITS",
    "RAMPART_HITS_MAX",

    "ENERGY_REGEN_TIME",
    "ENERGY_DECAY",

    "SPAWN_HITS",
    "SPAWN_ENERGY_START",
    "SPAWN_ENERGY_CAPACITY",
    "CREEP_SPAWN_TIME",
    "SPAWN_RENEW_RATIO",

    "SOURCE_ENERGY_CAPACITY",
    "SOURCE_ENERGY_NEUTRAL_CAPACITY",
    "SOURCE_ENERGY_KEEPER_CAPACITY",

    "WALL_HITS",
    "WALL_HITS_MAX",

    "EXTENSION_HITS",
    "EXTENSION_ENERGY_CAPACITY",

    "ROAD_HITS",
    "ROAD_WEAROUT",
    "ROAD_DECAY_AMOUNT",
    "ROAD_DECAY_TIME",

    "LINK_HITS",
    "LINK_HITS_MAX",
    "LINK_CAPACITY",
    "LINK_COOLDOWN",
    "LINK_LOSS_RATIO",

    "STORAGE_CAPACITY",
    "STORAGE_HITS",

    "STRUCTURE_SPAWN",
    "STRUCTURE_EXTENSION",
    "STRUCTURE_ROAD",
    "STRUCTURE_WALL",
    "STRUCTURE_RAMPART",
    "STRUCTURE_KEEPER_LAIR",
    "STRUCTURE_PORTAL",
    "STRUCTURE_CONTROLLER",
    "STRUCTURE_LINK",
    "STRUCTURE_STORAGE",
    "STRUCTURE_TOWER",
    "STRUCTURE_OBSERVER",
    "STRUCTURE_POWER_BANK",
    "STRUCTURE_POWER_SPAWN",
    "STRUCTURE_EXTRACTOR",
    "STRUCTURE_LAB",
    "STRUCTURE_TERMINAL",
    "STRUCTURE_CONTAINER",
    "STRUCTURE_NUKER",

    "CONSTRUCTION_COST",
    "CONSTRUCTION_COST_ROAD_SWAMP_RATIO",

    "CONTROLLER_LEVELS",
    "CONTROLLER_STRUCTURES",
    "CONTROLLER_DOWNGRADE",
    "CONTROLLER_CLAIM_DOWNGRADE",
    "CONTROLLER_RESERVE",
    "CONTROLLER_RESERVE_MAX",
    "CONTROLLER_MAX_UPGRADE_PER_TICK",
    "CONTROLLER_ATTACK_BLOCKED_UPGRADE",
    "CONTROLLER_NUKE_BLOCKED_UPGRADE",

    "SAFE_MODE_DURATION",
    "SAFE_MODE_COOLDOWN",
    "SAFE_MODE_COST",

    "TOWER_HITS",
    "TOWER_CAPACITY",
    "TOWER_ENERGY_COST",
    "TOWER_POWER_ATTACK",
    "TOWER_POWER_HEAL",
    "TOWER_POWER_REPAIR",
    "TOWER_OPTIMAL_RANGE",
    "TOWER_FALLOFF_RANGE",
    "TOWER_FALLOFF",

    "OBSERVER_HITS",
    "OBSERVER_RANGE",

    "POWER_BANK_HITS",
    "POWER_BANK_CAPACITY_MAX",
    "POWER_BANK_CAPACITY_MIN",
    "POWER_BANK_CAPACITY_CRIT",
    "POWER_BANK_DECAY",
    "POWER_BANK_HIT_BACK",
    "POWER_SPAWN_HITS",
    "POWER_SPAWN_ENERGY_CAPACITY",
    "POWER_SPAWN_POWER_CAPACITY",
    "POWER_SPAWN_ENERGY_RATIO",

    "EXTRACTOR_HITS",
    "EXTRACTOR_COOLDOWN",

    "LAB_HITS",
    "LAB_MINERAL_CAPACITY",
    "LAB_ENERGY_CAPACITY",
    "LAB_BOOST_ENERGY",
    "LAB_BOOST_MINERAL",
    "LAB_COOLDOWN",
    "LAB_REACTION_AMOUNT",

    "GCL_POW",
    "GCL_MULTIPLY",
    "GCL_NOVICE",

    "MODE_SIMULATION",
    "MODE_SURVIVAL",
    "MODE_WORLD",
    "MODE_ARENA",

    "TERRAIN_MASK_WALL",
    "TERRAIN_MASK_SWAMP",
    "TERRAIN_MASK_LAVA",

    "MAX_CONSTRUCTION_SITES",
    "MAX_CREEP_SIZE",

    "MINERAL_REGEN_TIME",
    "MINERAL_MIN_AMOUNT",
    "MINERAL_RANDOM_FACTOR",

    "MINERAL_DENSITY",
    "MINERAL_DENSITY_PROBABILITY",
    "MINERAL_DENSITY_CHANGE",

    "DENSITY_LOW",
    "DENSITY_MODERATE",
    "DENSITY_HIGH",
    "DENSITY_ULTRA",

    "TERMINAL_CAPACITY",
    "TERMINAL_HITS",
    "TERMINAL_SEND_COST",
    "TERMINAL_MIN_SEND",

    "CONTAINER_HITS",
    "CONTAINER_CAPACITY",
    "CONTAINER_DECAY",
    "CONTAINER_DECAY_TIME",
    "CONTAINER_DECAY_TIME_OWNED",

    "NUKER_HITS",
    "NUKER_COOLDOWN",
    "NUKER_ENERGY_CAPACITY",
    "NUKER_GHODIUM_CAPACITY",
    "NUKE_LAND_TIME",
    "NUKE_RANGE",
    "NUKE_DAMAGE",

    "PORTAL_DECAY",

    "ORDER_SELL",
    "ORDER_BUY",

    "MARKET_FEE",

    "FLAGS_LIMIT",

    "SUBSCRIPTION_TOKEN",

    "RESOURCE_ENERGY",
    "RESOURCE_POWER",

    "RESOURCE_HYDROGEN",
    "RESOURCE_OXYGEN",
    "RESOURCE_UTRIUM",
    "RESOURCE_LEMERGIUM",
    "RESOURCE_KEANIUM",
    "RESOURCE_ZYNTHIUM",
    "RESOURCE_CATALYST",
    "RESOURCE_GHODIUM",

    "RESOURCE_HYDROXIDE",
    "RESOURCE_ZYNTHIUM_KEANITE",
    "RESOURCE_UTRIUM_LEMERGITE",

    "RESOURCE_UTRIUM_HYDRIDE",
    "RESOURCE_UTRIUM_OXIDE",
    "RESOURCE_KEANIUM_HYDRIDE",
    "RESOURCE_KEANIUM_OXIDE",
    "RESOURCE_LEMERGIUM_HYDRIDE",
    "RESOURCE_LEMERGIUM_OXIDE",
    "RESOURCE_ZYNTHIUM_HYDRIDE",
    "RESOURCE_ZYNTHIUM_OXIDE",
    "RESOURCE_GHODIUM_HYDRIDE",
    "RESOURCE_GHODIUM_OXIDE",

    "RESOURCE_UTRIUM_ACID",
    "RESOURCE_UTRIUM_ALKALIDE",
    "RESOURCE_KEANIUM_ACID",
    "RESOURCE_KEANIUM_ALKALIDE",
    "RESOURCE_LEMERGIUM_ACID",
    "RESOURCE_LEMERGIUM_ALKALIDE",
    "RESOURCE_ZYNTHIUM_ACID",
    "RESOURCE_ZYNTHIUM_ALKALIDE",
    "RESOURCE_GHODIUM_ACID",
    "RESOURCE_GHODIUM_ALKALIDE",

    "RESOURCE_CATALYZED_UTRIUM_ACID",
    "RESOURCE_CATALYZED_UTRIUM_ALKALIDE",
    "RESOURCE_CATALYZED_KEANIUM_ACID",
    "RESOURCE_CATALYZED_KEANIUM_ALKALIDE",
    "RESOURCE_CATALYZED_LEMERGIUM_ACID",
    "RESOURCE_CATALYZED_LEMERGIUM_ALKALIDE",
    "RESOURCE_CATALYZED_ZYNTHIUM_ACID",
    "RESOURCE_CATALYZED_ZYNTHIUM_ALKALIDE",
    "RESOURCE_CATALYZED_GHODIUM_ACID",
    "RESOURCE_CATALYZED_GHODIUM_ALKALIDE",

    "REACTIONS",

    "BOOSTS",

    "PORTAL_UNSTABLE",
    "PORTAL_MIN_TIMEOUT",
    "PORTAL_MAX_TIMEOUT",
    "POWER_BANK_RESPAWN_TIME",

    "INVADERS_ENERGY_GOAL",

    "SYSTEM_USERNAME",

    "SIGN_NOVICE_AREA",
    "SIGN_RESPAWN_AREA",
    "SIGN_PLANNED_AREA",

    "EVENT_ATTACK",
    "EVENT_OBJECT_DESTROYED",
    "EVENT_ATTACK_CONTROLLER",
    "EVENT_BUILD",
    "EVENT_HARVEST",
    "EVENT_HEAL",
    "EVENT_REPAIR",
    "EVENT_RESERVE_CONTROLLER",
    "EVENT_UPGRADE_CONTROLLER",
    "EVENT_EXIT",

    "EVENT_ATTACK_TYPE_MELEE",
    "EVENT_ATTACK_TYPE_RANGED",
    "EVENT_ATTACK_TYPE_RANGED_MASS",
    "EVENT_ATTACK_TYPE_DISMANTLE",
    "EVENT_ATTACK_TYPE_HIT_BACK",
    "EVENT_ATTACK_TYPE_NUKE",

    "EVENT_HEAL_TYPE_MELEE",
    "EVENT_HEAL_TYPE_RANGED",

    "BODYPARTS_ALL",

    "RESOURCES_ALL",

    "COLORS_ALL",

    # classes
    'Creep', 'Game', 'PathFinder', '_', 'Memory', 'RawMemory', '_Memory', '_MemoryValue', 'Flag', 'Mineral', 'Resource',
    'RoomObject', 'Source', 'Infinity', 'JSON', 'Map', 'Set', 'Math', 'Object', 'RegExp', 'module', 'require', 'this',
    'typeof', 'undefined', 'Room', 'RoomPosition', '_PathPos', 'String', 'Array', 'console',
    'ConstructionSite', 'OwnedStructure', 'Structure', 'StructureContainer', 'StructureController',
    'StructureExtension', 'StructureExtractor', 'StructureKeeperLair', 'StructureLab', 'StructureLink',
    'StructureNuker', 'StructureObserver', 'StructurePortal', 'StructurePowerBank', 'StructurePowerSpawn',
    'StructureRampart', 'StructureRoad', 'StructureSpawn', 'StructureStorage', 'StructureTerminal', 'StructureTower',
    'StructureWall', 'Store',

    # misc
    "__pragma__",

    # transcrypt
    "__new__",
    "js_isNaN",
    'js_global',
    "__except0__",
    "Uint8Array",
]

__pragma__('noskip')
