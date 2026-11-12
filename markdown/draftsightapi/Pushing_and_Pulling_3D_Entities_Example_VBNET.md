---
title: "Pushing and Pulling 3D Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Pushing_and_Pulling_3D_Entities_Example_VBNET.htm"
---

# Pushing and Pulling 3D Entities Example (VB.NET)

This example shows how to pull out a 3D entity.

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
' 1. Inserts a 2D polyline and a circle.
' 2. Creates a point on the 2D polyline.
' 3. Pulls out a 3D entity from the point on the 2D polyline.
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
              dsPolyline = dsSketchManager.InsertPolyline2D(New  Double() {308.611, 244.543, 308.611, 133.606, 440.093, 133.606, 440.093, 244.543},  True)
            End  If

            Dim dsCircle  As Circle

            If  True  Then
              dsCircle = dsSketchManager.InsertCircle(60.029, 196.265, 0.0, 100.0)
            End  If

            Dim dsMathUtility  As MathUtility = application.GetMathUtility()
            Dim InternalPoint  As MathPoint = dsMathUtility.CreatePoint(308.611, 244.543, 0.0)
            Dim bRetVal  As  Boolean = dsSketchManager.PushPullEntities(InternalPoint, 300)
            Dim dsViewManager  As ViewManager = dsDoc.GetViewManager()
            If dsViewManager   IsNot   Nothing   Then dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric)
          Application.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)

       End  Sub

 End  Module
```
