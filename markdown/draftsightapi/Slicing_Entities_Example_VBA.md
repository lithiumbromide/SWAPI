---
title: "Slicing Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Slicing_Entities_Example_VBA.htm"
---

# Slicing Entities Example (VBA)

This example shows how to slice 3D entities.

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
' 1. Extrudes several 3D entities.
' 2. Slices 3D entities by:
' - 3 points
' - A planar entity
' - A surface
' - XY plane
' - YZ plane
' - ZX plane
' - Z axis
' - A predefined view
'----------------------------------------------------------------

```vb
 Option Explicit
Dim Application As DraftSight.Application
     Sub Main()

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

             Dim dsMathUtility As DraftSight.MathUtility
             Set dsMathUtility = Application.GetMathUtility()

             If dsMathUtility Is Nothing Then
                 Return
             End If

             Dim dsPolyline As DraftSight.PolyLine
             Dim coordinates(7) As Double
             coordinates(0) = 30.7029
             coordinates(1) = 12.4677
             coordinates(2) = 30.7029
             coordinates(3) = 10.2257
             coordinates(4) = 28.4117
             coordinates(5) = 10.2257
             coordinates(6) = 28.4117
             coordinates(7) = 12.4677

             If True Then
                 Set dsPolyline = dsSketchManager.InsertPolyline2D(coordinates, True)
             End If

             Dim dsEntities(0) As Object

             Set dsEntities(0) = dsPolyline
             Dim extrudes As Variant
             dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities, 4#, 0, extrudes

             Dim dsEntities1(0) As DraftSight.Extrusion
             Set dsEntities1(0) = extrudes(0)
             Dim FirstPoint As DraftSight.MathPoint
             Set FirstPoint = dsMathUtility.CreatePoint(28.4117, 10.2257, 4#)
             Dim SecondPoint As DraftSight.MathPoint
             Set SecondPoint = dsMathUtility.CreatePoint(30.7029, 12.4677, 4#)
             Dim ThirdPoint As DraftSight.MathPoint
             Set ThirdPoint = dsMathUtility.CreatePoint(0#, 0#, 0#)
             Dim obj As Variant
             dsSketchManager.SliceEntitiesBy3Points dsEntities1, FirstPoint, SecondPoint, ThirdPoint, True, ThirdPoint, obj
             changeColorProperty obj, 1
             Dim dsPolyline1 As DraftSight.PolyLine
             coordinates(0) = 31.3452
             coordinates(1) = 6.8946
             coordinates(2) = 31.3452
             coordinates(3) = 9.2404
             coordinates(4) = 33.888
             coordinates(5) = 9.2404
             coordinates(6) = 33.888
             coordinates(7) = 6.8946

             If True Then
                 Set dsPolyline1 = dsSketchManager.InsertPolyline2D(coordinates, True)
             End If

             Dim dsCircle As DraftSight.Circle

             If True Then
                 Set dsCircle = dsSketchManager.InsertCircle(32.6166, 8.0675, 2#, 0.98)
             End If

             Set dsEntities(0) = dsPolyline1
             Dim extrudes1 As Variant
             dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities, 4#, 0, extrudes1

             Set dsEntities1(0) = extrudes1(0)
             Dim dsEntityPlanar(0) As DraftSight.Circle
             Set dsEntityPlanar(0) = dsCircle
             Dim obj1 As Variant
             dsSketchManager.SliceEntitiesByPlanarEntity dsEntities1, dsEntityPlanar, True, ThirdPoint, obj1
             changeColorProperty obj1, 2
             Dim dsPolyline2 As DraftSight.PolyLine
             coordinates(0) = 34.5488
             coordinates(1) = 3.2662
             coordinates(2) = 34.5488
             coordinates(3) = 5.8077
             coordinates(4) = 37.1209
             coordinates(5) = 5.8077
             coordinates(6) = 37.1209
             coordinates(7) = 3.2662

             If True Then
                 Set dsPolyline2 = dsSketchManager.InsertPolyline2D(coordinates, True)
             End If

             Dim dsLine As Line

             If True Then
                 Set dsLine = dsSketchManager.InsertLine(35.8348, 3.2662, 0#, 35.8348, 5.8077, 0#)
             End If

             Set dsEntities(0) = dsPolyline2
             Dim extrudes2 As Variant
             dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities, 4#, 0, extrudes2

             Set dsEntities(0) = dsLine
             Dim extrudesSur As Variant
             dsSketchManager.ExtrudeEntitiesToSurfaceByHeight dsEntities, 4#, 0, extrudesSur

             Set dsEntities1(0) = extrudes2(0)
             Dim dsEntitySurface(0) As DraftSight.ExtrudedSurface
             Set dsEntitySurface(0) = extrudesSur(0)
             Dim obj2 As Variant
             dsSketchManager.SliceEntitiesBySurface dsEntities1, dsEntitySurface, True, ThirdPoint, obj2
             changeColorProperty obj2, 3
             Dim dsPolyline3 As DraftSight.PolyLine
             coordinates(0) = 37.9451
             coordinates(1) = -0.4819
             coordinates(2) = 37.9451
             coordinates(3) = 2.3739
             coordinates(4) = 40.64
             coordinates(5) = 2.3739
             coordinates(6) = 40.64
             coordinates(7) = -0.4819

             If True Then
                 Set dsPolyline3 = dsSketchManager.InsertPolyline2D(coordinates, True)
             End If

             Set dsEntities(0) = dsPolyline3
             Dim extrudes3 As Variant
             dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities, 4#, 0, extrudes3

             Set dsEntities1(0) = extrudes3(0)
             Dim obj3 As Variant
             dsSketchManager.SliceEntitiesByXY dsEntities1, dsMathUtility.CreatePoint(37.9451, -0.4819, 2#), True, ThirdPoint, obj3
             changeColorProperty obj3, 4
             Dim dsPolyline4 As DraftSight.PolyLine
             coordinates(0) = 41.2617
             coordinates(1) = -4.0399
             coordinates(2) = 41.2617
             coordinates(3) = -1.1841
             coordinates(4) = 43.9566
             coordinates(5) = -1.1841
             coordinates(6) = 43.9566
             coordinates(7) = -4.0399

             If True Then
                 Set dsPolyline4 = dsSketchManager.InsertPolyline2D(coordinates, True)
             End If

             Set dsEntities(0) = dsPolyline4
             Dim extrudes4 As Variant
             dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities, 4#, 0, extrudes4

             Set dsEntities1(0) = extrudes4(0)
             Dim obj4 As Variant
             dsSketchManager.SliceEntitiesByYZ dsEntities1, dsMathUtility.CreatePoint(42.60915, -4.0399, 4#), True, ThirdPoint, obj4
             changeColorProperty obj4, 5
             Dim dsPolyline5 As DraftSight.PolyLine
             coordinates(0) = 44.7029
             coordinates(1) = -7.6823
             coordinates(2) = 44.7029
             coordinates(3) = -4.8264
             coordinates(4) = 47.3978
             coordinates(5) = -4.8264
             coordinates(6) = 47.3978
             coordinates(7) = -7.6823

             If True Then
                 Set dsPolyline5 = dsSketchManager.InsertPolyline2D(coordinates, True)
             End If

             Set dsEntities(0) = dsPolyline5
             Dim extrudes5 As Variant
             dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities, 4#, 0, extrudes5

             Set dsEntities1(0) = extrudes5(0)
             Dim obj5 As Variant
             dsSketchManager.SliceEntitiesByZX dsEntities1, dsMathUtility.CreatePoint(44.7029, -6.25435, 4#), True, ThirdPoint, obj5
             changeColorProperty obj5, 6
             Dim dsPolyline6 As DraftSight.PolyLine
             coordinates(0) = 48.056
             coordinates(1) = -11.3057
             coordinates(2) = 48.056
             coordinates(3) = -8.4498
             coordinates(4) = 50.7509
             coordinates(5) = -8.4498
             coordinates(6) = 50.7509
             coordinates(7) = -11.3057

             If True Then
                 Set dsPolyline6 = dsSketchManager.InsertPolyline2D(coordinates, True)
             End If

             Set dsEntities(0) = dsPolyline6
             Dim extrudes6 As Variant
             dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities, 4#, 0, extrudes6

             Set dsEntities1(0) = extrudes6(0)
             Dim obj6 As Variant
             dsSketchManager.SliceEntitiesByZAxis dsEntities1, dsMathUtility.CreatePoint(49.4034, -11.3057, 0#), dsMathUtility.CreatePoint(50.7509, -11.3057, 2#), True, ThirdPoint, obj6
             changeColorProperty obj6, 2
             Dim dsPolyline7 As DraftSight.PolyLine
             coordinates(0) = 51.3856
             coordinates(1) = -14.871
             coordinates(2) = 51.3856
             coordinates(3) = -12.0151
             coordinates(4) = 54.0805
             coordinates(5) = -12.0151
             coordinates(6) = 54.0805
             coordinates(7) = -14.871

             If True Then
                 Set dsPolyline7 = dsSketchManager.InsertPolyline2D(coordinates, True)
             End If

             Set dsEntities(0) = dsPolyline7
             Dim extrudes7 As Variant
             dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities, 4#, 0, extrudes7

             Set dsEntities1(0) = extrudes7(0)
             Dim dsViewManager As ViewManager
             Set dsViewManager = dsDoc.GetViewManager()
             dsViewManager.SetPredefinedView (dsPredefinedView_e.dsPredefinedView_SWIsometric)
             Dim obj7 As Variant
             dsSketchManager.SliceEntitiesByView dsEntities1, dsMathUtility.CreatePoint(52.733, -14.871, 0#), True, ThirdPoint, obj7
             changeColorProperty obj7, 3
             Application.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing

         End Sub

     Public Sub changeColorProperty(ByVal solid As Variant, ByVal colorIndex As Integer)

         Dim dsSolid As DraftSight.Solid3D
         Dim dsSolidObj As Variant

         For Each dsSolidObj In solid
             Set dsSolid = dsSolidObj
             Dim dsColor As Color
             Set dsColor = Application.GetColorByIndex(colorIndex)
             dsSolid.Color = dsColor
         Next
     End Sub
```
