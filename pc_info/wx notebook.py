import wx

def create_tabs(parent, nested_tuple):
    """
    Creates a wx.Notebook instance from a nested tuple.

    Parameters:
    parent (wx.Window): Parent window for the notebook.
    nested_tuple (tuple): Nested tuple containing pages and their contents.

    Returns:
    wx.Notebook: Created wx.Notebook instance.
    """
    # Create a wx.Notebook instance with the given parent.
    notebook = wx.Notebook(parent)
    
    # Iterate over each page tuple in the nested tuple.
    for args in nested_tuple:
        # Extract the page name and contents from the page tuple.
        labels, handlers = args[0], args[1]
        
        # Create a wx.Panel instance for the page and add it to the notebook.
        page = wx.Panel(notebook)
        notebook.AddPage(page, labels)
        
        # Iterate over each content tuple in the page contents.
        for content in handlers:
            # Extract the content type and value from the content tuple.
            content_type, content_value = content[0], content[1]
            
            # If the content is text, create a wx.StaticText instance and add it to the page.
            if content_type == "text":
                text = wx.StaticText(page, label=content_value)
                sizer = wx.BoxSizer(wx.VERTICAL)
                sizer.Add(text, 0, wx.ALL, 10)
                page.SetSizer(sizer)
            # If the content is a button, create a wx.Button instance and add it to the page.
            elif content_type == "button":
                button = wx.Button(page, label=content_value)
                sizer = wx.BoxSizer(wx.VERTICAL)
                sizer.Add(button, 0, wx.ALL, 10)
                page.SetSizer(sizer)
            # If the content type is unsupported, ignore it and move on.
            else:
                pass
    
    # Return the created wx.Notebook instance.
    return notebook

my_tuple = (
    ("Page 1", (("text", "This is the first page."), ("button", "Click me!"))),
    ("Page 2", (("text", "This is the second page."),))
)

app = wx.App()
frame = wx.Frame(None, title="My Notebook")
notebook = create_notebook_from_tuple(frame, my_tuple)
frame.Show()
app.MainLoop()
