"""
Chapter 9: Runtime Environment - Garbage Collector

This module demonstrates a mark-and-sweep garbage collector,
one of the fundamental garbage collection algorithms.

Algorithm:
1. Mark phase: Starting from root objects, mark all reachable objects
2. Sweep phase: Delete all unmarked (unreachable) objects

Features:
- Mark-and-sweep algorithm
- Root set management
- Object reference tracking
- Automatic memory reclamation
"""


class GCObject:
    """Represents an object managed by the garbage collector"""

    def __init__(self, obj_id, data, references=None):
        """
        Initialize a GC-managed object.

        Args:
            obj_id: Unique identifier for the object
            data: Object data
            references: List of object IDs this object references
        """
        self.obj_id = obj_id
        self.data = data
        self.references = references or []

    def get_references(self):
        """Get list of object IDs this object references"""
        return self.references

    def __repr__(self):
        return f"GCObject({self.obj_id}, {self.data}, refs={self.references})"


class GarbageCollector:
    """Mark-and-sweep garbage collector"""

    def __init__(self):
        self.objects = {}  # All objects: {obj_id: GCObject}
        self.roots = set()  # Root objects (always reachable)
        self.collections = 0  # Number of GC runs
        self.objects_collected = 0  # Total objects collected

    def allocate(self, obj_id, data, references=None):
        """
        Allocate a new object.

        Args:
            obj_id: Unique identifier
            data: Object data
            references: List of referenced object IDs

        Returns:
            The allocated GCObject
        """
        obj = GCObject(obj_id, data, references)
        self.objects[obj_id] = obj
        return obj

    def add_root(self, obj_id):
        """
        Add an object to the root set.

        Root objects are always considered reachable.
        """
        if obj_id in self.objects:
            self.roots.add(obj_id)
        else:
            raise ValueError(f"Object {obj_id} does not exist")

    def remove_root(self, obj_id):
        """Remove an object from the root set"""
        self.roots.discard(obj_id)

    def collect(self):
        """
        Execute garbage collection.

        Returns:
            Number of objects collected
        """
        self.collections += 1

        # Mark phase
        marked = set()
        self.mark(self.roots, marked)

        # Sweep phase
        to_delete = []
        for obj_id in self.objects:
            if obj_id not in marked:
                to_delete.append(obj_id)

        # Delete unmarked objects
        for obj_id in to_delete:
            del self.objects[obj_id]

        collected = len(to_delete)
        self.objects_collected += collected

        return collected

    def mark(self, objects, marked):
        """
        Mark all reachable objects (recursive).

        Args:
            objects: Set of object IDs to mark
            marked: Set of already marked object IDs
        """
        for obj_id in objects:
            if obj_id not in marked:
                marked.add(obj_id)
                # Recursively mark referenced objects
                if obj_id in self.objects:
                    references = self.objects[obj_id].get_references()
                    self.mark(references, marked)

    def print_status(self):
        """Print garbage collector status"""
        print(f"Total objects: {len(self.objects)}")
        print(f"Root objects: {len(self.roots)}")
        print(f"Collections run: {self.collections}")
        print(f"Total objects collected: {self.objects_collected}")
        print("\nCurrent objects:")
        for obj_id, obj in self.objects.items():
            root_marker = " (ROOT)" if obj_id in self.roots else ""
            print(f"  {obj}{root_marker}")


# Example usage
if __name__ == "__main__":
    print("=== Garbage Collector Demo ===\n")

    gc = GarbageCollector()

    # Create object graph:
    #   A (root) -> B -> C
    #   D (root) -> E
    #   F (unreachable)

    print("Creating objects...")
    gc.allocate('A', 'Object A', references=['B'])
    gc.allocate('B', 'Object B', references=['C'])
    gc.allocate('C', 'Object C', references=[])
    gc.allocate('D', 'Object D', references=['E'])
    gc.allocate('E', 'Object E', references=[])
    gc.allocate('F', 'Object F', references=[])  # Unreachable

    # Set roots
    gc.add_root('A')
    gc.add_root('D')

    print("\nBefore garbage collection:")
    gc.print_status()

    # Run garbage collection
    print("\n" + "="*50)
    print("Running garbage collection...")
    collected = gc.collect()
    print(f"Collected {collected} objects")

    print("\nAfter garbage collection:")
    gc.print_status()

    # Remove a root and create more garbage
    print("\n" + "="*50)
    print("\nRemoving root 'D'...")
    gc.remove_root('D')

    print("Running garbage collection again...")
    collected = gc.collect()
    print(f"Collected {collected} objects (D and E should be collected)")

    print("\nFinal state:")
    gc.print_status()

    # Demonstrate circular references
    print("\n" + "="*50)
    print("\nDemonstrating circular references...")
    gc.allocate('X', 'Object X', references=['Y'])
    gc.allocate('Y', 'Object Y', references=['Z'])
    gc.allocate('Z', 'Object Z', references=['X'])  # Circular reference

    print("\nBefore collection (circular references, no roots):")
    gc.print_status()

    print("\nRunning garbage collection...")
    collected = gc.collect()
    print(
        f"Collected {collected} objects (circular references should be collected)")

    print("\nFinal state:")
    gc.print_status()
