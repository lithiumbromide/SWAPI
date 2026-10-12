---
title: "Put Assembly Components in Drawing View on Different Layers Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Put_Assembly_Components_in_Drawing_View_on_Different_Layers_Example_VB.htm"
---

# Put Assembly Components in Drawing View on Different Layers Example (VBA)

This example shows how to put all assembly components in a drawing view on different layers.

```
'------------------------------------------------------------
' Preconditions:
' 1. Open a drawing document of an assembly with multiple
'    components.
' 2. Select a drawing view.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates a new drawing layer for each assembly component.
' 2. Puts each component on its own layer.
' 3. To verify, right-click the drawing view selected in
'    Preconditions step 2 and click Change Layer > down-arrow
'    button on the Change document layer dialog.
' 4. Examine the Immediate window.
'
' NOTE: Illegal characters are replaced with legal characters
' when creating a new drawing layer.
'-------------------------------------------------------------
Option Explicit
```

```
Private Sub ChangeComponentLayer(swApp As SldWorks.SldWorks, swDraw As SldWorks.DrawingDoc, swDrawComp As SldWorks.DrawingComponent, sLayerName As String)
```

```
    Dim bRet As Boolean
```

```
    ' Form a legal layer name by replacing backslash
    '(/) and at sign (@) symbols with underscores
    sLayerName = Replace(sLayerName, "/", "_")
    sLayerName = Replace(sLayerName, "@", "_")
```

```
    bRet = swDraw.CreateLayer(sLayerName, "layer for " & sLayerName, 0, swLineCONTINUOUS, swLW_NORMAL, True): Debug.Assert bRet
    swDrawComp.Layer = sLayerName
```

```
End Sub
```

```
Sub ProcessDrawingComponent(swApp As SldWorks.SldWorks, swDraw As SldWorks.DrawingDoc, swDrawComp As SldWorks.DrawingComponent, sPadStr As String)
```

```
    Dim vDrawCompChildArr As Variant
    Dim vDrawCompChild As Variant
    Dim swDrawCompChild As SldWorks.DrawingComponent
```

```
    Debug.Print sPadStr & swDrawComp.Name
    ChangeComponentLayer swApp, swDraw, swDrawComp, swDrawComp.Name
```

```
    vDrawCompChildArr = swDrawComp.GetChildren
    If Not IsEmpty(vDrawCompChildArr) Then
        For Each vDrawCompChild In vDrawCompChildArr
            Set swDrawCompChild = vDrawCompChild
            ProcessDrawingComponent swApp, swDraw, swDrawCompChild, sPadStr + "  "
        Next
    End If
```

```
End Sub
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
    Dim swDrawComp As SldWorks.DrawingComponent
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
    Set swDrawComp = swView.RootDrawingComponent
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swView.Name & "  [" & swView.Type & "]"
```

```
    ProcessDrawingComponent swApp, swDraw, swDrawComp, "    "
```

```
End Sub
```
