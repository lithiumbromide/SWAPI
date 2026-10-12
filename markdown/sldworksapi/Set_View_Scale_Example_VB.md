---
title: "Set View Scale Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_View_Scale_Example_VB.htm"
---

# Set View Scale Example (VBA)

This example shows how to set the scale of a selected drawing view.

```
'---------------------------------------------
' Preconditions:
' 1. Open public_documents\introsw\bolt-assembly.slddrw.
' 2. Select a drawing view.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Increases the selected drawing view's scale.
' 2. Examine the drawing and Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not
' save changes.
'---------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swView As SldWorks.View
    Dim vScaleRatio As Variant
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
```

```
    vScaleRatio = swView.ScaleRatio
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  View = " & swView.Name
    Debug.Print "    Use sheet scale = " & CBool(swView.UseSheetScale)
    Debug.Print "    Original scale ratio = " & vScaleRatio(0) & ":" & vScaleRatio(1)
    Debug.Print "    Original decimal scale value = " & swView.ScaleDecimal
```

```
    ' Increase scale values
    ' Changing scale sets IView::UseSheetScale to false
    vScaleRatio = swView.ScaleRatio
    swView.ScaleDecimal = swView.ScaleDecimal * 2#
    vScaleRatio = swView.ScaleRatio
    Debug.Print ""
    Debug.Print "    Use sheet scale = " & CBool(swView.UseSheetScale)
    Debug.Print "    New scale ratio = " & vScaleRatio(0) & ":" & vScaleRatio(1)
    Debug.Print "    New decimal scale value = " & swView.ScaleDecimal
```

```
    ' Rebuild to see the scaled drawing view
    bRet = swModel.EditRebuild3: Debug.Assert bRet
```

```
End Sub
```
