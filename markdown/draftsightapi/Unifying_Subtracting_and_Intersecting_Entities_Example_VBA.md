---
title: "Unifying, Subtracting, and Intersecting Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Unifying_Subtracting_and_Intersecting_Entities_Example_VBA.htm"
---

# Unifying, Subtracting, and Intersecting Entities Example (VBA)

This example shows how to perform union, subtract, and intersect operations on 3D solids.

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
' 1. Inserts 2D polylines and creates 3D polysolids from them.
' 2. Performs union, subtract, and intersect operations on the 3D polysolids.
' 3. Inspect the graphics area and Immediate window.
'----------------------------------------------------------------

```vb
 Option Explicit
 Sub Main()

         Dim dsApp As DraftSight.Application
         'Connect to DraftSight application
         Set dsApp = GetObject(, "DraftSight.Application")

         dsApp.AbortRunningCommand
         Dim dsDoc As Document
         Set dsDoc = dsApp.GetActiveDocument

         If dsDoc Is Nothing Then
             Return
         End If

         Dim dsModel As Model
         Set dsModel = dsDoc.GetModel

         If dsModel Is Nothing Then
             Return
         End If

         Dim dsSketchManager As DraftSight.SketchManager
         Set dsSketchManager = dsModel.GetSketchManager

         If dsSketchManager Is Nothing Then
             Return
         End If

         Dim dsViewManager As ViewManager
         Set dsViewManager = dsDoc.GetViewManager()
         dsViewManager.SetPredefinedView (dsPredefinedView_e.dsPredefinedView_SWIsometric)
         dsApp.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

         Dim dsPolyline As PolyLine
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

         Dim dsPolyline2 As PolyLine
         coordinates(0) = 5.8839
         coordinates(1) = 12.3348
         coordinates(2) = 5.8839
         coordinates(3) = 11.0943
         coordinates(4) = 14.3647
         coordinates(5) = 11.0943
         coordinates(6) = 14.3647
         coordinates(7) = 12.3348

         If True Then
             Set dsPolyline2 = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         dsApp.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing
         Dim dsEntities(0) As PolyLine
         Set dsEntities(0) = dsPolyline
         Dim dsSolid3D_1 As Solid3D
         Set dsSolid3D_1 = dsSketchManager.PolysolidByEntities(dsEntities, 4#, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left)
         Set dsEntities(0) = dsPolyline2
         Dim dsSolid3D_2 As Solid3D
         Set dsSolid3D_2 = dsSketchManager.PolysolidByEntities(dsEntities, 4#, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left)

         Dim dsEntities2(1) As Solid3D
         Set dsEntities2(0) = dsSolid3D_1
         Set dsEntities2(1) = dsSolid3D_2

         Dim obj As Variant
         Dim reg(0) As Solid3D

         dsSketchManager.UnionEntities dsEntities2, obj
         dsApp.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

         Set reg(0) = obj(0)
         Debug.Print "Union solid type as defined in dsSolidType_e: " & reg(0).SolidType

         Dim dsPolyline3 As PolyLine
         coordinates(0) = 22.507
         coordinates(1) = 8.2407
         coordinates(2) = 22.507
         coordinates(3) = 13.8125
         coordinates(4) = 36.4164
         coordinates(5) = 13.8125
         coordinates(6) = 36.4164
         coordinates(7) = 8.2407

         If True Then
             Set dsPolyline3 = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         Dim dsPolyline4 As PolyLine
         coordinates(0) = 30.7029
         coordinates(1) = 12.4677
         coordinates(2) = 30.7029
         coordinates(3) = 10.2257
         coordinates(4) = 28.4117
         coordinates(5) = 10.2257
         coordinates(6) = 28.4117
         coordinates(7) = 12.4677

         If True Then
             Set dsPolyline4 = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         Set dsEntities(0) = dsPolyline3
         Dim extrudes As Variant
         dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities, 4#, 0, extrudes

         Dim dsEntities1(0) As Extrusion
         Set dsEntities1(0) = extrudes(0)

         Dim dsEntities3(0) As PolyLine
         Set dsEntities3(0) = dsPolyline4
         Set extrudes = Nothing
         dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities3, 4#, 0, extrudes
         Dim dsExtrudeObjs2(0) As Object

         Dim dsEntities4(0) As Extrusion
         Set dsEntities4(0) = extrudes(0)

         dsSketchManager.SubtractEntities dsEntities4, dsEntities1, obj
         dsApp.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

         Set reg(0) = obj(0)
         Debug.Print "Subtract solid type as defined in dsSolidType_e: " & reg(0).SolidType

         Dim dsPolyline5 As PolyLine
         coordinates(0) = 22.178
         coordinates(1) = 3.6354
         coordinates(2) = 22.178
         coordinates(3) = -2.0369
         coordinates(4) = 36.1998
         coordinates(5) = -2.0369
         coordinates(6) = 36.1998
         coordinates(7) = 3.6354

         If True Then
             Set dsPolyline5 = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         Dim dsPolyline6 As PolyLine
         coordinates(0) = 36.1998
         coordinates(1) = -2.0369
         coordinates(2) = 36.1998
         coordinates(3) = 2.124
         coordinates(4) = 30.3079
         coordinates(5) = 2.124
         coordinates(6) = 30.3079
         coordinates(7) = -2.0369

         If True Then
             Set dsPolyline6 = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         dsApp.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

         Set dsEntities(0) = dsPolyline5
         Dim dsSolid3D_3 As Solid3D
         Set dsSolid3D_3 = dsSketchManager.PolysolidByEntities(dsEntities, 4#, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left)

         Set dsEntities(0) = dsPolyline6
         Dim dsSolid3D_4 As Solid3D
          Set dsSolid3D_4 = dsSketchManager.PolysolidByEntities(dsEntities, 4#, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left)

         Set dsEntities2(0) = dsSolid3D_3
         Set dsEntities2(1) = dsSolid3D_4
         dsSketchManager.IntersectEntities dsEntities2, obj
         dsApp.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

         Set reg(0) = obj(0)
         Debug.Print "Intersect solid type as defined in dsSolidType_e: " & reg(0).SolidType

     End Sub
```
