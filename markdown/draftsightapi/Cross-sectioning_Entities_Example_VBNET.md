---
title: "Cross-sectioning Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Cross-sectioning_Entities_Example_VBNET.htm"
---

# Cross-sectioning Entities Example (VB.NET)

This example shows how to cross-section 3D entities.

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
 Imports System
 Imports System.Collections.Generic
 Imports System.Linq
 Imports System.Text
 Imports System.Threading.Tasks
 Imports System.Runtime.InteropServices
 Imports DraftSight.Interop.dsAutomation
 Imports System.Diagnostics
 Module   Module1

       Dim Application  As DraftSight.Interop.dsAutomation.Application
       Sub Main()

           Application =   CType(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

            If application  Is   Nothing   Then
                   Return
               End  If

              application.AbortRunningCommand()
               Dim dsDoc  As Document = application.GetActiveDocument()

               If dsDoc  Is  Nothing   Then
                   Return
               End  If

               Dim dsMathUtility  As MathUtility = application.GetMathUtility()

               If dsMathUtility  Is   Nothing   Then
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

               Dim dsPolyline  As PolyLine

               If  True  Then
                  dsPolyline = dsSketchManager.InsertPolyline2D(New  Double() {128.253, 166.459, 128.253, 43.84, 307.848, 43.84, 307.848, 166.459},  True)
                  dsPolyline.Elevation = 100
               End  If

               Dim dsCircleArc  As CircleArc

               If  True  Then
                  dsCircleArc = dsSketchManager.InsertArc(218.0505, 105.1495, 100.0, 108.73107098019408, 0.5990566759191, 3.74064932950889)
               End  If

               Dim dsEntities  As DispatchWrapper() =  New DispatchWrapper(0) {}
              dsEntities(0) =   New DispatchWrapper(dsPolyline)
               Dim extrudes  As  Object =   Nothing
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 50, 0, extrudes)
               Dim dsExtrudeObjs  As   Object() =   CType(extrudes,   Object())
              dsEntities =   New DispatchWrapper(dsExtrudeObjs.Length - 1) {}
               Dim dsExtrusion  As Extrusion =   Nothing
               Dim i  As  Integer = 0

               For  Each dsExtrudeObj  As   Object  In dsExtrudeObjs
                  dsExtrusion =   TryCast(dsExtrudeObj, Extrusion)
                  dsEntities(i) =   New DispatchWrapper(dsExtrusion)
                  i += 1
               Next

               Dim dsEntities_0  As DispatchWrapper() =  New DispatchWrapper(0) {}
              dsEntities_0(0) =   New DispatchWrapper(dsCircleArc)
               Dim regions  As  Object =   Nothing
              dsSketchManager.CrossSectionEntitiesByEntity(dsEntities, dsEntities_0, regions)
              changeColorProperty(regions, 1)
               Dim FirstPoint  As MathPoint = dsMathUtility.CreatePoint(307.848, 166.459, 150.0)
               Dim SecondPoint  As MathPoint = dsMathUtility.CreatePoint(307.848, 166.459, 100.0)
               Dim ThirdPoint  As MathPoint = dsMathUtility.CreatePoint(128.253, 43.84, 150.0)
              regions =   Nothing
              dsSketchManager.CrossSectionEntitiesBy3Points(dsEntities, FirstPoint, SecondPoint, ThirdPoint, regions)
              changeColorProperty(regions, 2)
              regions =   Nothing
              dsSketchManager.CrossSectionEntitiesByZAxis(dsEntities, FirstPoint, SecondPoint, regions)
              changeColorProperty(regions, 3)
               Dim dsViewManager  As ViewManager = dsDoc.GetViewManager()
               If dsViewManager   IsNot   Nothing   Then dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric)
              regions =   Nothing
               Dim PointOnActiveViewPlane  As MathPoint = dsMathUtility.CreatePoint(128.253, 43.84, 100.0)
              dsSketchManager.CrossSectionEntitiesByView(dsEntities, PointOnActiveViewPlane, regions)
              changeColorProperty(regions, 4)
               Dim dsPolyline1  As PolyLine

               If  True  Then
                  dsPolyline1 = dsSketchManager.InsertPolyline2D(New  Double() {515.202, 23.36, 515.202, -82.68, 367.471, -82.68, 367.471, 23.36},  True)
               End  If

              dsEntities =   New DispatchWrapper(0) {}
              dsEntities(0) =   New DispatchWrapper(dsPolyline1)
              extrudes =   Nothing
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 50, 0, extrudes)
              dsExtrudeObjs =   CType(extrudes,   Object())
              dsEntities =   New DispatchWrapper(dsExtrudeObjs.Length - 1) {}
               Dim dsExtrusion_extr  As Extrusion =   Nothing
              i = 0

               For  Each dsExtrudeObj  As   Object  In dsExtrudeObjs
                  dsExtrusion_extr =   TryCast(dsExtrudeObj, Extrusion)
                  dsEntities(i) =   New DispatchWrapper(dsExtrusion_extr)
                  i += 1
               Next

              PointOnActiveViewPlane = dsMathUtility.CreatePoint(515.202, -82.68, 50)
              regions =   Nothing
              dsSketchManager.CrossSectionEntitiesByXY(dsEntities, PointOnActiveViewPlane, regions)
              changeColorProperty(regions, 5)
              regions =   Nothing
              dsSketchManager.CrossSectionEntitiesByYZ(dsEntities, PointOnActiveViewPlane, regions)
              changeColorProperty(regions, 6)
              regions =   Nothing
              dsSketchManager.CrossSectionEntitiesByZX(dsEntities, PointOnActiveViewPlane, regions)
              changeColorProperty(regions, 3)
              application.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)
            End  Sub

       Public  Sub changeColorProperty(ByVal regions  As   Object,   ByVal colorIndex  As   Integer)
            Dim dsRegionsObjs  As   Object() =   CType(regions,   Object())
            Dim dsRegion  As Region =   Nothing

            For  Each dsRegionObj  As   Object  In dsRegionsObjs
              dsRegion =   TryCast(dsRegionObj, Region)
               Dim dsColor  As Color = Application.GetColorByIndex(colorIndex)
              dsRegion.Color = dsColor
            Next
       End  Sub

 End  Module
```
