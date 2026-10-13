---
title: "Create 3D Bounding Box for Cut List Item Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_3D_Bounding_Box_Example_VB.htm"
---

# Create 3D Bounding Box for Cut List Item Example (VBA)

This example shows how to create a 3D bounding box for a cut list item in a weldment part.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open: public_documents\samples\tutorial\api\weldment_box3.sldprt.
 ' 2. Right-click the Cut list folder and select Update.
 '
 ' Postconditions:
 ' 1. Expand the Cut-List-Item5 folder.
 ' 2. Select Bounding-Box_Cut-List-Item5.
 ' 3. Observe the sketch of the bounding box in the graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes when closing it.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim modDocExt As SldWorks.ModelDocExtension
 Dim boolstatus As Boolean
 Option Explicit
 Sub main()
     Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     Set modDocExt = Part.Extension

    boolstatus = modDocExt.SelectByID2("Cut-List-Item5", "SUBWELDFOLDER", 0, 0, 0, False, 0, Nothing, 0)
     modDocExt.Create3DBoundingBox
 End Sub
```
