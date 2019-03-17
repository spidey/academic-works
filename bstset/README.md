# BSTSet - Binary Search Tree based Set data structure
**BSTSet** is an ordered Set implementation for Python using a Binary Search
Tree as underlying data structure. **BalancedBSTSet** is an α-balanced BSTSet,
that does automatic balancing of the tree after an insertion or deletion that
causes any subtree to have one side bigger than (α * size-of-subtree).

## Files
The documentation is present on the doc/ folder. Project specification and tasks
are described over there. As you'll see described on *AD1.pdf*, only the
**BalancedBSTSet** script was completely implemented for this project.

Source code lives in src/ subfolder.

## Usage
Both **BSTSet** and **BalancedBSTSet** can be imported directly into client
code. There is also a graphic viewer/editor for BSTs called **treeGL** which
supports both implemented types. It can be run with parameters, or directly.
When run directly, it will ask interactively for the possible options. After
initialized, it will open a new window which will show the graphical
representation of the BST, complete with adding and removing interactions
possible with the mouse and keyboard.

    $ python treeGL.py

## Testing
Both **BSTSet** and **BalancedBSTSet** have tests that can be run by calling
them directly. **BSTSet** have unit and interactive tests. **BalancedBSTSet**
only has automatic unit tests.

    $ python BSTSet.py
    $ python BalancedBSTSet.py
