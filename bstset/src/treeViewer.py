from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from BalancedBSTSet import *
from random import randint

class TreeViewer(Frame):

    def __insertNewNode(self):
        try:
            value = int(self.newNodeValue.get())
            self.tree.add(value)
            self.__draw()
        except (ValueError, SyntaxError):
            messagebox.showerror("New Node", "Invalid value. Use integer values.")

        self.newNodeValue.delete(0, END)
        self.newNodeValue.insert(0, "0")

    def __openTreeFile(self):
        filename = filedialog.askopenfilename()

        data = []
        with open(filename, "r") as file:
            data = file.readlines()

        try:
            parts = data[0].split()
            if len(parts) not in (1, 3):
                raise ValueError("Invalid format for the first line.")
            balanced = (True == int(parts[0]))
            if len(parts) > 1:
                top = int(parts[1])
                bottom = int(parts[2])
                newTree = BalancedBSTSet(balanced, top, bottom)
            else:
                newTree = BalancedBSTSet(balanced)
            for line in data[1:]:
                numbers = line.split()
                for number in numbers:
                    integer = int(number)
                    newTree.add(integer)

            self.tree = newTree
            self.__draw()
            self.master.title("TreeViewer - " + str(newTree))

        except:
            messagebox.showerror("Invalid File", "Invalid file format. Click " \
                    "the \"Format\" for further help on the expected file " \
                    "format.")

    def __showFormatHelp(self):
        messagebox.showinfo("Tree File Format", "The tree file should be a " \
                "simple text file, with the first line having the following " \
                "format:\n\n<balanced> [top] [bottom]\n\nwhere <balanced> is " \
                "1 or 0, indicating if the saved tree is balanced or not, " \
                "and, in the case the tree being balanced, [top] and " \
                "[bottom] are optional integers representing the numerator " \
                "and denominator of the fraction that defines the tree α " \
                "constant. All other lines are read as whitespace separated " \
                "integers considered to be node values.\n\nSome examples:\n\n" \
                "1 2 3\n4 5 6 7 8 9 1 2 3\n\nor\n\n0\n5\n4\n-3\n2 100 50\n15")

    def __rebalanceTree(self):
        if None != self.tree.root():
            self.tree.rebalance(self.tree.root())
            self.__draw()

    def __drawTree(self, root, nodeWidth, nodeHeight, canvasWidth, x, y):
        c = self.treeCanvas
        halfWidth = nodeWidth / 2
        halfHeight = nodeHeight / 2
        middle = (x + (canvasWidth / 2))
        x0Center, y0Center = (c.canvasx(middle), c.canvasy(y + nodeHeight))
        x0, y0 = (c.canvasx(middle - halfWidth), c.canvasy(y + halfHeight))
        x1, y1 = (c.canvasx(middle + halfWidth), c.canvasy(y + 3*halfHeight))

        childCanvasWidth = (canvasWidth / 2)
        childY = (y + 2*nodeHeight)

        if root.left != None:
            leftMiddle = middle - (childCanvasWidth / 2)
            x1Left = c.canvasx(leftMiddle)
            y1Left = c.canvasy(childY + nodeHeight)
            c.create_line(x0Center, y0Center, x1Left, y1Left)
            self.__drawTree(root.left, nodeWidth, nodeHeight, childCanvasWidth,
                    x, childY)

        if root.right != None:
            rightMiddle = middle + (childCanvasWidth / 2)
            x1Right = c.canvasx(rightMiddle)
            y1Right = c.canvasy(childY + nodeHeight)
            c.create_line(x0Center, y0Center, x1Right, y1Right)
            self.__drawTree(root.right, nodeWidth, nodeHeight, childCanvasWidth,
                    middle, childY)

        ovalId = c.create_oval(x0, y0, x1, y1, fill="orange", tags="Node")
        self.elements[ovalId] = root.data
        c.create_text(x0, y0, text=repr(root))

    def __draw(self):
        self.treeCanvas.delete(ALL)
        self.elements = {}

        root = self.tree.root()
        if root == None:
            return

        height = self.tree.height()
        maxWidthTotal = 2**height
        canvasWidth = self.treeCanvas.winfo_width()
        maxWidthPerNode = canvasWidth / maxWidthTotal
        nodeWidth = maxWidthPerNode / 2
        canvasHeight = self.treeCanvas.winfo_height()
        maxHeightPerNode = canvasHeight / (height + 1)
        nodeHeight = maxHeightPerNode / 2

        self.__drawTree(root, nodeWidth, nodeHeight, canvasWidth, 0, 0)

    def __deleteNode(self, event):
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        items = canvas.find_overlapping(x, y, x+1, y+1)
        try:
            for item in items:
                value = self.elements[item]
                self.tree.remove(value)
        except:
            pass
        self.__draw()

    def __resize(self, event):
        self.__draw()

    def __clearTree(self):
        self.tree = BalancedBSTSet(True)
        self.__draw()
        self.master.title("TreeViewer - " + str(self.tree))

    def __insertRandomValue(self):
        self.tree.add(randint(1, 5000))
        self.__draw()

    def __init__(self):
        Frame.__init__(self, width=800, height=600)

        headerFrame = Frame(self)
        headerFrame.pack()
        openTreeFrame = Frame(headerFrame)
        openTreeFrame.pack(side=LEFT, expand=True)
        Label(openTreeFrame, text="Load Saved Tree", font="bold").pack()
        Button(openTreeFrame, text="Open", command=self.__openTreeFile).pack(expand=True, fill=X, side=LEFT)

        deletionFrame = Frame(headerFrame)
        deletionFrame.pack(side=LEFT)
        Label(deletionFrame, text="Node Deletion", font="bold").pack()
        Label(deletionFrame, text="Click any node to delete it").pack()

        insertionFrame = Frame(headerFrame)
        insertionFrame.pack(side=LEFT)
        Label(insertionFrame, text="Node Insertion", font="bold").pack()
        self.newNodeValue = Entry(insertionFrame)
        self.newNodeValue.insert(0, "0")
        self.newNodeValue.pack(side=LEFT)
        Button(insertionFrame, text="Insert", command=self.__insertNewNode).pack(side=LEFT)

        Button(headerFrame, text="Rebalance", font="bold", command=self.__rebalanceTree).pack(expand=True, fill=BOTH, side=LEFT)
        Button(headerFrame, text="Clear", font="bold", command=self.__clearTree).pack(expand=True, fill=BOTH, side=LEFT)
        Button(headerFrame, text="Insert Random", font="bold", command=self.__insertRandomValue).pack(expand=True, fill=BOTH, side=LEFT)

        self.treeCanvas = Canvas(self, bg="white")
        self.treeCanvas.bind("<Configure>", self.__resize)
        self.treeCanvas.tag_bind("Node", "<Button-1>", self.__deleteNode)
        self.treeCanvas.pack(fill=BOTH, expand=True)

        footerFrame = Frame(self)
        footerFrame.pack(fill=X)
        Button(footerFrame, text="File Format", command=self.__showFormatHelp).pack(side=LEFT)
        Label(footerFrame, text="AD2 PIG 2019-1, by Claudio Roberto França Pereira").pack(side=LEFT)

        self.pack(fill=BOTH, expand=True)

        self.tree = BalancedBSTSet(True)
        self.master.title("TreeViewer - " + str(self.tree))

if __name__ == "__main__":
    app = TreeViewer()
    mainloop()
