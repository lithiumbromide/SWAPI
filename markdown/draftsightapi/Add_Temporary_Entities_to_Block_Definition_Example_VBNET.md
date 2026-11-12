---
title: "Add Temporary Entities to Block Definition Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Add_Temporary_Entities_to_Block_Definition_Example_VBNET.htm"
---

# Add Temporary Entities to Block Definition Example (VB.NET)

This example shows how to add temporary entities to a Block definition and Block Instance.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add references to System and System.Windows.Forms.
' 5. Start DraftSight and open a document.
' 6. Start debugging the project.
'
' Postconditions:
' 1. Creates Block definition with one element, a Circle.
' 2. Inserts Block instance.
' 3. Zooms to fit the drawing and execution stops.
' 4. Press F10 to step through the rest of the project
'    and examine the drawing after each call.
' 5. Creates temporary entities, two Circles.
' 6. Modifies temporary entities.
' 7. Adds temporary entities to Block definition and Block
'    instance.
'----------------------------------------------------------------

Imports System
Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms

Module Module1

    Sub Main()

        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connect to DraftSight application
        dsApp = GetObject(, "DraftSight.Application")

        If dsApp Is Nothing Then
            Return
        End If
```

```
        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand()

        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        Dim dsModel As Model
        Dim dsSketchMgr As SketchManager
        dsModel = dsDoc.GetModel()
        dsSketchMgr = dsModel.GetSketchManager()

        'Create Block definition with one element, a Circle
        Dim dsCircle As Circle = dsSketchMgr.InsertCircle(0, 0, 0, 5)
        Dim dsEntities As DispatchWrapper() = New DispatchWrapper(0) {}
        Dim dsEntityTypes As Integer() = New Integer(0) {}
        dsEntities(0) = New DispatchWrapper(dsCircle)
        dsEntityTypes(0) = CInt(dsObjectType_e.dsCircleType)
        Dim dsBlkDef As BlockDefinition = dsDoc.CreateBlockDefinition("SampleBlock", "Sample block definition", 0, 0, 0, dsEntityTypes, _
         dsEntities, dsBlockDefinitionEntities_e.dsBlockDefinitionEntities_RemoveFromDrawing)

        dsSketchMgr.InsertBlock2("SampleBlock", 0, 0, 0, 1, 1, 1, 0)

        'Zoom to fit
        dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

        'Examine the drawing
        'to verify that a Block instance
        'was inserted
        'Press F10 to continue
        System.Diagnostics.Debugger.Break()

        'Create temporary entities, which are not added to drawing

        'Turn temporary entity mode on
        dsApp.TemporaryEntityMode = True

        'Create temporary Circles
        Dim dsTempCircle1 As Circle = dsSketchMgr.InsertCircle(0, 0, 0, 5)
        Dim dsTempCircle2 As Circle = dsSketchMgr.InsertCircle(0, 0, 0, 5)

        'Turn temporary entity mode off
        dsApp.TemporaryEntityMode = False

        'Modify Circles, which you cannot see
        Dim PointOnCurveX As Double = 0.0
        Dim PointOnCurveY As Double = 0.0
        Dim PointOnCurveZ As Double = 0.0
        dsCircle.GetClosestPointOn(2.5, 2.5, 0, PointOnCurveX, PointOnCurveY, PointOnCurveZ)
        dsTempCircle1.SetCenter(PointOnCurveX, PointOnCurveY, PointOnCurveZ)

        dsTempCircle1.GetClosestPointOn(PointOnCurveX + 2.5, PointOnCurveY + 2.5, PointOnCurveZ, PointOnCurveX, PointOnCurveY, PointOnCurveZ)
        dsTempCircle2.SetCenter(PointOnCurveX, PointOnCurveY, PointOnCurveZ)

        'Zoom to fit
        dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

        'Add temporary Circles to Block definition
        'Block instance updates accordingly
        dsBlkDef.AddTemporaryEntity(dsTempCircle1)
        dsBlkDef.AddTemporaryEntity(dsTempCircle2)

        'Zoom to fit
        dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

    End Sub

End Module
```
