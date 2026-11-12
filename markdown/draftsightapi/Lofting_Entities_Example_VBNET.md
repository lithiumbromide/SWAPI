---
title: "Lofting Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Lofting_Entities_Example_VBNET.htm"
---

# Lofting Entities Example (VB.NET)

This example shows how to loft entities.

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
 Imports System
 Imports System.Collections.Generic
 Imports System.Linq
 Imports System.Text
 Imports System.Threading.Tasks
 Imports System.Runtime.InteropServices
 Imports System.Reflection
 Imports DraftSight.Interop.dsAutomation

 Module   Module1

       Sub Main()

            Dim Application  As DraftSight.Interop.dsAutomation.Application
           Application =   CType(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

            If Application  Is   Nothing   Then
               Return
            End  If

           Application.AbortRunningCommand()
            Dim dsDoc  As Document = Application.GetActiveDocument()

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

            Dim dsPolyline  As PolyLine

            If  True  Then
              dsPolyline = dsSketchManager.InsertPolyline2D(New  Double() {128.253, 166.459, 128.253, 43.84, 307.848, 43.84, 307.848, 166.459},  True)
              dsPolyline.Elevation = 100
            End  If

            Dim dsCircle  As Circle

            If  True  Then
              dsCircle = dsSketchManager.InsertCircle(221.87613941018759, 159.34343163538875, 0.00000000000000, 103.39978537214083)
            End  If

            Dim dsLine  As Line

            If  True  Then
              dsLine = dsSketchManager.InsertLine(432.58, 113.544, 0, 432.58, 113.544, -155.752)
            End  If

            Dim dsEntities  As DispatchWrapper() =  New DispatchWrapper(1) {}
           dsEntities(0) =   New DispatchWrapper(dsPolyline)
           dsEntities(1) =   New DispatchWrapper(dsCircle)
            Dim dsGuideEntities  As DispatchWrapper() =  New DispatchWrapper(0) {}
           dsGuideEntities(0) =   New DispatchWrapper(dsLine)
            Dim dsLoft  As Loft

            If  True  Then
              dsLoft = dsSketchManager.LoftEntitiesToSolidByGuides(dsEntities,   False, dsGuideEntities, dsLoftSurfaceNormalOption_e.dsLoftSurfaceNormalOption_SmoothFit, dsLoftedSurfaceNormalOption_e.dsLoftedSurfaceNormalOption_SmoothFit, 0, 0, 0, 0)
            End  If

            ' Loft entities to surface by guides
            ' LoftedSurface dsLoftedSurface = dsSketchManager.LoftEntitiesToSurfaceByGuides(dsEntities, false,
            '    dsGuideEntities, dsLoftSurfaceNormalOption_e.dsLoftSurfaceNormalOption_SmoothFit,
            '    dsLoftedSurfaceNormalOption_e.dsLoftedSurfaceNormalOption_SmoothFit, 0, 0, 0, 0);

            If dsLoft  Is  Nothing   Then
               Return
            End  If

            Dim dsPolyline1  As PolyLine

            If  True  Then
              dsPolyline1 = dsSketchManager.InsertPolyline2D(New  Double() {486.181, 78.416, 486.181, 246.617, 675.147, 246.617, 675.147, 78.416},  True)
              dsPolyline1.Elevation = 100
            End  If

            Dim dsPolyline2  As PolyLine

            If  True  Then
              dsPolyline2 = dsSketchManager.InsertPolyline2D(New   Double() {546.401, 200.933, 546.401, 123.062, 675.147, 123.062, 675.147, 200.933},   True)
            End  If

            Dim dsLine1  As Line

            If  True  Then
              dsLine1 = dsSketchManager.InsertLine(486.181, 246.617, 100, 546.401, 200.933, 0)
            End  If

           dsEntities =   New DispatchWrapper(1) {}
           dsEntities(0) =   New DispatchWrapper(dsPolyline1)
           dsEntities(1) =   New DispatchWrapper(dsPolyline2)
            Dim dsPathEntities  As DispatchWrapper() =  New DispatchWrapper(0) {}
           dsPathEntities(0) =   New DispatchWrapper(dsLine1)
            Dim dsLoft_1  As Loft

            If  True  Then
              dsLoft_1 = dsSketchManager.LoftEntitiesToSolidByPath(dsEntities,   False, dsPathEntities, dsLoftSurfaceNormalOption_e.dsLoftSurfaceNormalOption_SmoothFit, dsLoftedSurfaceNormalOption_e.dsLoftedSurfaceNormalOption_SmoothFit, 0, 0, 0, 0)
            End  If

            ' Loft entities to surface by path
            ' LoftedSurface dsLoftedSurface = dsSketchManager.LoftEntitiesToSurfaceByPath(dsEntities, false,
            '    dsPathEntities, dsLoftSurfaceNormalOption_e.dsLoftSurfaceNormalOption_SmoothFit,
            '    dsLoftedSurfaceNormalOption_e.dsLoftedSurfaceNormalOption_SmoothFit, 0, 0, 0, 0);

            Dim dsViewManager  As ViewManager = dsDoc.GetViewManager()
            If dsViewManager   IsNot   Nothing   Then dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric)
           Application.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)

       End  Sub

 End  Module
```
