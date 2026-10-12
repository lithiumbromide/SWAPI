---
title: "Get Extension Line Direction Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Extension_Line_Direction_Example_VB.htm"
---

# Get Extension Line Direction Example (VBA)

This example shows how to get the direction of the selected dimension's extension line.

```
'------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
' 2. Select a non-radial dimension.
'
' Postconditions:
' 1. Gets the extension line direction for the selected non-radial
'    dimension.
' 2. Examine the Immediate window.
'------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDim As SldWorks.Dimension
    Dim swDispDim As SldWorks.DisplayDimension
    Dim swExtLineDirn As SldWorks.MathVector
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swDispDim = swSelMgr.GetSelectedObject6(1, -1)
    Set swDim = swDispDim.GetDimension
```

```
    Set swExtLineDirn = swDim.ExtensionLineDirection
```

```
    ' IDimension::ExtensionLineDirection only returns
    ' non-0 vector for feature dimensions
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Name = " & swDim.FullName
    Debug.Print "    Extension line direction = (" & swExtLineDirn.ArrayData(0) & ", " & swExtLineDirn.ArrayData(1) & ", " & swExtLineDirn.ArrayData(2) & ")"
```

```
End Sub
```
