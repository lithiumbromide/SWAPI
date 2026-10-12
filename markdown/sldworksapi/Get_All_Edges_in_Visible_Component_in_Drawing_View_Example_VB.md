---
title: "Get All Edges in Visible Component in Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_All_Edges_in_Visible_Component_in_Drawing_View_Example_VB.htm"
---

# Get All Edges in Visible Component in Drawing View Example (VBA)

This method gets all of the edges in the first visible component in a drawing view.

```
'---------------------------------
' Preconditions:
' 1. Open a drawing of an assembly with multiple
'    components and a drawing view named Drawing View1.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets all of the visible components in the assembly in
'    Drawing View1.
' 2. Prints the name of the first visible component to the
'    Immediate window.
' 3. Iterates and selects all edges on the first visible
'    component.
' 4. Examine the Immediate window and drawing.
'----------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swSelData As SldWorks.SelectData
Dim swComp As SldWorks.Component2
Dim swView As SldWorks.View
Dim swEnt As SldWorks.Entity
Dim vComps As Variant
Dim vEdges As Variant
Dim itr As Long
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
```

```
    boolstatus = swModel.ActivateView("Drawing View1")
    boolstatus = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
```

```
    swModel.ClearSelection2 True
```

```
    'Get all visible components
    vComps = swView.GetVisibleComponents
```

```
    'Print name of first visible component
    Debug.Print vComps(0).Name2
```

```
    'Get all edges on the first visible component
    vEdges = swView.GetVisibleEntities(vComps(0), swViewEntityType_Edge)
```

```
    'Iterate and select all edges on the first visible component
    Set swSelData = swSelMgr.CreateSelectData
    swSelData.View = swView
    For itr = 0 To UBound(vEdges)
        Set swEnt = vEdges(itr)
        boolstatus = swEnt.Select4(True, swSelData)
    Next itr
```

```
End Sub
```
