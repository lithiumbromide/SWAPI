---
title: "Extruding Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Extruding_Entities_Example_VBA.htm"
---

# Extruding Entities Example (VBA)

This example shows how to extrude 3D entities.

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
' 1. Extrudes 2D entities to both 3D solids and 3D surfaces by
' both heights and paths.
' 2. Inspect the graphics area.
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
         Dim dsDoc As Document
         Set dsDoc = Application.GetActiveDocument

         If dsDoc Is Nothing Then
             Return
         End If

         Dim dsModel As Model
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
         coordinates(0) = 128.253
         coordinates(1) = 166.459
         coordinates(2) = 128.253
         coordinates(3) = 43.84
         coordinates(4) = 307.848
         coordinates(5) = 43.84
         coordinates(6) = 307.848
         coordinates(7) = 166.459

         If True Then
             Set dsPolyline = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         Dim dsCircle As DraftSight.Circle

         If True Then
             Set dsCircle = dsSketchManager.InsertCircle(221.876139410188, 159.343431635389, 0#, 103.399785372141)
         End If

         Dim dsEntities(1) As Object
         Set dsEntities(0) = dsPolyline
         Set dsEntities(1) = dsCircle

         Dim extrudes As Variant
         dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities, 20, 0, extrudes

         Dim dsExtrusion As Extrusion
         Set dsExtrusion = Nothing

         Dim dsExtrudeObj As Variant
         For Each dsExtrudeObj In extrudes
             Set dsExtrusion = dsExtrudeObj
             dsExtrusion.Height = 30
             Dim dsColor As Color
             Set dsColor = Application.GetColorByIndex(2)
             dsExtrusion.Color = dsColor
         Next

         Dim dsLine As DraftSight.Line

         If True Then
             Set dsLine = dsSketchManager.InsertLine(550#, 122#, 0#, 431#, 70#, 0#)
         End If

         Dim dsEntities1(0) As Object
         Set dsEntities1(0) = dsLine

         dsSketchManager.ExtrudeEntitiesToSurfaceByHeight dsEntities1, 20, 0, extrudes
         Dim dsExtrudedSurface As ExtrudedSurface
         Set dsExtrudedSurface = Nothing

         Dim dsExtrudedSurfaceObj As Variant
         For Each dsExtrudedSurfaceObj In extrudes
             Set dsExtrudedSurface = dsExtrudedSurfaceObj
             dsExtrudedSurface.Height = 50
         Next

         Dim dsPolyline1 As PolyLine
         coordinates(0) = 515.202
         coordinates(1) = 23.36
         coordinates(2) = 515.202
         coordinates(3) = -82.68
         coordinates(4) = 367.471
         coordinates(5) = -82.68
         coordinates(6) = 367.471
         coordinates(7) = 23.36

         If True Then
             Set dsPolyline1 = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         Dim dsLinePath As DraftSight.Line

         If True Then
             Set dsLinePath = dsSketchManager.InsertLine(734.317, 74.52, 0#, 734.317, 74.52, -309.475)
         End If

         Dim dsEntities2(0) As Object
         Set dsEntities2(0) = dsPolyline1
         Dim dsPathEntities(0) As Object
         Set dsPathEntities(0) = dsLinePath

         dsSketchManager.ExtrudeEntitiesToSolidByPath dsEntities2, dsPathEntities, 0, extrudes

         Dim dsPolyline2 As DraftSight.PolyLine
         coordinates(0) = 659.732
         coordinates(1) = 89.273
         coordinates(2) = 659.732
         coordinates(3) = 16.042
         coordinates(4) = 555.531
         coordinates(5) = 16.042
         coordinates(6) = 555.531
         coordinates(7) = 89.273

         If True Then
             Set dsPolyline2 = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         Dim dsEntities3(0) As Object
         Set dsEntities3(0) = dsPolyline2

         dsSketchManager.ExtrudeEntitiesToSurfaceByPath dsEntities3, dsPathEntities, 0, extrudes
         Dim dsViewManager As ViewManager
         Set dsViewManager = dsDoc.GetViewManager()
         dsViewManager.SetPredefinedView dsPredefinedView_e.dsPredefinedView_SWIsometric

         Application.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

     End Sub
```
