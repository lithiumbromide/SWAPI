---
title: "Creating Polysolid Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Creating_Polysolid_Entities_Example_VBNET.htm"
---

# Creating Polysolid Entities Example (VB.NET)

This example shows how to create 3D polysolids.

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
' 1. Inserts a 2D polyline.
' 2. Creates a 3D polysolid using the 2D polyline.
' 3. Creates an array of coordinates.
' 4. Creates a 3D polysolid using the coordinates.
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
                  dsPolyline = dsSketchManager.InsertPolyline2D(New  Double() {0.8839, 7.3348, 0.8839, 6.0943, 9.3647, 6.0943, 9.3647, 7.3348},  True)
               End  If

               Dim dsEntities  As DispatchWrapper() =  New DispatchWrapper(0) {}
              dsEntities(0) =   New DispatchWrapper(dsPolyline)
              dsSketchManager.PolysolidByEntities(dsEntities, 4.0, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left)
               Dim coordinatesArray  As   Double() =   New   Double() {0.6339, 3.9955, 9.3647, 3.9955}
              dsSketchManager.PolysolidByCoordinates(coordinatesArray, 4.0, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left)
               Dim dsViewManager  As ViewManager = dsDoc.GetViewManager()
               If dsViewManager   IsNot   Nothing   Then dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric)
              application.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)
            End  Sub

 End  Module
```
