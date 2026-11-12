---
title: "Get All Visible Components in Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_All_Visible_Components_in_Drawing_View_Example_VB.htm"
---

# Get All Visible Components in Drawing View Example (VBA)

This example shows how to get all of the visible components in a drawing view.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open a drawing document that contains Drawing View1
'    with one or more components.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the components and their names in Drawing View1.
' 2. Examine the Immediate window.
'-------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swView As SldWorks.View
Dim swComp As SldWorks.Component2
Dim vComps As Variant
Dim boolstatus As Boolean
Dim itr As Long
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
boolstatus = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0) w
Set swView = swSelMgr.GetSelectedObject6(1, -1)
```

```
swModel.ClearSelection2 True
```

```
'Get all visible components in the Drawing View1
vComps = swView.GetVisibleComponents
```

```
' Print the number of visible components
Debug.Print "Number of components:"
Debug.Print "  " & UBound(vComps)
' Iterate through the visible components and print each one's name
Debug.Print "Names of components:"
For itr = 0 To UBound(vComps)
    Set swComp = vComps(itr)
    Debug.Print "  " & swComp.Name2
Next itr
```

```
End Sub
```
