"""
Chapter 9: Runtime Environment - Heap Manager

This module demonstrates a simple heap memory manager with:
- Dynamic memory allocation (malloc)
- Memory deallocation (free)
- Free list management
- Memory coalescing (merging adjacent free blocks)

Features:
- First-fit allocation strategy
- Automatic coalescing of adjacent free blocks
- Simple but functional heap management
"""


class HeapManager:
    """Simple heap manager with first-fit allocation"""

    def __init__(self, heap_size):
        """
        Initialize heap manager.

        Args:
            heap_size: Total size of heap in bytes
        """
        self.heap = bytearray(heap_size)
        self.free_list = [(0, heap_size)]  # (起始地址, 大小)
        self.allocated_blocks = {}  # Track allocated blocks for debugging

    def malloc(self, size):
        """
        Allocate memory block.

        Args:
            size: Number of bytes to allocate

        Returns:
            Starting address of allocated block

        Raises:
            MemoryError: If insufficient memory available
        """
        # 首次适配算法 (First-fit)
        for i, (start, block_size) in enumerate(self.free_list):
            if block_size >= size:
                # 分配内存
                self.free_list.pop(i)

                # 如果有剩余空间，加回空闲列表
                if block_size > size:
                    self.free_list.insert(i, (start + size, block_size - size))

                # Track allocation
                self.allocated_blocks[start] = size

                return start

        # 内存不足
        raise MemoryError("Out of memory")

    def free(self, address, size):
        """
        Free memory block.

        Args:
            address: Starting address of block to free
            size: Size of block in bytes
        """
        # Remove from allocated blocks
        if address in self.allocated_blocks:
            del self.allocated_blocks[address]

        # 将释放的块加入空闲列表
        self.free_list.append((address, size))

        # 合并相邻的空闲块
        self.coalesce()

    def coalesce(self):
        """
        Merge adjacent free blocks.

        This reduces fragmentation by combining neighboring
        free blocks into larger contiguous blocks.
        """
        # Sort free list by address
        self.free_list.sort()

        i = 0
        while i < len(self.free_list) - 1:
            start1, size1 = self.free_list[i]
            start2, size2 = self.free_list[i + 1]

            # Check if blocks are adjacent
            if start1 + size1 == start2:
                # 合并
                self.free_list[i] = (start1, size1 + size2)
                self.free_list.pop(i + 1)
            else:
                i += 1

    def get_free_memory(self):
        """
        Get total free memory.

        Returns:
            Total bytes of free memory
        """
        return sum(size for _, size in self.free_list)

    def get_allocated_memory(self):
        """
        Get total allocated memory.

        Returns:
            Total bytes of allocated memory
        """
        return sum(self.allocated_blocks.values())

    def print_status(self):
        """Print current heap status"""
        print(f"Heap size: {len(self.heap)} bytes")
        print(f"Free memory: {self.get_free_memory()} bytes")
        print(f"Allocated memory: {self.get_allocated_memory()} bytes")
        print(f"Free blocks: {len(self.free_list)}")
        print(f"Allocated blocks: {len(self.allocated_blocks)}")
        print("\nFree list:")
        for start, size in self.free_list:
            print(f"  Address {start}: {size} bytes")
        print("\nAllocated blocks:")
        for start, size in self.allocated_blocks.items():
            print(f"  Address {start}: {size} bytes")


# Example usage
if __name__ == "__main__":
    print("=== Heap Manager Demo ===\n")

    # Create a heap of 1000 bytes
    heap = HeapManager(1000)

    print("Initial state:")
    heap.print_status()
    print("\n" + "="*50 + "\n")

    # Allocate some blocks
    print("Allocating 100 bytes...")
    addr1 = heap.malloc(100)
    print(f"Allocated at address: {addr1}")
    heap.print_status()
    print("\n" + "="*50 + "\n")

    print("Allocating 200 bytes...")
    addr2 = heap.malloc(200)
    print(f"Allocated at address: {addr2}")
    heap.print_status()
    print("\n" + "="*50 + "\n")

    print("Allocating 150 bytes...")
    addr3 = heap.malloc(150)
    print(f"Allocated at address: {addr3}")
    heap.print_status()
    print("\n" + "="*50 + "\n")

    # Free the middle block
    print(f"Freeing block at address {addr2} (200 bytes)...")
    heap.free(addr2, 200)
    heap.print_status()
    print("\n" + "="*50 + "\n")

    # Free the first block (should coalesce with freed middle block)
    print(f"Freeing block at address {addr1} (100 bytes)...")
    heap.free(addr1, 100)
    print("Note: Should coalesce with previously freed block")
    heap.print_status()
    print("\n" + "="*50 + "\n")

    # Allocate a large block that fits in the coalesced space
    print("Allocating 250 bytes (should fit in coalesced space)...")
    addr4 = heap.malloc(250)
    print(f"Allocated at address: {addr4}")
    heap.print_status()
    print("\n" + "="*50 + "\n")

    # Test memory exhaustion
    print("Testing memory exhaustion...")
    try:
        addr5 = heap.malloc(10000)  # Too large
    except MemoryError as e:
        print(f"Expected error: {e}")
