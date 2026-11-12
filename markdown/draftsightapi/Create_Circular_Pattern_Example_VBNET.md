---
title: "Create Circular Pattern Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Circular_Pattern_Example_VBNET.htm"
---

# Create Circular Pattern Example (VB.NET)

This example shows how to construct a circular pattern of Circles in a DraftSight drawing.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Start DraftSight and open a drawing document.
' 5. Run the macro.
'
' Postconditions:
' 1. Constructs three Circles.
' 2. Creates a circular pattern using the Circles.
' 3. Zooms the drawing to fit.
' 4. Examine the drawing.
'----------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
```

```
Module Module1
```

```
    Sub Main()
```

```
        Dim dsApp As Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsCircle1 As Circle
        Dim dsCircle2 As Circle
        Dim dsCircle3 As Circle
```

```
        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")
	dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands
```

```
        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If Not dsDoc Is Nothing Then
```

```
            'Get model space
            dsModel = dsDoc.GetModel()
```

```
            'Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager()
```

```
            'Circle parameters
            Dim center1X As Double, center2X As Double, center3X As Double
            center1X = 30.0#
            center2X = 60.0#
            center3X = 90.0#
```

```
            Dim center1Y As Double, center2Y As Double, center3Y As Double
            center1Y = 30.0#
            center2Y = 60.0#
            center3Y = 90.0#
```

```
            Dim center1Z As Double, center2Z As Double, center3Z As Double
            center1Z = 0.0#
            center2Z = 0.0#
            center3Z = 0.0#
```

```
            Dim radius1 As Double, radius2 As Double, radius3 As Double
            radius1 = 10.0#
            radius2 = 10.0#
            radius3 = 10.0#
```

```
            'Draw the Circles
            dsCircle1 = dsSketchManager.InsertCircle(center1X, center1Y, center1Z, radius1)
            dsCircle2 = dsSketchManager.InsertCircle(center2X, center2Y, center2Z, radius2)
            dsCircle3 = dsSketchManager.InsertCircle(center3X, center3Y, center3Z, radius3)
```

```
            'Circular pattern parameters
            Dim angleBetween As Double
            angleBetween = 3.14159265358979 / 2  '90 degrees in radians
```

```
            Dim fillAngle As Double
            fillAngle = 4.71238898 '270 degrees in radians
```

```
            Dim totalNumber As Integer
            totalNumber = 4
```

```
            Dim elementBasePointX As Double
            Dim elementBasePointY As Double
            Dim axisPointX As Double
            Dim axisPointY As Double
            elementBasePointX = 0.0#
            elementBasePointY = 0.0#
            axisPointX = 0.0#
            axisPointY = 0.0#
```

```
            Dim orientElementsAboutAxis As Boolean
            orientElementsAboutAxis = True
```

```
            'Prepare list of entity types
            Dim dsEntityTypes(0 To 2) As Integer
            dsEntityTypes(0) = dsObjectType_e.dsCircleType
            dsEntityTypes(1) = dsObjectType_e.dsCircleType
            dsEntityTypes(2) = dsObjectType_e.dsCircleType
```

```
            'Prepare list of entities
            Dim dsEntities As DispatchWrapper() = New DispatchWrapper(2) {}
            dsEntities(0) = New DispatchWrapper(dsCircle1)
            dsEntities(1) = New DispatchWrapper(dsCircle2)
            dsEntities(2) = New DispatchWrapper(dsCircle3)
```

```
            'Create circular pattern
            dsSketchManager.PatternCircular(dsBasePatternOn_e.dsBasePatternOn_AngleBetweenAndElementsNumber, angleBetween, fillAngle, totalNumber, elementBasePointX, elementBasePointY, axisPointX, axisPointY, orientElementsAboutAxis, dsEntityTypes, dsEntities)
```

```
            'Zoom to fit
            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)
```

```
        Else
```

```
            MsgBox("There are no open documents in DraftSight.")
```

```
        End If

    End Sub
```

```
End Module
```
