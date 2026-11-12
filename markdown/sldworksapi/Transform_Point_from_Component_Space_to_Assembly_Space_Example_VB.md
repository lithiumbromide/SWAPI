---
title: "Transform Point from Component Space to Assembly Space Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Transform_Point_from_Component_Space_to_Assembly_Space_Example_VB.htm"
---

# Transform Point from Component Space to Assembly Space Example (VBA)

This example shows how to transform a point from component space to assembly space.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Selects a component.
' 3. Transforms the component's origin to a point in
'    assembly space.
' 4. Examine the Immediate window.
'--------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swMathUtil As SldWorks.MathUtility
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swComp As SldWorks.Component2
    Dim swXform As SldWorks.MathTransform
    Dim nPt(2) As Double
    Dim vPt As Variant
    Dim swPt As SldWorks.MathPoint
    Dim bRet As Boolean
    Dim errors As Long
    Dim warnings As Long
    Dim fileName As String
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open assembly
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\smartcomponents\stepped_shaft.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    bRet = swModelDocExt.SelectByID2("stepped_shaft-1@stepped_shaft", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
```

```
    Set swMathUtil = swApp.GetMathUtility
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent(1)
    Set swXform = swComp.Transform2
```

```
    ' Point at component origin
    nPt(0) = 0#
    nPt(1) = 0#
    nPt(2) = 0#
    vPt = nPt
    Set swPt = swMathUtil.CreatePoint(vPt)
    Set swPt = swPt.MultiplyTransform(swXform)
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Component = " & swComp.Name2 & " [" & swComp.GetPathName & "]"
    Debug.Print "    Point in component = (" & nPt(0) * 1000# & ", " & nPt(1) * 1000# & ", " & nPt(2) * 1000# & ") mm"
    Debug.Print "    Point in assembly = (" & swPt.ArrayData(0) * 1000# & ", " & swPt.ArrayData(1) * 1000# & ", " & swPt.ArrayData(2) * 1000# & ") mm"
```

```
End Sub
```
