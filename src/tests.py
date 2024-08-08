import unittest
from unittest.mock import MagicMock
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        window = MagicMock()
        maze = Maze(window, 0, 0, 2, 3, 10, 10)
        self.assertEqual(2, len(maze._cells))
        self.assertEqual(3, len(maze._cells[0]))
        self.assertEqual(3, len(maze._cells[1]))
    

    def test_maze_single_row(self):
        window = MagicMock()
        maze = Maze(window, 0, 0, 1, 3, 10, 10)
        self.assertEqual(1, len(maze._cells))
        self.assertEqual(3, len(maze._cells[0]))
        
    def test_maze_single_collumn(self):
        window = MagicMock()
        maze = Maze(window, 0, 0, 3, 1, 10, 10)
        self.assertEqual(3, len(maze._cells))
        self.assertEqual(1, len(maze._cells[0]))
        self.assertEqual(1, len(maze._cells[1]))
        self.assertEqual(1, len(maze._cells[2]))
        
    def test_super_large_maze(self):
        window = MagicMock()
        maze = Maze(window, 0, 0, 100, 100, 10, 10)
        self.assertEqual(100, len(maze._cells))
        self.assertEqual(100, len(maze._cells[0]))
        self.assertEqual(100, len(maze._cells[99]))

    def test_start_wall_breaking(self):
        window = MagicMock()
        maze = Maze(window, 0, 0, 2, 3, 10, 10)
        maze._break_entrance_and_exit()
        self.assertFalse(maze._cells[0][0].has_left_wall)
        self.assertFalse(maze._cells[-1][-1].has_bottom_wall)

if __name__ == '__main__':
    unittest.main()