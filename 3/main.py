from typing import Dict, List

def move_disk(source: str, target: str, rods: Dict[str, List[int]]) -> None:
    """Moves the disk from one rod to another"""
    if rods[source]:
        disk = rods[source].pop()
        rods[target].append(disk)
        print(f"Move the disk from {source} to {target}: {disk}")
        print(f"Intermediate state: {rods}")

def hanoi_towers(n: int, source: str, target: str, auxiliary: str, rods: Dict[str, List[int]]  ) -> None:
    """Recursive function for solving the Towers of Hanoi problem"""
    if n == 1:
        move_disk(source, target, rods)
        return

    hanoi_towers(n - 1, source, auxiliary, target, rods)
    move_disk(source, target, rods)
    hanoi_towers(n - 1, auxiliary, target, source, rods)

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of disks: "))
        if n <= 0:
            raise ValueError("The number of disks must be a positive number.")

        # Initializing the rods with disks
        rods = {
            'A': list(range(n, 0, -1)),  # The disks are arranged in descending order.
            'B': [],
            'C': []
        }
        print(f"Initial state: {rods}")
        hanoi_towers(n, 'A', 'C', 'B', rods)
        print(f"Final state: {rods}")

    except ValueError as e:
        print(f"Error occurred: {e}")

# n --> number of discs to be rewritten
# source --> start rod (A)
# target --> end rod (C)
# auxiliary --> auxiliary rod (B)
# rods: dictionary containing rods and their disks
