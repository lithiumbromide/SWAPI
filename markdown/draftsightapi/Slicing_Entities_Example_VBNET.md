---
title: "Slicing Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Slicing_Entities_Example_VBNET.htm"
---

# Slicing Entities Example (VB.NET)

This example shows how to slice 3D entities.

' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this project into the VB.NET IDE.
' 3. Add a reference to
' `install_dir\`**APISDK\tlb\DraftSight.Interop.dsAutomation.dll**
' 4. Start DraftSight.
' 5. Press F5 to debug the project.
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
 Imports System
 Imports System.Collections.Generic
 Imports System.Linq
 Imports System.Text
 Imports System.Threading.Tasks
 Imports System.Runtime.InteropServices
 Imports DraftSight.Interop.dsAutomation

 Module Module1
     Public Application As DraftSight.Interop.dsAutomation.Application
     Sub Main()

         Application = CType(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

         If application Is Nothing Then
                 Return
             End If

             application.AbortRunningCommand()
             Dim dsDoc As Document = application.GetActiveDocument()

             If dsDoc Is Nothing Then
                 Return
             End If

             Dim dsModel As Model = dsDoc.GetModel()

             If dsModel Is Nothing Then
                 Return
             End If

             Dim dsSketchManager As SketchManager = dsModel.GetSketchManager()

             If dsSketchManager Is Nothing Then
                 Return
             End If

             Dim dsMathUtility As MathUtility = application.GetMathUtility()

             If dsMathUtility Is Nothing Then
                 Return
             End If

             Dim dsEntities As DispatchWrapper()
             Dim dsPolyline As PolyLine

             If True Then
                 dsPolyline = dsSketchManager.InsertPolyline2D(New Double() {30.7029, 12.4677, 30.7029, 10.2257, 28.4117, 10.2257, 28.4117, 12.4677}, True)
             End If

             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(dsPolyline)
             Dim extrudes As Object = Nothing
             dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0, extrudes)
             Dim dsExtrudeObjs As Object() = CType(extrudes, Object())
             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(CType(dsExtrudeObjs(0), Extrusion))
             Dim FirstPoint As MathPoint = dsMathUtility.CreatePoint(28.4117, 10.2257, 4.0)
             Dim SecondPoint As MathPoint = dsMathUtility.CreatePoint(30.7029, 12.4677, 4.0)
             Dim ThirdPoint As MathPoint = dsMathUtility.CreatePoint(0.0, 0.0, 0.0)
             Dim obj As Object
             dsSketchManager.SliceEntitiesBy3Points(dsEntities, FirstPoint, SecondPoint, ThirdPoint, True, ThirdPoint, obj)
             changeColorProperty(obj, 1)
             Dim dsPolyline1 As PolyLine

             If True Then
                 dsPolyline1 = dsSketchManager.InsertPolyline2D(New Double() {31.3452, 6.8946, 31.3452, 9.2404, 33.888, 9.2404, 33.888, 6.8946}, True)
             End If

             Dim dsCircle As Circle

             If True Then
                 dsCircle = dsSketchManager.InsertCircle(32.6166, 8.0675, 2.0, 0.98)
             End If

             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(dsPolyline1)
             Dim extrudes1 As Object = Nothing
             dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0, extrudes1)
             Dim dsExtrudeObjs1 As Object() = CType(extrudes1, Object())
             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(CType(dsExtrudeObjs1(0), Extrusion))
             Dim dsEntityPlanar As DispatchWrapper() = New DispatchWrapper(0) {}
             dsEntityPlanar(0) = New DispatchWrapper(dsCircle)
             Dim obj1 As Object
             dsSketchManager.SliceEntitiesByPlanarEntity(dsEntities, dsEntityPlanar, True, ThirdPoint, obj1)
             changeColorProperty(obj1, 2)
             Dim dsPolyline2 As PolyLine

             If True Then
                 dsPolyline2 = dsSketchManager.InsertPolyline2D(New Double() {34.5488, 3.2662, 34.5488, 5.8077, 37.1209, 5.8077, 37.1209, 3.2662}, True)
             End If

             Dim dsLine As Line

             If True Then
                 dsLine = dsSketchManager.InsertLine(35.8348, 3.2662, 0.0000, 35.8348, 5.8077, 0.0000)
             End If

             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(dsPolyline2)
             Dim extrudes2 As Object = Nothing
             dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0, extrudes2)
             Dim dsExtrudeObjs2 As Object() = CType(extrudes2, Object())
             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(dsLine)
             Dim extrudesSur As Object = Nothing
             dsSketchManager.ExtrudeEntitiesToSurfaceByHeight(dsEntities, 4.0, 0, extrudesSur)
             Dim dsExtrudeObjsSur As Object() = CType(extrudesSur, Object())
             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(CType(dsExtrudeObjs2(0), Extrusion))
             Dim dsEntitySurface As DispatchWrapper() = New DispatchWrapper(0) {}
             dsEntitySurface(0) = New DispatchWrapper(CType(dsExtrudeObjsSur(0), ExtrudedSurface))
             Dim obj2 As Object
             dsSketchManager.SliceEntitiesBySurface(dsEntities, dsEntitySurface, True, ThirdPoint, obj2)
             changeColorProperty(obj2, 3)
             Dim dsPolyline3 As PolyLine

             If True Then
                 dsPolyline3 = dsSketchManager.InsertPolyline2D(New Double() {37.9451, -0.4819, 37.9451, 2.3739, 40.64, 2.3739, 40.64, -0.4819}, True)
             End If

             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(dsPolyline3)
             Dim extrudes3 As Object = Nothing
             dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0, extrudes3)
             Dim dsExtrudeObjs3 As Object() = CType(extrudes3, Object())
             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(CType(dsExtrudeObjs3(0), Extrusion))
             Dim obj3 As Object
             dsSketchManager.SliceEntitiesByXY(dsEntities, dsMathUtility.CreatePoint(37.9451, -0.4819, 2.0), True, ThirdPoint, obj3)
             changeColorProperty(obj3, 4)
             Dim dsPolyline4 As PolyLine

             If True Then
                 dsPolyline4 = dsSketchManager.InsertPolyline2D(New Double() {41.2617, -4.0399, 41.2617, -1.1841, 43.9566, -1.1841, 43.9566, -4.0399}, True)
             End If

             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(dsPolyline4)
             Dim extrudes4 As Object = Nothing
             dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0, extrudes4)
             Dim dsExtrudeObjs4 As Object() = CType(extrudes4, Object())
             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(CType(dsExtrudeObjs4(0), Extrusion))
             Dim obj4 As Object
             dsSketchManager.SliceEntitiesByYZ(dsEntities, dsMathUtility.CreatePoint(42.60915, -4.0399, 4.0), True, ThirdPoint, obj4)
             changeColorProperty(obj4, 5)
             Dim dsPolyline5 As PolyLine

             If True Then
                 dsPolyline5 = dsSketchManager.InsertPolyline2D(New Double() {44.7029, -7.6823, 44.7029, -4.8264, 47.3978, -4.8264, 47.3978, -7.6823}, True)
             End If

             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(dsPolyline5)
             Dim extrudes5 As Object = Nothing
             dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0, extrudes5)
             Dim dsExtrudeObjs5 As Object() = CType(extrudes5, Object())
             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(CType(dsExtrudeObjs5(0), Extrusion))
             Dim obj5 As Object
             dsSketchManager.SliceEntitiesByZX(dsEntities, dsMathUtility.CreatePoint(44.7029, -6.25435, 4.0), True, ThirdPoint, obj5)
             changeColorProperty(obj5, 6)
             Dim dsPolyline6 As PolyLine

             If True Then
                 dsPolyline6 = dsSketchManager.InsertPolyline2D(New Double() {48.056, -11.3057, 48.056, -8.4498, 50.7509, -8.4498, 50.7509, -11.3057}, True)
             End If

             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(dsPolyline6)
             Dim extrudes6 As Object = Nothing
             dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0, extrudes6)
             Dim dsExtrudeObjs6 As Object() = CType(extrudes6, Object())
             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(CType(dsExtrudeObjs6(0), Extrusion))
             Dim obj6 As Object
             dsSketchManager.SliceEntitiesByZAxis(dsEntities, dsMathUtility.CreatePoint(49.4034, -11.3057, 0.0), dsMathUtility.CreatePoint(50.7509, -11.3057, 2.0), True, ThirdPoint, obj6)
             changeColorProperty(obj6, 2)
             Dim dsPolyline7 As PolyLine

             If True Then
                 dsPolyline7 = dsSketchManager.InsertPolyline2D(New Double() {51.3856, -14.871, 51.3856, -12.0151, 54.0805, -12.0151, 54.0805, -14.871}, True)
             End If

             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(dsPolyline7)
             Dim extrudes7 As Object = Nothing
             dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0, extrudes7)
             Dim dsExtrudeObjs7 As Object() = CType(extrudes7, Object())
             dsEntities = New DispatchWrapper(0) {}
             dsEntities(0) = New DispatchWrapper(CType(dsExtrudeObjs7(0), Extrusion))
             Dim dsViewManager As ViewManager = dsDoc.GetViewManager()
             If dsViewManager IsNot Nothing Then dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric)
             Dim obj7 As Object
             dsSketchManager.SliceEntitiesByView(dsEntities, dsMathUtility.CreatePoint(52.733, -14.871, 0.0), True, ThirdPoint, obj7)
             changeColorProperty(obj7, 3)
             application.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)
         End Sub

     Public Sub changeColorProperty(ByVal solid As Object, ByVal colorIndex As Integer)
         Dim dsSolidsObjs As Object() = CType(solid, Object())
         Dim dsSolid As Solid3D = Nothing

         For Each dsSolidObj As Object In dsSolidsObjs
             dsSolid = TryCast(dsSolidObj, Solid3D)
             Dim dsColor As Color = Application.GetColorByIndex(colorIndex)
             dsSolid.Color = dsColor
         Next
     End Sub

 End Module
```
