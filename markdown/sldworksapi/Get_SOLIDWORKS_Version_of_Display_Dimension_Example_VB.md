---
title: "Get Version of Display Dimension (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_SOLIDWORKS_Version_of_Display_Dimension_Example_VB.htm"
---

# Get Version of Display Dimension (VBA)

This example shows how to find out if a display dimension in a drawing was created in SOLIDWORKS 2011 or later.

```
'------------------------------------------------
' Preconditions:
' 1. Open a drawing document in which a display
'    dimension exists.
' 2. Open the Immediate window.
' 3. Select the display dimension.
'
' Postconditions: Examine the Immediate window
' to see if the selected display dimension
' was created in SOLIDWORKS 2011 or later.
'-------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swDispDim As SldWorks.DisplayDimension
Dim swSelObj As Object
Dim selCount As Long
Dim selType As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    selCount = swSelMgr.GetSelectedObjectCount2(-1)
    If selCount < 1 Then
        Debug.Print "Select a display dimension and rerun the macro."
        Exit Sub
    End If
```

```
    selType = swSelMgr.GetSelectedObjectType3(1, 0)
    Set swSelObj = swSelMgr.GetSelectedObject6(1, 0)
    Select Case selType
        Case swSelDIMENSIONS
            Set swDispDim = swSelObj
            Debug.Print "Was display dimension created in SOLIDWORKS 2011 or later? " & swDispDim.GetSupportsGenericText
    End Select
```

```
End Sub
```
