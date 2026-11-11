---
title: "Creating Polysolid Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Creating_Polysolid_Entities_Example_VBA.htm"
---

# Creating Polysolid Entities Example (VBA)

This example shows how to create 3D polysolids.

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
' 1. Inserts a 2D polyline.
' 2. Creates a 3D polysolid using the 2D polyline.
' 3. Creates an array of coordinates.
' 4. Creates a 3D polysolid using the coordinates.
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
             coordinates(0) = 0.8839
             coordinates(1) = 7.3348
             coordinates(2) = 0.8839
             coordinates(3) = 6.0943
             coordinates(4) = 9.3647
             coordinates(5) = 6.0943
             coordinates(6) = 9.3647
             coordinates(7) = 7.3348

             If True Then
                 Set dsPolyline = dsSketchManager.InsertPolyline2D(coordinates, True)
             End If
            Dim a3DSolid As DraftSight.Solid3D

             Dim dsEntities(0) As DraftSight.PolyLine
             Set dsEntities(0) = dsPolyline
             Set a3DSolid = dsSketchManager.PolysolidByEntities( dsEntities, 4#, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left)

             Dim coordinatesArray(3) As Double
             coordinatesArray(0) = 0.6339
             coordinatesArray(1) = 3.9955
             coordinatesArray(2) = 9.3647
             coordinatesArray(3) = 3.9955

             Set a3DSolid = dsSketchManager.PolysolidByCoordinates( coordinatesArray, 4#, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left)
             Dim dsViewManager As ViewManager
             Set dsViewManager = dsDoc.GetViewManager()
             dsViewManager.SetPredefinedView dsPredefinedView_e.dsPredefinedView_SWIsometric
             Application.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

         End Sub
```
