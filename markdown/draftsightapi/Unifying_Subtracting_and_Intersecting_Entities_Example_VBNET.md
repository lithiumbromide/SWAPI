---
title: "Unifying, Subtracting, and Intersecting Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Unifying_Subtracting_and_Intersecting_Entities_Example_VBNET.htm"
---

# Unifying, Subtracting, and Intersecting Entities Example (VB.NET)

This example shows how to perform union, subtract, and intersect operations on 3D solids.

'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this project into the VB.NET IDE.
' 3. Add a reference to
' `install_dir\`**APISDK\tlb\DraftSight.Interop.dsAutomation.dll**
' 4. Start DraftSight.
' 5. Press F5 to debug the project.
'
' Postconditions:
' 1. Inserts 2D polylines and creates 3D polysolids from them.
' 2. Performs union, subtract, and intersect operations on the 3D polysolids.
' 3. Inspect the graphics area.
'----------------------------------------------------------------

```vb
 Imports System
 Imports System.Collections.Generic
 Imports System.Linq
 Imports System.Text
 Imports System.Threading.Tasks
 Imports System.Runtime.InteropServices
 Imports DraftSight.Interop.dsAutomation
 Module   Module1

       Sub Main()

            Dim dsApp  As DraftSight.Interop.dsAutomation.Application
           dsApp =  CType(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)
           dsApp.AbortRunningCommand()
            Dim dsDoc  As Document = dsApp.GetActiveDocument()

            If dsDoc  Is  Nothing   Then
               Return
            End  If

            Dim dsModel  As Model = dsDoc.GetModel()

            If dsModel  Is  Nothing   Then
               Return
            End  If

            Dim dsSketchManager  As SketchManager = dsModel.GetSketchManager()

            If dsSketchManager  Is   Nothing   Then
               Return
            End  If

            Dim dsViewManager  As ViewManager = dsDoc.GetViewManager()
          If dsViewManager   IsNot   Nothing   Then dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric)
           dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)
            Dim dsPolyline  As PolyLine

            If  True  Then
              dsPolyline = dsSketchManager.InsertPolyline2D(New  Double() {0.8839, 7.3348, 0.8839, 6.0943, 9.3647, 6.0943, 9.3647, 7.3348},  True)
            End  If

            Dim dsPolyline2  As PolyLine

            If  True  Then
              dsPolyline2 = dsSketchManager.InsertPolyline2D(New   Double() {5.8839, 12.3348, 5.8839, 11.0943, 14.3647, 11.0943, 14.3647, 12.3348},   True)
            End  If

           dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)
            Dim dsEntities  As DispatchWrapper() =  New DispatchWrapper(0) {}
           dsEntities(0) =   New DispatchWrapper(dsPolyline)
            Dim dsSolid3D_1  As Solid3D = dsSketchManager.PolysolidByEntities(dsEntities, 4.0, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left)
           dsEntities =   New DispatchWrapper(0) {}
           dsEntities(0) =   New DispatchWrapper(dsPolyline2)
            Dim dsSolid3D_2  As Solid3D = dsSketchManager.PolysolidByEntities(dsEntities, 4.0, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left)
           dsEntities =   New DispatchWrapper(1) {}
           dsEntities(0) =   New DispatchWrapper(dsSolid3D_1)
           dsEntities(1) =   New DispatchWrapper(dsSolid3D_2)
            Dim obj  As  Object
           dsSketchManager.UnionEntities(dsEntities, obj)
           dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)
            Dim dsPolyline3  As PolyLine

            If  True  Then
              dsPolyline3 = dsSketchManager.InsertPolyline2D(New  Double() {22.507, 8.2407, 22.507, 13.8125, 36.4164, 13.8125, 36.4164, 8.2407},  True)
            End  If

            Dim dsPolyline4  As PolyLine

            If  True  Then
              dsPolyline4 = dsSketchManager.InsertPolyline2D(New  Double() {30.7029, 12.4677, 30.7029, 10.2257, 28.4117, 10.2257, 28.4117, 12.4677},  True)
            End  If

           dsEntities =   New DispatchWrapper(0) {}
           dsEntities(0) =   New DispatchWrapper(dsPolyline3)
            Dim extrudes  As  Object =   Nothing
           dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0, extrudes)
            Dim dsExtrudeObjs  As   Object() =   CType(extrudes,   Object())
            Dim dsEntities2  As DispatchWrapper() =  New DispatchWrapper(0) {}
           dsEntities2(0) =   New DispatchWrapper(dsPolyline4)
           extrudes =   Nothing
           dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities2, 4.0, 0, extrudes)
            Dim dsExtrudeObjs2  As   Object() =   CType(extrudes,   Object())
           dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)
           dsEntities =   New DispatchWrapper(0) {}
           dsEntities(0) =   New DispatchWrapper(CType(dsExtrudeObjs(0), Extrusion))
           dsEntities2 =   New DispatchWrapper(0) {}
           dsEntities2(0) =   New DispatchWrapper(CType(dsExtrudeObjs2(0), Extrusion))
           dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)
           dsSketchManager.SubtractEntities(dsEntities2, dsEntities, obj)
           dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)
            Dim dsPolyline5  As PolyLine

            If  True  Then
              dsPolyline5 = dsSketchManager.InsertPolyline2D(New  Double() {22.178, 3.6354, 22.178, -2.0369, 36.1998, -2.0369, 36.1998, 3.6354},  True)
            End  If

            Dim dsPolyline6  As PolyLine

            If  True  Then
              dsPolyline6 = dsSketchManager.InsertPolyline2D(New  Double() {36.1998, -2.0369, 36.1998, 2.124, 30.3079, 2.124, 30.3079, -2.0369},  True)
            End  If

           dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)
           dsEntities =   New DispatchWrapper(0) {}
           dsEntities(0) =   New DispatchWrapper(dsPolyline5)
            Dim dsSolid3D_3  As Solid3D = dsSketchManager.PolysolidByEntities(dsEntities, 4.0, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left)
           dsEntities =   New DispatchWrapper(0) {}
           dsEntities(0) =   New DispatchWrapper(dsPolyline6)
            Dim dsSolid3D_4  As Solid3D = dsSketchManager.PolysolidByEntities(dsEntities, 4.0, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left)
           dsEntities =   New DispatchWrapper(1) {}
           dsEntities(0) =   New DispatchWrapper(dsSolid3D_3)
           dsEntities(1) =   New DispatchWrapper(dsSolid3D_4)
           dsSketchManager.IntersectEntities(dsEntities, obj)
           dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)
       End  Sub

 End  Module
```
