---
title: "Revolving Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Revolving_Entities_Example_VBNET.htm"
---

# Revolving Entities Example (VB.NET)

This example shows how to revolve 3D entities.

--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this project into the VB.NET IDE.
' 3. Add a reference to
' `install_dir\`**APISDK\tlb\DraftSight.Interop.dsAutomation.dll**
' 4. Start DraftSight.
' 5. Press F5 to debug the project.
'
' Postconditions:
' 1. Inserts a 2D polyline, a circle, and an axis.
' 2. Revolves the 2D polyline and circle about the axis into a 3D solid.
' 3. Changes the color of the revolved entities.
' 4. Inserts a 2D polyline and a circle.
' 5. Revolves the 2D polyline and circle about the X axis into a 3D solid.
' 6. Inserts a 2D polyline and a circle.
' 7. Revolves the 2D polyline and circle about the specified axis
' and angle of revolution to a surface.
' 8. Inspect the graphics area.
'
' Optional: Open a new document, comment out the solid/surface revolve methods,
' uncomment the other solid/surface revolve methods, and rerun
' the macro.
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
                  dsPolyline = dsSketchManager.InsertPolyline2D(New  Double() {-231.229, 148, -231.229, 76.963, -157.191, 76.963, -157.191, 148},  True)
                  dsPolyline.Elevation = 100
              End  If

               Dim dsCircle  As Circle

               If  True  Then
                  dsCircle = dsSketchManager.InsertCircle(-199.212, 233.044, 0.0, 48.357)
               End  If

               Dim dsLine  As Line

               If  True  Then
                  dsLine = dsSketchManager.InsertLine(-111.167, 282.069, 0, -111.167, 83.966, 0)
               End  If

               Dim dsEntities  As DispatchWrapper() =  New DispatchWrapper(1) {}
              dsEntities(0) =   New DispatchWrapper(dsPolyline)
              dsEntities(1) =   New DispatchWrapper(dsCircle)
               Dim revolveArray  As DispatchWrapper() =  New DispatchWrapper(0) {}
              revolveArray(0) =   New DispatchWrapper(dsLine)
               Dim revolves  As  Object =   Nothing
              revolves = dsSketchManager.RevolveEntitiesToSolidByObject(dsEntities, revolveArray, 360.0)
               Dim dsRevolve  As Revolve =   Nothing

            For  Each dsRevolveObj  As   Object  In   CType(revolves,   Object())
              dsRevolve =   TryCast(dsRevolveObj, Revolve)
               Dim dsColor  As Color = application.GetColorByIndex(3)
              dsRevolve.Color = dsColor
            Next

            'Revolve entities to surface by object
            'revolves = dsSketchManager.RevolveEntitiesToSurfaceByObject(dsEntities, revolveArray, 360.0)

            Dim dsPolyline1  As PolyLine

               If  True  Then
                  dsPolyline1 = dsSketchManager.InsertPolyline2D(New  Double() {107.848, 158.077, 107.848, 74.014, 212.128, 74.014, 212.128, 158.077},  True)
                  dsPolyline.Elevation = 100
               End  If

               Dim dsCircle1  As Circle

               If  True  Then
                  dsCircle1 = dsSketchManager.InsertCircle(153.603, 252.781, 0.0, 52.831)
               End  If

              dsEntities =   New DispatchWrapper(1) {}
              dsEntities(0) =   New DispatchWrapper(dsPolyline1)
              dsEntities(1) =   New DispatchWrapper(dsCircle1)
              revolves =   Nothing
           revolves = dsSketchManager.RevolveEntitiesToSolidByXAxis(dsEntities, 360.0,   True)

            'Revolve entities to surface by X axis
            'revolves = dsSketchManager.RevolveEntitiesToSurfaceByXAxis(dsEntities, 360.0, True)

            Dim dsPolyline2  As PolyLine

               If  True  Then
                  dsPolyline2 = dsSketchManager.InsertPolyline2D(New  Double() {435.587, 167.654, 435.587, 98.488, 483.471, 98.488, 483.471, 167.654},  True)
                  dsPolyline.Elevation = 100
               End  If

               Dim dsCircle2  As Circle

               If  True  Then
                  dsCircle2 = dsSketchManager.InsertCircle(447.292, 270.87, 0.0, 41.116)
               End  If

              dsEntities =   New DispatchWrapper(1) {}
              dsEntities(0) =   New DispatchWrapper(dsPolyline2)
              dsEntities(1) =   New DispatchWrapper(dsCircle2)
           revolves =   Nothing

            'Revolve entities to solid by axis
            'revolves = dsSketchManager.RevolveEntitiesToSolidByAxis(dsEntities, 447.292, 270.87, 0.0, 483.471, 167.654, 0.0, 360.0)

           revolves = dsSketchManager.RevolveEntitiesToSurfaceByAxis(dsEntities, 447.292, 270.87, 0.0, 483.471, 167.654, 0.0, 360.0)

            Dim dsViewManager  As ViewManager = dsDoc.GetViewManager()
            If dsViewManager   IsNot   Nothing   Then dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric)
           Application.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)

       End  Sub

 End  Module
```
