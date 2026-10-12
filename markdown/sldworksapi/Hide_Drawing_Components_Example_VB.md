---
title: "Hide Drawing Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_Drawing_Components_Example_VB.htm"
---

# Hide Drawing Components Example (VBA)

This example shows how to hide the drawing components in the selected drawing view.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a drawing of an assembly.
' 2. Select a drawing view.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Hides the drawing components in the selected
'    drawing view.
' 2. Examine the drawing and the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Sub ProcessDrawingComponent(swDrawComp As SldWorks.DrawingComponent, sPadStr As String)
    Dim vDrawCompChildArr As Variant
    Dim vDrawCompChild As Variant
    Dim swDrawCompChild As SldWorks.DrawingComponent
```

```
    Debug.Print sPadStr & swDrawComp.Name
```

```
    ' Does not affect root component
    swDrawComp.Visible = False
    vDrawCompChildArr = swDrawComp.GetChildren
    If Not IsEmpty(vDrawCompChildArr) Then
        For Each vDrawCompChild In vDrawCompChildArr
            Set swDrawCompChild = vDrawCompChild
            ProcessDrawingComponent swDrawCompChild, sPadStr + "  "
        Next
    End If
End Sub
```

```
Sub main()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swView As SldWorks.View
    Dim swDrawComp As SldWorks.DrawingComponent
    Dim swComp As SldWorks.Component2
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
    Set swDrawComp = swView.RootDrawingComponent
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swView.Name & "  [" & swView.Type & "]"
```

```
    ProcessDrawingComponent swDrawComp, "    "
```

```
End Sub
```
