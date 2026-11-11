---
title: "Revolving Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Revolving_Entities_Example_VBA.htm"
---

# Revolving Entities Example (VBA)

This example shows how to revolve 3D entities.

'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
' embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
' `install_dir`**\bin\dsAutomation.dll**.
' 4. Start DraftSight.
' 5 Open the Immediate window.
' 6. Run the macro.
'
' Postconditions:
' 1. Inserts a 2D polyline, a circle, and an axis.
' 2. Revolves the 2D polyline and circle about the axis into a 3D solid.
' 3. Changes the color of the revolved entities.
' 4. Inserts a 2D polyline and a circle.
' 5. Revolves the 2D polyline and circle about the X axis into a 3D solid.
' 6. Inserts a 2D polyline and a circle.
' 7. Revolves the 2D polyline and circle about the specified axis
' and angle of revolution to a solid.
' 8. Inspect the graphics area.
'
' Optional: Open a new document, comment out the solid revolve methods,
' uncomment the surface revolve methods, and rerun the macro.
'----------------------------------------------------------------

```vb
 Option Explicit
 Sub Main()

         Dim Application As DraftSight.Application
         Set Application = GetObject(, "DraftSight.Application")

         If Application Is Nothing Then
                 Return
             End If

             Application.AbortRunningCommand
             Dim dsDoc As DraftSight.Document
             Set dsDoc = Application.GetActiveDocument()

             If dsDoc Is Nothing Then
                 Return
             End If

             Dim dsModel As DraftSight.Model
             Set dsModel = dsDoc.GetModel()

             If dsModel Is Nothing Then
                 Return
             End If

             Dim dsSketchManager As DraftSight.SketchManager
             Set dsSketchManager = dsModel.GetSketchManager()

             If dsSketchManager Is Nothing Then
                 Return
             End If

             Dim dsPolyline As DraftSight.PolyLine
             Dim coordinates(7) As Double
             coordinates(0) = -231.229
             coordinates(1) = 148
             coordinates(2) = -231.229
             coordinates(3) = 76.963
             coordinates(4) = -157.191
             coordinates(5) = 76.963
             coordinates(6) = -157.191
             coordinates(7) = 148

             If True Then
                 Set dsPolyline = dsSketchManager.InsertPolyline2D(coordinates, True)
                 dsPolyline.Elevation = 100
             End If

             Dim dsCircle As DraftSight.Circle

             If True Then
                 Set dsCircle = dsSketchManager.InsertCircle(-199.212, 233.044, 0#, 48.357)
             End If

             Dim dsLine As DraftSight.Line

             If True Then
                 Set dsLine = dsSketchManager.InsertLine(-111.167, 282.069, 0, -111.167, 83.966, 0)
             End If

             Dim dsEntities(1) As Object
             Set dsEntities(0) = dsPolyline
             Set dsEntities(1) = dsCircle
             Dim revolveArray(0) As DraftSight.Line
             Set revolveArray(0) = dsLine

             Dim revolves As Variant
             revolves = dsSketchManager.RevolveEntitiesToSolidByObject(dsEntities, revolveArray, 360#)
             Dim dsRevolve As Revolve
             Dim dsRevolveObj As Variant

             For Each dsRevolveObj In revolves
                 Set dsRevolve = dsRevolveObj
                 Dim dsColor As Color
                 Set dsColor = Application.GetColorByIndex(3)
                 dsRevolve.Color = dsColor
             Next

             'Revolve entities to surface by object
             'Dim surfRevolves As Variant
             'surfRevolves = dsSketchManager.RevolveEntitiesToSurfaceByObject(dsEntities, revolveArray, 360.0)

             Dim dsPolyline1 As DraftSight.PolyLine
             coordinates(0) = 107.848
             coordinates(1) = 158.077
             coordinates(2) = 107.848
             coordinates(3) = 74.014
             coordinates(4) = 212.128
             coordinates(5) = 74.014
             coordinates(6) = 212.128
             coordinates(7) = 158.077

             If True Then
                 Set dsPolyline1 = dsSketchManager.InsertPolyline2D(coordinates, True)
                 dsPolyline.Elevation = 100
             End If

             Dim dsCircle1 As DraftSight.Circle

             If True Then
                 Set dsCircle1 = dsSketchManager.InsertCircle(153.603, 252.781, 0#, 52.831)
             End If

             Dim dsEntities2(1) As Object
             Set dsEntities2(0) = dsPolyline1
             Set dsEntities2(1) = dsCircle1

             revolves = dsSketchManager.RevolveEntitiesToSolidByXAxis(dsEntities2, 360#, True)

             'Revolve entities to surface by X axis
             'surfRevolves = dsSketchManager.RevolveEntitiesToSurfaceByXAxis(dsEntities2, 360.0, True)

             Dim dsPolyline2 As DraftSight.PolyLine
             coordinates(0) = 435.587
             coordinates(1) = 167.654
             coordinates(2) = 435.587
             coordinates(3) = 98.488
             coordinates(4) = 483.471
             coordinates(5) = 98.488
             coordinates(6) = 483.471
             coordinates(7) = 167.654

             If True Then
                 Set dsPolyline2 = dsSketchManager.InsertPolyline2D(coordinates, True)
                 dsPolyline.Elevation = 100
             End If

             Dim dsCircle2 As DraftSight.Circle

             If True Then
                 Set dsCircle2 = dsSketchManager.InsertCircle(447.292, 270.87, 0#, 41.116)
             End If

             Dim dsEntities1(1) As Object
             Set dsEntities1(0) = dsPolyline2
             Set dsEntities1(1) = dsCircle2

             'Revolve entities to solid by axis
             revolves = dsSketchManager.RevolveEntitiesToSolidByAxis(dsEntities1, 447.292, 270.87, 0.0, 483.471, 167.654, 0.0, 360.0)

            'Revolve entities to surface by axis
             'surfReevolves = dsSketchManager.RevolveEntitiesToSurfaceByAxis(dsEntities1, 447.292, 270.87, 0#, 483.471, 167.654, 0#, 360#)

             Dim dsViewManager As ViewManager
             Set dsViewManager = dsDoc.GetViewManager()
             dsViewManager.SetPredefinedView dsPredefinedView_e.dsPredefinedView_SWIsometric
             Application.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

     End Sub
```
