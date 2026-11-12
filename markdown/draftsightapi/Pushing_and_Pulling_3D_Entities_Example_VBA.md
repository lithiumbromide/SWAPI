---
title: "Pushing and Pulling 3D Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Pushing_and_Pulling_3D_Entities_Example_VBA.htm"
---

# Pushing and Pulling 3D Entities Example (VBA)

This example shows how to pull out a 3D entity.

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
' 1. Inserts a 2D polyline and a circle.
' 2. Creates a point on the 2D polyline.
' 3. Pulls out a 3D entity from the point on the 2D polyline.
'----------------------------------------------------------------

```vb
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
         coordinates(0) = 308.611
         coordinates(1) = 244.543
         coordinates(2) = 308.611
         coordinates(3) = 133.606
         coordinates(4) = 440.093
         coordinates(5) = 133.606
         coordinates(6) = 440.093
         coordinates(7) = 244.543

         If True Then
             Set dsPolyline = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         Dim dsCircle As DraftSight.Circle

         If True Then
             Set dsCircle = dsSketchManager.InsertCircle(60.029, 196.265, 0#, 100#)
         End If

         Dim dsMathUtility As DraftSight.MathUtility
         Set dsMathUtility = Application.GetMathUtility()
         Dim InternalPoint As DraftSight.MathPoint
         Set InternalPoint = dsMathUtility.CreatePoint(308.611, 244.543, 0#)
         Dim bRetVal As Boolean
         bRetVal = dsSketchManager.PushPullEntities(InternalPoint, 300)
         Dim dsViewManager As ViewManager
         Set dsViewManager = dsDoc.GetViewManager()
         dsViewManager.SetPredefinedView dsPredefinedView_e.dsPredefinedView_SWIsometric
         Application.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

     End Sub
```
