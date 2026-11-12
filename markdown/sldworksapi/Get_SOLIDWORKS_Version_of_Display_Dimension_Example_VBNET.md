---
title: "Get Version of Display Dimension (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_SOLIDWORKS_Version_of_Display_Dimension_Example_VBNET.htm"
---

# Get Version of Display Dimension (VB.NET)

This example shows how to find out if a display dimension in a drawing was created in SOLIDWORKS 2011 or later.

```vb
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

```vb
Imports
```

SolidWorks.Interop.sldworks

```vb
Imports
```

SolidWorks.Interop.swconst

```vb
Imports
```

System

```vb
Imports
```

System.Diagnostics

```vb
Partial
```

Class SolidWorksMacro

```vb
Public Sub Main()
```

```vb
Dim swModel As ModelDoc2
```

Dim swSelMgr As

SelectionMgr

Dim swDispDim As

DisplayDimension

Dim swSelObj As Object

```vb
Dim selCount As  Long
Dim selType As  Long
swModel = swApp.ActiveDoc
swSelMgr = swModel.SelectionManager
selCount = swSelMgr.GetSelectedObjectCount2(-1)
If selCount < 1 Then
    Debug.Print("Select a display dimension and rerun the macro.")
    Exit Sub
End If

 selType = swSelMgr.GetSelectedObjectType3(1, 0)
swSelObj = swSelMgr.GetSelectedObject6(1, 0)
Select Case selType
```

```vb
Case swSelectType_e.swSelDIMENSIONS
swDispDim = swSelObj
Debug.Print("Was display dimension created in SOLIDWORKS 2011 or later? " & swDispDim.GetSupportsGenericText)
```

```vb
End Select
End Sub
```

```vb
''' <summary>
''' The SldWorks swApp variable is pre-assigned for you.
''' </summary>
Public swApp As SldWorks
```

```vb
End
```

Class
