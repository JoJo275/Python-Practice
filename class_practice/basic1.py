# !/usr/bin/env python3
"""basic1.py

Class practice focusing on class methods.

"""


class UserTracker:
    """Tracks users created via class methods."""
    
    user_count = 0  # Class variable shared by all instances
    all_users = []  # Stores all user names
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        UserTracker.user_count += 1
        UserTracker.all_users.append(name)
    
    @classmethod
    def from_input(cls):
        """Factory method: creates instance from user input."""
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        return cls(name, age)  # Returns new instance
    
    @classmethod
    def get_stats(cls):
        """Returns class-level statistics."""
        return f"Total users: {cls.user_count}, Names: {cls.all_users}"
    
    @classmethod
    def reset_tracker(cls):
        """Resets all class-level data."""
        cls.user_count = 0
        cls.all_users = []
        print("Tracker reset!")


if __name__ == "__main__":
    # Create users via class method (from input)
    user1 = UserTracker.from_input()
    user2 = UserTracker.from_input()
    
    # Check stats via class method
    print(UserTracker.get_stats())
    
    # Reset via class method
    UserTracker.reset_tracker()
    print(UserTracker.get_stats())
