---
title: "Sweeping Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Sweeping_Entities_Example_VBNET.htm"
---

# Sweeping Entities Example (VB.NET)

This example shows how to sweep 3D entities.

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
' 1. Inserts a 2D polyline and a path line.
' 2. Sweeps the 2D polyline along the path line to create a 3D solid.
' 3. Inserts a 2D polyline and a path line.
' 4. Sweeps the 2D polyline along the path line to create a 3D surface.
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

            Dim dsPolyline1  As PolyLine

            If  True  Then
              dsPolyline1 = dsSketchManager.InsertPolyline2D(New   Double() {0.8839, 7.3348, 0.8839, 6.0943, 9.3647, 6.0943, 9.3647, 7.3348},   True)
            End  If

            Dim dsLine1  As Line

            If  True  Then
              dsLine1 = dsSketchManager.InsertLine(1.6048, 1.4138, 0.0000, 1.9225, 7.8519, 0.0000)
            End  If

            Dim dsEntitiesSo  As DispatchWrapper() =  New DispatchWrapper(0) {}
           dsEntitiesSo(0) =   New DispatchWrapper(dsPolyline1)
           dsSketchManager.SweepEntitiesToSolid(dsEntitiesSo, dsLine1,   True,   False,   False, 0.0, 0.0, 0.0, 1.0, 0.0)
            Dim dsPolyline2  As PolyLine

            If  True  Then
              dsPolyline2 = dsSketchManager.InsertPolyline2D(New  Double() {10.8839, 17.3348, 10.8839, 16.0943, 19.3647, 16.0943, 19.3647, 17.3348},  True)
            End  If

            Dim dsLine2  As Line

            If  True  Then
              dsLine2 = dsSketchManager.InsertLine(10.6048, 10.4138, 0.0000, 10.9225, 17.8519, 0.0000)
            End  If

            Dim dsEntitiesSu  As DispatchWrapper() =  New DispatchWrapper(0) {}
           dsEntitiesSu(0) =   New DispatchWrapper(dsPolyline2)
           dsSketchManager.SweepEntitiesToSurface(dsEntitiesSu, dsLine2,   True,   False,   False, 0.0, 0.0, 0.0, 1.0, 0.0)

            Dim dsViewManager  As ViewManager = dsDoc.GetViewManager()
            If dsViewManager   IsNot   Nothing   Then dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric)
           Application.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)

       End  Sub

 End  Module
```
