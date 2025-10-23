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


def shortest_path(grid: list[list[int]]) -> int:
    """
    Find the shortest path from top-left to bottom-right in a grid using BFS.

    Args:
        grid: 2D list where 0 represents open cell and 1 represents wall

    Returns:
        Length of shortest path, or -1 if no path exists
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
    queue = deque([(0, 0, 0)])  # (row, col, distance)
    visited: set[tuple[int, int]] = set()
    visited.add((0, 0))

    # 4-directional movements: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        row, col, distance = queue.popleft()

        # Check if we reached the destination
        if row == rows - 1 and col == cols - 1:
            return distance

        # Explore all 4 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check bounds and if cell is valid (not wall and not visited)
            if (0 <= new_row < rows and
                    0 <= new_col < cols and
                    grid[new_row][new_col] == 0 and
                    (new_row, new_col) not in visited):

                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))

    # No path found
    return -1


def main() -> None:
    """Test the shortest_path function with various examples."""
    # Test case 1: Simple 3x3 grid with clear path
    grid1 = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(f"Grid 1 shortest path: {shortest_path(grid1)}")  # Expected: 4

    # Test case 2: No path (blocked)
    grid2 = [
        [0, 1],
        [1, 0]
    ]
    print(f"Grid 2 shortest path: {shortest_path(grid2)}")  # Expected: -1

    # Test case 3: Direct path
    grid3 = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    print(f"Grid 3 shortest path: {shortest_path(grid3)}")  # Expected: 4

    # Test case 4: Single cell
    grid4 = [[0]]
    print(f"Grid 4 shortest path: {shortest_path(grid4)}")  # Expected: 0

    # Test case 5: Start position blocked
    grid5 = [
        [1, 0],
        [0, 0]
    ]
    print(f"Grid 5 shortest path: {shortest_path(grid5)}")  # Expected: -1


if __name__ == "__main__":
    main()
