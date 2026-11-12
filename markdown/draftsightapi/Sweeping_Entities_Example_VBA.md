---
title: "Sweeping Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Sweeping_Entities_Example_VBA.htm"
---

# Sweeping Entities Example (VBA)

This example shows how to sweep 3D entities.

'--------------------------------------------------------------
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
' 1. Inserts a 2D polyline and a path line.
' 2. Sweeps the 2D polyline along the path line to create a 3D solid.
' 3. Inserts a 2D polyline and a path line.
' 4. Sweeps the 2D polyline along the path line to create a 3D surface.
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

         Dim dsPolyline1 As DraftSight.PolyLine
         Dim coordinates(7) As Double
         coordinates(0) = 0.8839
         coordinates(1) = 7.3348
         coordinates(2) = 0.8839
         coordinates(3) = 6.0943
         coordinates(4) = 9.3647
         coordinates(5) = 6.0943
         coordinates(6) = 9.3647
         coordinates(7) = 7.3348

         If True Then
             Set dsPolyline1 = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         Dim dsLine1 As DraftSight.Line

         If True Then
             Set dsLine1 = dsSketchManager.InsertLine(1.6048, 1.4138, 0#, 1.9225, 7.8519, 0#)
         End If

         Dim dsEntitiesSo(0) As DraftSight.PolyLine
         Set dsEntitiesSo(0) = dsPolyline1
        Dim sweepArr As Variant
         sweepArr = dsSketchManager.SweepEntitiesToSolid (dsEntitiesSo, dsLine1, True, False, False, 0#, 0#, 0#, 1#, 0#)
         Dim dsPolyline2 As DraftSight.PolyLine
         coordinates(0) = 10.8839
         coordinates(1) = 17.3348
         coordinates(2) = 10.8839
         coordinates(3) = 16.0943
         coordinates(4) = 19.3647
         coordinates(5) = 16.0943
         coordinates(6) = 19.3647
         coordinates(7) = 17.3348

         If True Then
             Set dsPolyline2 = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         Dim dsLine2 As DraftSight.Line

         If True Then
             Set dsLine2 = dsSketchManager.InsertLine(10.6048, 10.4138, 0#, 10.9225, 17.8519, 0#)
         End If

         Dim dsEntitiesSu(0) As DraftSight.PolyLine
         Set dsEntitiesSu(0) = dsPolyline2
        Dim surfSweepArr As Variant
         surfSweepArr = dsSketchManager.SweepEntitiesToSurface (dsEntitiesSu, dsLine2, True, False, False, 0#, 0#, 0#, 1#, 0#)

         Dim dsViewManager As ViewManager
         Set dsViewManager = dsDoc.GetViewManager()
         dsViewManager.SetPredefinedView (dsPredefinedView_e.dsPredefinedView_SWIsometric)
         Application.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

     End Sub
```
