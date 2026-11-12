---
title: "Determine if Display Dimension Marked for Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Determine_if_Display_Dimension_Marked_for_Drawing_Example_VB.htm"
---

# Determine if Display Dimension Marked for Drawing Example (VBA)

This example shows how to determine if a display dimension is marked to include in a drawing document.

```
'--------------------------------------
' Preconditions:
' 1. Open a part or assembly document.
' 2. Insert a smart dimension and leave the PropertyManager
'    page open so that the dimension is selected.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'--------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDispDim As SldWorks.DisplayDimension
    Dim swDim As SldWorks.Dimension
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swDispDim = swSelMgr.GetSelectedObject6(1, 0)
    Set swDim = swDispDim.GetDimension
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Name of dimension = " & swDim.FullName
    Debug.Print "    Marked for drawing? " & swDispDim.MarkedForDrawing
```

```
End Sub
```
