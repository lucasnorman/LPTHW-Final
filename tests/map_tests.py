from nose.tools import *
from gothonweb.map import *
from dungeonwalk.maps import *

def test_gothon_game_map():
	room = START.go('tell a joke')
	assert_equal(room, laser_weapon_armory)

	dead = Room("death", "Oh you died")
	assert_equal(dead.name, "death")
	assert_equal(dead.description, "Oh you died")

	room = START.go('shoot')
	assert_equal(dead.name, "death")
	assert_equal(dead.description, "Oh you died")

	room = START.go('dodge')
	assert_equal(dead.name, "death")

	room = laser_weapon_armory.go('725')
	assert_equal(room, the_bridge)

	room = laser_weapon_armory.go('*')
	assert_equal(dead.name, "death")

	room = the_bridge.go('throw the bomb')
	assert_equal(dead.name, "death")

	room = the_bridge.go('slowly place the bomb')
	assert_equal(room, escape_pod)

	room = escape_pod.go('2')
	assert_equal(room, the_end_winner)

	room = escape_pod.go('*')
	assert_equal(dead.name, "death")


def test_dungeon_walk_map():
	room = START2.go('torch')
	assert_equal(room, monster_room)

	dead = Room("death", "Oh you died")
	assert_equal(dead.name, "death")
	assert_equal(dead.description, "Oh you died")

	room = START2.go('*')
	assert_equal(room, start_room)

	room = monster_room.go('yes')
	assert_equal(room, generic_death)

	room = monster_room.go('no')
	assert_equal(room, puzzle_room)

	room = puzzle_room.go('north')
	assert_equal(room, generic_death)

	room = puzzle_room.go('west')
	assert_equal(room, riddle_room)

	room = riddle_room.go('3')
	assert_equal(room, treasure_room)

	room = treasure_room.go('17')
	assert_equal(room, ladder_room)
