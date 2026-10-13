---
title: "Set View Scale Opposite Parent View Scale Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_View_Scale_Opposite_Parent_View_Scale_Example_VB.htm"
---

# Set View Scale Opposite Parent View Scale Example (VBA)

This example shows how to set the selected drawing view's scale opposite the parent's drawing view's scale.

```
'-----------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
' 2. Select Drawing View2.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Sets Drawing View2's scale opposite
'    of the parent's drawing's view scale.
' 2. Examine the Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save
' changes.
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
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
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  View = " & swView.Name
    Debug.Print "    Original UseParentScale = " & CBool(swView.UseParentScale)
```

```
    ' Toggle
    If swView.UseParentScale Then
        swView.UseParentScale = False
    Else
        swView.UseParentScale = True
    End If
```

```
    Debug.Print "    Toggled UseParentScale = " & CBool(swView.UseParentScale)
```

```
    ' Rebuild to see new scale
    bRet = swModel.EditRebuild3: Debug.Assert bRet
```

```
End Su
```
