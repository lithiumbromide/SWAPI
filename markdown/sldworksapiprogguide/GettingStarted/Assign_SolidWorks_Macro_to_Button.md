---
title: "Assign SOLIDWORKS Macro to Button"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Assign_SolidWorks_Macro_to_Button.htm"
---

# Assign SOLIDWORKS Macro to Button

When you create a SOLIDWORKS macro, you can assign a bitmap to a macro button on a SOLIDWORKS toolbar. The SOLIDWORKS installation includes sample bitmaps, or you can create your own bitmap. If you create a bitmap for a macro button, the bitmap must meet these requirements:

- Dimension = 16 x 16 pixels
- Color = 16 colors
- Background color = white

#### To assign a macro to a button:

1. With a document open, click Tools > Customize.
2. In the dialog box, on the Commands tab:
3. In the Customize Macro Button dialog box:

1. Click Choose Image.
2. In the Icon path dialog box, select a bitmap image (*.bmp), then click Open.

  NOTE: The SOLIDWORKS installation provides bitmap images to use as custom buttons. These are located in install_dir/data/user macro icons. Select Thumbnail to see the image in the Icon path dialog box.
3. Type a Tooltip and Prompt message, which should provide a brief description of the function of the tool on the status bar. Both the ToolTip and message are displayed when the pointer is on the bitmap.

1. Select SW VBA Macros (*.swp) if adding a VBA macro (selected by default).

  - or -

  Select SW VSTA Macros (*.dll) if adding a VB.NET or C# macro.

  **NOTE:** [SOLIDWORKS 2018 offers Visual Studio Tools for Applications (VSTA)](VSTA_2015.htm), impacting how you develop and run VB.NET and C# macros in SOLIDWORKS 2018 and later.
2. Select the macro.
3. Click Open.

1. Click OK to close the Customize dialog box.

#### To edit a macro button on a toolbar or CommandManager:

1. In an open SOLIDWORKS document, click Tools > Customize.
2. If on a toolbar, right-click the macro button that you want to edit.
3. If in CommandManager, right-click the macro button that you want to edit. Select **Properties**.
4. In the Customize Macro Button dialog, edit the macro button and click OK.
5. Click OK to close the Customize dialog.

#### To delete a macro button from a toolbar or CommandManager:

1. In an open SOLIDWORKS document, click Tools > Customize.
2. If on a toolbar, drag and drop the macro button from the toolbar to the Recycle Bin.
3. If in CommandManager, right-click the macro button that you want to delete. Select **Delete**.
4. Click OK to close the Customize dialog.

For more information about assigning macros to toolbars, see SOLIDWORKS Design user-interface Help.
