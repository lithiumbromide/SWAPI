---
title: "Select Face Using Intersecting Ray Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Face_Using_Intersecting_Ray_Example_VB.htm"
---

# Select Face Using Intersecting Ray Example (VBA)

This example shows how to select the first face that is intersected by a ray that starts at the specified point and runs parallel to the specified direction vector within the specified radius.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\box.sldrpt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects the first face intersected by a ray that starts
'    at the specified point and runs parallel to the specified
'    direction vector within the specified radius.
' 2. Examine the graphics area and Immediate window.
'-----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
   Dim swApp As SldWorks.SldWorks
   Dim swModel As SldWorks.ModelDoc2
   Dim swModelDocExt As SldWorks.ModelDocExtension
   Dim startPointX As Double
   Dim startPointY As Double
   Dim startPointZ As Double
   Dim rayVecX As Double
   Dim rayVecY As Double
   Dim rayVecZ As Double
   Dim radius As Double
   Dim status As Boolean
```

```
   Set swApp = Application.SldWorks
   Set swModel = swApp.ActiveDoc
   Set swModelDocExt = swModel.Extension
```

```
   startPointX = 0.1
   startPointY = 0#
   startPointZ = 0#
```

```
   rayVecX = -1#
   rayVecY = 0#
   rayVecZ = 0#
```

```
   radius = 1#
```

```
   status = swModelDocExt.SelectByRay(startPointX, startPointY, startPointZ, rayVecX, rayVecY, rayVecZ, radius, swSelectType_e.swSelFACES, False, 0, swSelectOption_e.swSelectOptionDefault)
   Debug.Print "Selection status: " & status
```

```
End Sub
```
