# Introduction

## Properties of trees:

* Trees have a hierarchy each level of depth can represent
  a certain entity. E.g. Kingdom -> Phylum -> Class -> Order

* The children of one node are independent of the children
  of another node.

* Each leaf exists as a unique entity, and the route starting
  from the top of the tree ending in that leaf is unique.

* Entire sections of trees can be moved en-masse from one
  area to another.

## Terms

**Node:** A node is a fundamental part of a tree. It can have a
name, which we call the “key.” A node may also have additional
information. We call this additional information the “payload.”
While the payload information is not central to many tree
algorithms, it is often critical in applications that make use
of trees.

**Edge:** An edge is another fundamental part of a tree. 
An edge connects two nodes to show that there is a relationship
between them. Every node (except the root) is connected by
exactly one incoming edge from another node. Each node may
have several outgoing edges.

**Root:** The root of the tree is the only node in the tree
that has no incoming edges. In Figure Figure 2, / is the
root of the tree.

**Path:** A path is an ordered list of nodes that are connected
by edges. For example, Mammal → Carnivora → Felidae → Felis
→ Domestica is a path.

**Children:** The set of nodes c that have incoming edges from
the same node to are said to be the children of that node. 
In Figure Figure 2, nodes log/, spool/, and yp/ are the 
children of node var/.

**Parent:** A node is the parent of all the nodes it connects
to with outgoing edges. In Figure 2 the node var/ is the parent
of nodes log/, spool/, and yp/.

**Sibling:** Nodes in the tree that are children of the same
parent are said to be siblings. The nodes etc/ and usr/ are
siblings in the filesystem tree.

**Subtree:** A subtree is a set of nodes and edges comprised of 
a parent and all the descendants of that parent.

**Leaf Node:** A leaf node is a node that has no children.
For example, Human and Chimpanzee are leaf nodes in Figure 1.

**Level:** The level of a node n is the number of edges on the 
path from the root node to n. For example, the level of the 
Felis node in Figure 1 is five. By definition, the level of 
the root node is zero.

**Height:** The height of a tree is equal to the maximum level
of any node in the tree. The height of the tree in Figure 2 is two.

**Binary Tree:** A tree in which each node has a maximum of
two children.

A tree can be thought of using a recursive definition in which,
"A tree is either empty or consists of a root and zero or more
subtrees, each of which is also a tree."
MK NOTE: So a leaf node would be an example of a tree with
a root node and zero subtrees.

# Implementation

Can be implemented using a list of lists. In this setup,
A root node with only a single child will dump that child
into the left node placeholder. 
