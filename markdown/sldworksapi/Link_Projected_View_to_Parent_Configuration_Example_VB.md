---
title: "Link Projected View to Parent Configuration Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Link_Projected_View_to_Parent_Configuration_Example_VB.htm"
---

# Link Projected View to Parent Configuration Example (VBA)

This example shows how to link a projected drawing view to the parent configuration.

```
'-------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified file exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Links the projected view to the parent configuration.
' 2. Examine the Immediate window.
'
' NOTE: Because this drawing document is used elsewhere, do not save
' changes.
'-------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawing As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim status As Boolean
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
```

```
' Open drawing document that has a projected view
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
Set swModel = swApp.OpenDoc6(fileName, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
Set swDrawing = swModel
Set swModelDocExt = swModel.Extension
```

```
' Make the projected view the active view
status = swDrawing.ActivateView("Drawing View2")
status = swModelDocExt.SelectByID2("Drawing View2", "DRAWINGVIEW", 0.4426278247583, 0.3837831481976, 0, False, 0, Nothing, 0)
 Set swView = swDrawing.ActiveDrawingView
```

```
' Determine whether the projected view is linked to the
' parent configuration
Call LinkConfiguration
```

```
' Link the projected view to the parent
' configuration
swView.LinkParentConfiguration = True
```

```
' Determine whether the projected view is linked to the
' parent configuration
Call LinkConfiguration
```

```
End Sub
```

```
Private Sub LinkConfiguration()
' Print to the Immediate window whether
' the projected view is linked to the parent
' configuration
    status = swView.LinkParentConfiguration
    If status Then
        Debug.Print "Projected view now linked to parent configuration."
        swModel.EditRebuild3
    Else
        Debug.Print "Projected view not linked to parent configuration."
    End If
End Sub
```
