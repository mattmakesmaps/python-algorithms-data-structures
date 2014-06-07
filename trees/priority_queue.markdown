Priority Queues implemented with a binary heap provide O(log n)
performance. This is fast. Much faster then if you were to
implement a priority queue using list insertion O(n) and
list soring O(log n).

# Binary Heaps

Two varieties:

- Min heap - Smallest key is at the front.
- Max heap - largest key is at the front.

DataPlunger note: I should probably be using heaps/priority queue
 as feeders of sorted data into kyotocabinet rather then sorting
lists

Binary heaps can be stored in a list. Indexes of the list
can be used to find the children of a parent.

Given a parent at index `p`:

- Left Child: `2p`
- Right Child: `2p + 1`
- Parent of Parent: p/2

**Question:** To delete an element from the binary heap,
why do you need to move the last item on the list to the top
of the heap, and percolate down? Is this operation less expensive
then examining the nodes at the next level, promoting the lowest
valued to the root, and percolating all its children down?

**Answer:?** Pop() is an O(1) operation, so grabbing the last
element and percolating down may be faster then finding keys for
the 2nd and 3rd min items on the heap, cmparing, and re-balancing.