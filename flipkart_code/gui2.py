import Tkinter as tk
import random_sample



def main(arg1, arg2):
    global g1 
    g1= arg1
    global g2
    g2=arg2
    app = ExampleApp()
    app.mainloop()

class ExampleApp(tk.Tk):
    def __init__(self):
        
        tk.Tk.__init__(self)
        t = SimpleTable(self, 11,7)
        t.pack(side="top", fill="x")

class CustomText(tk.Text):
    '''A text widget with a new method, highlight_pattern()

    example:

    text = CustomText()
    text.tag_configure("red", foreground="#ff0000")
    text.highlight_pattern("this should be red", "red")

    The highlight_pattern method is a simplified python
    version of the tcl code at http://wiki.tcl.tk/3246
    '''
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression.
        '''

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.StringVar()
        index = self.search(pattern, "matchEnd","searchLimit",
                            count=count, regexp=regexp)

        self.mark_set("matchStart", index)
        self.mark_set("matchEnd", "%s+%sc" % (index, len(pattern)))
        self.tag_add(tag, "matchStart", "matchEnd")


class SimpleTable(tk.Frame):

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def __init__(self, parent, rows=10, columns=7):
        # use black background so it "peeks through" to 
        # form grid lines
        root = tk.Tk()
        tk.Frame.__init__(self, parent, background="black")

        self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.hsb = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)



        self.frame._widgets = []
        data = random_sample.output_rows(g1,g2)
        for row in range(rows):
            current_row = []
            for column in range(columns):
                x = 20
                if column == 5:
                    x = 100
                if column == 6:
                    x = 60
                label = CustomText(self.frame,height = 5,width = x) 
                if column == 6 and row>0:

                    matches = data[row][column][1]
                    for key in matches.keys():
                        label.insert(tk.INSERT,"%s : %s\n" % (matches[key],key))    

                else:
                    label.insert(tk.INSERT,"%s" % str(data[row][column]))
                if column == 5 and row > 0:
                    tags = data[row][column+1][0]
                    for tag in tags.keys():
                        if tags[tag] == "attribute_name":
                            label.tag_configure("red", foreground="red")
                            label.highlight_pattern(tag, "red")
                        else:
                            label.tag_configure("green", foreground="green")
                            label.highlight_pattern(tag, "green")         


                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self.frame._widgets.append(current_row)

        for column in range(columns):
            self.frame.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)



if __name__ == "__main__":
    sys.exit(main(arg1, arg2 ))
    