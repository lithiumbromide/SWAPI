---
title: "Cross-sectioning Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Cross-sectioning_Entities_Example_VBA.htm"
---

# Cross-sectioning Entities Example (VBA)

This example shows how to cross-section 3D entities.

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
' 1. Extrudes a 2D polyline into a 3D entity.
' 2. Creates a CircleArc and cross-sections the 3D entity using the CircleArc. (Color red)
' 3. Creates 3 MathPoints and cross-sections the 3D entity using them. (Color yellow)
' 4. Cross-sections the 3D entity using the Z axis. (Color green)
' 5. Creates a point on the active view plane and cross-sections the 3D entity
' using the view plane. (Color cyan)
' 6. Extrudes another 2D polyline into a 3D entity.
' 7. Creates another MathPoint and uses its planes to cross-section the 3D entity:
' a. XY plane (Color blue)
' b. YZ plane (Color magenta)
' c. XZ plane (Color green)
'----------------------------------------------------------------

```vb
 Option Explicit

     Dim Application As DraftSight.Application
     Sub Main()

         'Connect to DraftSight application
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

             Dim dsMathUtility As DraftSight.MathUtility
             Set dsMathUtility = Application.GetMathUtility

             If dsMathUtility Is Nothing Then
                 Return
             End If

             Dim dsModel As Model
             Set dsModel = dsDoc.GetModel()

             If dsModel Is Nothing Then
                 Return
             End If

             Dim dsSketchManager As DraftSight.SketchManager
             Set dsSketchManager = dsModel.GetSketchManager

             If dsSketchManager Is Nothing Then
                 Return
             End If

             Dim dsPolyline As PolyLine
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

             Dim dsCircleArc As DraftSight.CircleArc

             If True Then
                 Set dsCircleArc = dsSketchManager.InsertArc(218.0505, 105.1495, 100#, 108.731070980194, 0.5990566759191, 3.74064932950889)
             End If

             Dim dsEntities(0) As PolyLine
             Set dsEntities(0) = dsPolyline

             Dim extrudes As Variant
             dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities, 50, 0, extrudes

             Dim dsEntities4(0) As Extrusion

             Dim dsExtrusion As Extrusion
             Dim i As Long
             i = 0

             Dim dsExtrudeObj As Variant
             For Each dsExtrudeObj In extrudes
                 Set dsExtrusion = dsExtrudeObj
                 Set dsEntities4(i) = dsExtrusion
                 i = i + 1
             Next

             Dim dsEntities_0(0) As DraftSight.CircleArc
             Set dsEntities_0(0) = dsCircleArc
             Dim regions As Variant
             dsSketchManager.CrossSectionEntitiesByEntity dsEntities4, dsEntities_0, regions
             changeColorProperty regions, 1
             Dim FirstPoint As DraftSight.MathPoint
             Set FirstPoint = dsMathUtility.CreatePoint(307.848, 166.459, 150#)
             Dim SecondPoint As DraftSight.MathPoint
             Set SecondPoint = dsMathUtility.CreatePoint(307.848, 166.459, 100#)
             Dim ThirdPoint As DraftSight.MathPoint
             Set ThirdPoint = dsMathUtility.CreatePoint(128.253, 43.84, 150#)
             Set regions = Nothing
             dsSketchManager.CrossSectionEntitiesBy3Points dsEntities4, FirstPoint, SecondPoint, ThirdPoint, regions
             changeColorProperty regions, 2
             Set regions = Nothing
             dsSketchManager.CrossSectionEntitiesByZAxis dsEntities4, FirstPoint, SecondPoint, regions
             changeColorProperty regions, 3
             Dim dsViewManager As ViewManager
             Set dsViewManager = dsDoc.GetViewManager()
             dsViewManager.SetPredefinedView dsPredefinedView_e.dsPredefinedView_SWIsometric
             Set regions = Nothing
             Dim PointOnActiveViewPlane As DraftSight.MathPoint
             Set PointOnActiveViewPlane = dsMathUtility.CreatePoint(128.253, 43.84, 100#)
             dsSketchManager.CrossSectionEntitiesByView dsEntities4, PointOnActiveViewPlane, regions
             changeColorProperty regions, 4

             Dim dsPolyline1 As DraftSight.PolyLine
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

             Dim dsEntities2(0) As PolyLine
             Set dsEntities2(0) = dsPolyline1
             Set extrudes = Nothing
             dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities2, 50, 0, extrudes

             Dim dsEntities3(0) As Extrusion
             Dim dsExtrusion_extr As Extrusion
             i = 0

             For Each dsExtrudeObj In extrudes
                 Set dsExtrusion_extr = dsExtrudeObj
                 Set dsEntities3(i) = dsExtrusion_extr
                 i = i + 1
             Next

             Dim PointOnActiveViewPlane2 As DraftSight.MathPoint
             Set PointOnActiveViewPlane2 = dsMathUtility.CreatePoint(515.202, -82.68, 50)
             Set regions = Nothing
             dsSketchManager.CrossSectionEntitiesByXY dsEntities3, PointOnActiveViewPlane2, regions
             changeColorProperty regions, 5
             Set regions = Nothing
             dsSketchManager.CrossSectionEntitiesByYZ dsEntities3, PointOnActiveViewPlane2, regions
             changeColorProperty regions, 6
             Set regions = Nothing
             'dsSketchManager.CrossSectionEntitiesByZX dsEntities3, PointOnActiveViewPlane2, regions
             'changeColorProperty regions, 3

             Application.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

         End Sub

      Public Sub changeColorProperty(ByVal regions As Variant, ByVal colorIndex As Integer)

         Dim dsRegion As Region
         Dim dsRegionObj As Variant

         For Each dsRegionObj In regions
             Set dsRegion = dsRegionObj
             Dim dsColor As Color
             Set dsColor = Application.GetColorByIndex(colorIndex)
             dsRegion.Color = dsColor
         Next

     End Sub
```
