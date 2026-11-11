---
title: "Extruding Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Extruding_Entities_Example_VBNET.htm"
---

# Extruding Entities Example (VB.NET)

This example shows how to extrude 3D entities.

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
' 1. Extrudes 2D entities to both 3D solids and 3D surfaces by
' both heights and paths.
' 2. Inspect the graphics area.
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

            Dim Application  As DraftSight.Interop.dsAutomation.Application
           Application =   CType(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

            If application  Is   Nothing   Then
               Return
            End  If

           application.AbortRunningCommand()
            Dim dsDoc  As Document = application.GetActiveDocument()

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
            End  If

            Dim dsCircle  As Circle

            If  True  Then
              dsCircle = dsSketchManager.InsertCircle(221.87613941018759, 159.34343163538875, 0.00000000000000, 103.39978537214083)
            End  If

            Dim dsEntities  As DispatchWrapper() =  New DispatchWrapper(1) {}
           dsEntities(0) =   New DispatchWrapper(dsPolyline)
           dsEntities(1) =   New DispatchWrapper(dsCircle)
            Dim extrudes  As  Object =   Nothing
           dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 20, 0, extrudes)
            Dim dsExtrudeObjs  As   Object() =   CType(extrudes,   Object())
            Dim dsExtrusion  As Extrusion =   Nothing

            For  Each dsExtrudeObj  As   Object  In dsExtrudeObjs
              dsExtrusion =   TryCast(dsExtrudeObj, Extrusion)
              dsExtrusion.Height = 30
               Dim dsColor  As Color = application.GetColorByIndex(2)
              dsExtrusion.Color = dsColor
            Next

            Dim dsLine  As Line

            If  True  Then
              dsLine = dsSketchManager.InsertLine(550.0, 122.0, 0.0, 431.0, 70.0, 0.0)
            End  If

           dsEntities =   New DispatchWrapper(0) {}
           dsEntities(0) =   New DispatchWrapper(dsLine)
           extrudes =   Nothing
           dsSketchManager.ExtrudeEntitiesToSurfaceByHeight(dsEntities, 20, 0, extrudes)
            Dim dsExtrudedSurface  As ExtrudedSurface =   Nothing
           dsExtrudeObjs =   CType(extrudes,   Object())

            For  Each dsExtrudedSurfaceObj  As   Object  In dsExtrudeObjs
              dsExtrudedSurface =   TryCast(dsExtrudedSurfaceObj, ExtrudedSurface)
              dsExtrudedSurface.Height = 50
            Next

            Dim dsPolyline1  As PolyLine

            If  True  Then
              dsPolyline1 = dsSketchManager.InsertPolyline2D(New  Double() {515.202, 23.36, 515.202, -82.68, 367.471, -82.68, 367.471, 23.36},  True)
            End  If

            Dim dsLinePath  As Line

            If  True  Then
              dsLinePath = dsSketchManager.InsertLine(734.317, 74.52, 0.0, 734.317, 74.52, -309.475)
            End  If

           dsEntities =   New DispatchWrapper(0) {}
           dsEntities(0) =   New DispatchWrapper(dsPolyline1)
            Dim dsPathEntities  As DispatchWrapper() =  New DispatchWrapper(0) {}
           dsPathEntities(0) =   New DispatchWrapper(dsLinePath)
           extrudes =   Nothing
           dsSketchManager.ExtrudeEntitiesToSolidByPath(dsEntities, dsPathEntities, 0, extrudes)
            Dim dsPolyline2  As PolyLine

            If  True  Then
              dsPolyline2 = dsSketchManager.InsertPolyline2D(New  Double() {659.732, 89.273, 659.732, 16.042, 555.531, 16.042, 555.531, 89.273},  True)
            End  If

           dsEntities =   New DispatchWrapper(0) {}
           dsEntities(0) =   New DispatchWrapper(dsPolyline2)
           extrudes =   Nothing
           dsSketchManager.ExtrudeEntitiesToSurfaceByPath(dsEntities, dsPathEntities, 0, extrudes)
            Dim dsViewManager  As ViewManager = dsDoc.GetViewManager()
            If dsViewManager   IsNot   Nothing   Then dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric)
          Application.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)

       End  Sub

 End  Module
```
