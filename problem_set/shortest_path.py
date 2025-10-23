"""
6) shortest_path(grid)
- Description: Given a 2D grid (list of lists) with 0 for open cell and 1 for
wall, return the length of shortest path from top-left (0,0) to bottom-right
(m-1,n-1) moving 4-directionally. If no path, return -1. Grid is non-empty.
- Input: list[list[int]]
- Output: integer
"""

# !/usr/bin/env python3

from collections import deque
from typing import List, Tuple, Optional, Set


def shortest_path(grid: List[List[int]]) -> int:
    """
    Find the shortest path from top-left to bottom-right in a grid using BFS.

    Args:
        grid: 2D list where 0 represents open cell and 1 represents wall

    Returns:
        Length of shortest path, or -1 if no path exists
    
    Time Complexity: O(m * n) where m, n are grid dimensions
    Space Complexity: O(m * n) for the visited set
    """
    if not grid or not grid[0]:
        return -1

    rows, cols = len(grid), len(grid[0])

    # Check if start or end positions are blocked
    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return -1

    # Special case: if grid is 1x1 and start position is open
    if rows == 1 and cols == 1:
        return 0

    # BFS setup
    queue: deque[Tuple[int, int, int]] = deque([(0, 0, 0)])  # (row, col, distance)
    visited: Set[Tuple[int, int]] = {(0, 0)}
    
    # 4-directional movements: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        row, col, distance = queue.popleft()

        # Explore all 4 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check if we reached the destination
            if new_row == rows - 1 and new_col == cols - 1:
                return distance + 1

            # Check bounds and if cell is valid (not wall and not visited)
            if (0 <= new_row < rows and
                0 <= new_col < cols and
                grid[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))

    # No path found
    return -1


def shortest_path_with_route(grid: List[List[int]]) -> Tuple[int, Optional[List[Tuple[int, int]]]]:
    """
    Find the shortest path and return both the length and the actual path.
    
    Args:
        grid: 2D list where 0 represents open cell and 1 represents wall
    
    Returns:
        Tuple of (path length, list of coordinates) or (-1, None) if no path
    """
    if not grid or not grid[0]:
        return -1, None
    
    rows, cols = len(grid), len(grid[0])
    
    # Check if start or end positions are blocked
    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return -1, None
    
    # Special case: if grid is 1x1
    if rows == 1 and cols == 1:
        return 0, [(0, 0)]
    
    # BFS with parent tracking for path reconstruction
    queue: deque[Tuple[int, int]] = deque([(0, 0)])
    visited: Set[Tuple[int, int]] = {(0, 0)}
    parent: dict[Tuple[int, int], Optional[Tuple[int, int]]] = {(0, 0): None}
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        row, col = queue.popleft()
        
        # Check if we reached the destination
        if row == rows - 1 and col == cols - 1:
            # Reconstruct path
            path = []
            current = (row, col)
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return len(path) - 1, path
        
        # Explore all 4 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and
                0 <= new_col < cols and
                grid[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                parent[(new_row, new_col)] = (row, col)
                queue.append((new_row, new_col))
    
    return -1, None


def visualize_path(grid: List[List[int]], path: Optional[List[Tuple[int, int]]] = None) -> str:
    """
    Create a visual representation of the grid and optional path.
    
    Args:
        grid: The grid to visualize
        path: Optional list of coordinates representing the path
    
    Returns:
        String representation of the grid with path marked
    """
    if not grid or not grid[0]:
        return "Empty grid"
    
    rows, cols = len(grid), len(grid[0])
    visual = [['■' if grid[r][c] == 1 else '□' for c in range(cols)] for r in range(rows)]
    
    if path:
        for i, (r, c) in enumerate(path):
            if i == 0:
                visual[r][c] = 'S'  # Start
            elif i == len(path) - 1:
                visual[r][c] = 'E'  # End
            else:
                visual[r][c] = '●'  # Path
    
    return '\n'.join(' '.join(row) for row in visual)


def main() -> None:
    """Test the shortest_path function with various examples."""
    test_cases = [
        # Test case 1: Simple 3x3 grid with clear path
        {
            "grid": [
                [0, 1, 0],
                [0, 1, 0],
                [0, 0, 0]
            ],
            "expected": 4,
            "description": "3x3 grid with obstacle"
        },
        # Test case 2: No path (blocked)
        {
            "grid": [
                [0, 1],
                [1, 0]
            ],
            "expected": -1,
            "description": "No path available"
        },
        # Test case 3: Direct path
        {
            "grid": [
                [0, 0, 0],
                [1, 1, 0],
                [0, 0, 0]
            ],
            "expected": 4,
            "description": "Path around obstacle"
        },
        # Test case 4: Single cell
        {
            "grid": [[0]],
            "expected": 0,
            "description": "Single cell grid"
        },
        # Test case 5: Start position blocked
        {
            "grid": [
                [1, 0],
                [0, 0]
            ],
            "expected": -1,
            "description": "Start blocked"
        },
        # Test case 6: Straight line
        {
            "grid": [
                [0, 0, 0, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0]
            ],
            "expected": 6,
            "description": "Longer path"
        },
        # Test case 7: Maze-like
        {
            "grid": [
                [0, 0, 1, 0, 0],
                [1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]
            ],
            "expected": 8,
            "description": "Complex maze"
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        grid = test["grid"]
        expected = test["expected"]
        description = test["description"]
        
        result = shortest_path(grid)
        path_length, path = shortest_path_with_route(grid)
        
        print(f"\nTest Case {i}: {description}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Result: {'✓ PASS' if result == expected else '✗ FAIL'}")
        
        if path:
            print(f"Path length: {path_length}")
            print("Grid visualization:")
            print(visualize_path(grid, path))
        else:
            print("No path found")
            print("Grid visualization:")
            print(visualize_path(grid))


if __name__ == "__main__":
    main()
