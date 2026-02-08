#!/usr/bin/env python3
"""e4.py - Code Organization Examples

Demonstrates Python best practices for organizing code:
- Import ordering
- Constants and configuration
- Class and function structure
- Documentation patterns
- Main block pattern
"""

# =============================================================================
# IMPORTS (organized by: stdlib, third-party, local)
# =============================================================================
import os
import sys
from datetime import datetime
from typing import Optional, List, Dict

# Third-party imports would go here (e.g., import requests)

# Local imports would go here (e.g., from mymodule import helper)


# =============================================================================
# CONSTANTS & CONFIGURATION
# =============================================================================
VERSION = "1.0.0"
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
VALID_STATUSES = ("active", "inactive", "pending")


# =============================================================================
# HELPER FUNCTIONS (private, prefixed with underscore)
# =============================================================================
def _validate_input(value: str) -> bool:
    """Validate that input is non-empty string.
    
    Args:
        value: The string to validate.
        
    Returns:
        True if valid, False otherwise.
    """
    return isinstance(value, str) and len(value.strip()) > 0


def _format_timestamp(dt: datetime) -> str:
    """Format datetime as ISO string."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================
def greet_user(name: str, greeting: str = "Hello") -> str:
    """Generate a greeting message for a user.
    
    Args:
        name: The user's name.
        greeting: Optional greeting word (default: "Hello").
        
    Returns:
        Formatted greeting string.
        
    Raises:
        ValueError: If name is empty or invalid.
        
    Example:
        >>> greet_user("Alice")
        'Hello, Alice!'
        >>> greet_user("Bob", "Welcome")
        'Welcome, Bob!'
    """
    if not _validate_input(name):
        raise ValueError("Name must be a non-empty string")
    return f"{greeting}, {name.strip()}!"


def process_items(items: List[str], uppercase: bool = False) -> List[str]:
    """Process a list of items with optional transformation.
    
    Args:
        items: List of strings to process.
        uppercase: If True, convert items to uppercase.
        
    Returns:
        List of processed items.
    """
    result = [item.strip() for item in items if _validate_input(item)]
    if uppercase:
        result = [item.upper() for item in result]
    return result


# =============================================================================
# CLASSES
# =============================================================================
class TaskManager:
    """Manages a collection of tasks.
    
    Attributes:
        name: The name of the task manager.
        tasks: List of current tasks.
        
    Example:
        >>> manager = TaskManager("My Tasks")
        >>> manager.add_task("Write code")
        >>> manager.task_count
        1
    """
    
    # Class-level constants
    MAX_TASKS = 100
    
    def __init__(self, name: str) -> None:
        """Initialize the TaskManager.
        
        Args:
            name: Name for this task manager instance.
        """
        self.name = name
        self._tasks: List[Dict[str, str]] = []
        self._created_at = datetime.now()
    
    # Properties first
    @property
    def task_count(self) -> int:
        """Return the number of tasks."""
        return len(self._tasks)
    
    @property
    def created_at(self) -> str:
        """Return formatted creation timestamp."""
        return _format_timestamp(self._created_at)
    
    # Public methods
    def add_task(self, description: str, status: str = "pending") -> bool:
        """Add a new task.
        
        Args:
            description: Task description.
            status: Task status (default: "pending").
            
        Returns:
            True if task was added, False otherwise.
        """
        if self.task_count >= self.MAX_TASKS:
            return False
        if status not in VALID_STATUSES:
            status = "pending"
        
        self._tasks.append({
            "description": description,
            "status": status,
            "created": _format_timestamp(datetime.now())
        })
        return True
    
    def get_tasks(self, status: Optional[str] = None) -> List[Dict[str, str]]:
        """Get tasks, optionally filtered by status.
        
        Args:
            status: Optional status to filter by.
            
        Returns:
            List of matching tasks.
        """
        if status is None:
            return self._tasks.copy()
        return [t for t in self._tasks if t["status"] == status]
    
    def __repr__(self) -> str:
        """Return string representation."""
        return f"TaskManager(name={self.name!r}, tasks={self.task_count})"
    
    # Private methods at the end
    def _validate_task(self, task: Dict[str, str]) -> bool:
        """Validate task structure (internal use)."""
        return "description" in task and "status" in task


# =============================================================================
# MAIN BLOCK
# =============================================================================
def main() -> None:
    """Main entry point demonstrating usage."""
    print(f"Code Organization Examples v{VERSION}")
    print("=" * 40)
    
    # Demo greet_user
    print("\n1. Greeting Function:")
    print(f"   {greet_user('Alice')}")
    print(f"   {greet_user('Bob', 'Welcome')}")
    
    # Demo process_items
    print("\n2. Process Items:")
    items = ["apple", "  banana  ", "cherry", ""]
    print(f"   Original: {items}")
    print(f"   Processed: {process_items(items)}")
    print(f"   Uppercase: {process_items(items, uppercase=True)}")
    
    # Demo TaskManager
    print("\n3. TaskManager Class:")
    manager = TaskManager("Work Tasks")
    manager.add_task("Write documentation")
    manager.add_task("Review code", "active")
    manager.add_task("Deploy to production")
    
    print(f"   {manager}")
    print(f"   Created: {manager.created_at}")
    print(f"   All tasks: {manager.get_tasks()}")
    print(f"   Active: {manager.get_tasks('active')}")


if __name__ == "__main__":
    main()
