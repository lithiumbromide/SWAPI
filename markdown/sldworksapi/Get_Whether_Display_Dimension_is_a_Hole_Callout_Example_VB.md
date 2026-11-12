---
title: "Get Whether Display Dimension is a Hole Callout Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Display_Dimension_is_a_Hole_Callout_Example_VB.htm"
---

# Get Whether Display Dimension is a Hole Callout Example (VBA)

This example shows how to determine if a display dimension is a hole callout.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\costing\machined_part.sldprt.
' 2. Click File > Make Drawing from Part > OK, drag-and-drop
'    (A)Top in the drawing, and click OK in the PropertyManager page.
' 3. Click Insert > Annotations > Hole Callout, click any
'    hole in the model, drag-and-drop the hole
'    callout in an empty space in the drawing, and click OK
'    in the PropertyManager page.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Selects RD1@DrawingView1.
' 2. Gets whether RD1@DrawingView1 is a hole callout and
'    gets its text.
' 3. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDisplayDimension  As SldWorks.DisplayDimension
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
```

```
    ' Select hole callout and get its text
    boolstatus = swModelDocExt.SelectByID2("RD1@Drawing View1", "DIMENSION", 0.2385689138462, 0.1081692215385, 0, False, 0, Nothing, 0)
    Set swDisplayDimension = swSelMgr.GetSelectedObject6(1, -1)
    Debug.Print "Is a hole callout? " & swDisplayDimension.IsHoleCallout
    Debug.Print "  Callout portion above text  = " & swDisplayDimension.GetText(swDimensionTextParts_e.swDimensionTextCalloutAbove)
    Debug.Print "  Callout portion below text  = " & swDisplayDimension.GetText(swDimensionTextParts_e.swDimensionTextCalloutBelow)
    Debug.Print "  Prefix of callout = " & swDisplayDimension.GetText(swDimensionTextParts_e.swDimensionTextPrefix)
    Debug.Print "  Suffix of callout = " & swDisplayDimension.GetText(swDimensionTextParts_e.swDimensionTextSuffix)
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
