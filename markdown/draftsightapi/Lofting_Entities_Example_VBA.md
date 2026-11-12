---
title: "Lofting Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Lofting_Entities_Example_VBA.htm"
---

# Lofting Entities Example (VBA)

This example shows how to loft entities.

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
' 1. Inserts a 2D polyline, a circle, and a guide line.
' 2. Lofts the polyline and circle to solids using the guide line.
' 3. Inserts two 2D polylines and a path line.
' 4. Lofts the polylines to solids using the path line.
' 5. Inspect the graphics area.
'
' Optional: Open a new document. Comment out the two solid loft methods,
' uncomment the two surface loft methods, and rerun the macro.
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
         Set dsDoc = Application.GetActiveDocument()

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
             dsPolyline.Elevation = 100
         End If

         Dim dsCircle As DraftSight.Circle

         If True Then
             Set dsCircle = dsSketchManager.InsertCircle(221.876139410188, 159.343431635389, 0#, 103.399785372141)
         End If

         Dim dsLine As Line

         If True Then
             Set dsLine = dsSketchManager.InsertLine(432.58, 113.544, 0, 432.58, 113.544, -155.752)
         End If

         Dim dsEntities(1) As Object
         Set dsEntities(0) = dsPolyline
         Set dsEntities(1) = dsCircle
         Dim dsGuideEntities(0) As Object
         Set dsGuideEntities(0) = dsLine
         Dim dsLoft As Loft

         If True Then
             Set dsLoft = dsSketchManager.LoftEntitiesToSolidByGuides(dsEntities, False, dsGuideEntities, dsLoftSurfaceNormalOption_e.dsLoftSurfaceNormalOption_SmoothFit, dsLoftedSurfaceNormalOption_e.dsLoftedSurfaceNormalOption_SmoothFit, 0, 0, 0, 0)
         End If

         ' Loft entities to surface by guides
        ' Dim dsLoftedSurface As DraftSight.LoftedSurface
         ' dsLoftedSurface = dsSketchManager.LoftEntitiesToSurfaceByGuides(dsEntities, false,
         '     dsGuideEntities, dsLoftSurfaceNormalOption_e.dsLoftSurfaceNormalOption_SmoothFit,
         '     dsLoftedSurfaceNormalOption_e.dsLoftedSurfaceNormalOption_SmoothFit, 0, 0, 0, 0);

         If dsLoft Is Nothing Then
             Return
         End If

         Dim dsPolyline1 As DraftSight.PolyLine
         coordinates(0) = 486.181
         coordinates(1) = 78.416
         coordinates(2) = 486.181
         coordinates(3) = 246.617
         coordinates(4) = 675.147
         coordinates(5) = 246.617
         coordinates(6) = 675.147
         coordinates(7) = 78.416

         If True Then
             Set dsPolyline1 = dsSketchManager.InsertPolyline2D(coordinates, True)
             dsPolyline1.Elevation = 100
         End If

         Dim dsPolyline2 As DraftSight.PolyLine
         coordinates(0) = 546.401
         coordinates(1) = 200.933
         coordinates(2) = 546.401
         coordinates(3) = 123.062
         coordinates(4) = 675.147
         coordinates(5) = 123.062
         coordinates(6) = 675.147
         coordinates(7) = 200.933

         If True Then
             Set dsPolyline2 = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         Dim dsLine1 As DraftSight.Line

         If True Then
             Set dsLine1 = dsSketchManager.InsertLine(486.181, 246.617, 100, 546.401, 200.933, 0)
         End If

         Dim dsEntities2(1) As Object
         Set dsEntities2(0) = dsPolyline1
         Set dsEntities2(1) = dsPolyline2
         Dim dsPathEntities(0) As Object
         Set dsPathEntities(0) = dsLine1
         Dim dsLoft_1 As DraftSight.Loft

         If True Then
             Set dsLoft_1 = dsSketchManager.LoftEntitiesToSolidByPath(dsEntities2, False, dsPathEntities, dsLoftSurfaceNormalOption_e.dsLoftSurfaceNormalOption_SmoothFit, dsLoftedSurfaceNormalOption_e.dsLoftedSurfaceNormalOption_SmoothFit, 0, 0, 0, 0)
         End If

         ' Loft entities to surface by path
         ' dsLoftedSurface = dsSketchManager.LoftEntitiesToSurfaceByPath(dsEntities2, false,
         '    dsPathEntities, dsLoftSurfaceNormalOption_e.dsLoftSurfaceNormalOption_SmoothFit,
         '     dsLoftedSurfaceNormalOption_e.dsLoftedSurfaceNormalOption_SmoothFit, 0, 0, 0, 0);

         Dim dsViewManager As ViewManager
         Set dsViewManager = dsDoc.GetViewManager()
         dsViewManager.SetPredefinedView (dsPredefinedView_e.dsPredefinedView_SWIsometric)

         Application.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

     End Sub
```
