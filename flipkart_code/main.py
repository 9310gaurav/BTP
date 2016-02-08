import gui2

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


import subprocess

def select():
    sf = var.get()
    sd= sample_size.get()
    print sf +"\n"+ sd
    root.title(sf)
    gui2.main(sf,sd)
    #subprocess.Popen("./gui2.py", shell=True)
    # optional
    #color = var.get()
    #root['bg'] = color
root = tk.Tk()
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (600, 80, 200, 150))
root.title("Choose seller description category")
var = tk.StringVar(root)
# initial value
var.set('All Categories')






 


choices = ['All Categories','Pet Supplies', 'Sports & Outdoors'

'Health & Personal Care',

'Clothing',

'Beauty',

'Patio',

'Home & Kitchen',

'Grocery & Gourmet Food',

'Grills & Outdoor Cooking',

'Tools & Home Improvement',

'Baby Products',

'Small Appliance Parts & Accessories',

'Kitchen & Dining',

'Industrial & Scientific',

'Electronics',

'Appliances',

'Cell Phones & Accessories',

'Office Products',

'Home Improvement',

'Toys & Games',

'Power & Hand Tools',

'Arts',

'Books',

'Musical Instruments',

'Automotive',

'Mobility & Daily Living Aids',

'CDs & Vinyl',

'Medical Supplies & Equipment',

'Sports & Fitness',

'Audio & Video Accessories',

'Security & Surveillance',

'Accessories']
#['red', 'green', 'blue', 'yellow','white', 'magenta']
option = tk.OptionMenu(root, var, *choices)
option.pack(side='left', padx=10, pady=10)
sample_size= tk.Entry(root)
sample_size.insert(0, "Please enter sample size")
sample_size.pack(side='left',padx=10, pady=10)
button = tk.Button(root, text="See Attribute-Value Pairs", command=select)
button.pack(side='left') # padx=100, pady=100)

root.mainloop()
#30, 100   100, 10