---
title: "Add Temporary Entities to Block Definition Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Add_Temporary_Entities_to_Block_Definition_Example_VBA.htm"
---

# Add Temporary Entities to Block Definition Example (VBA)

This example shows how to add temporary entities to a Block definition and Block Instance.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Run the macro.
'
' Postconditions:
' 1. Creates Block definition with one element, a Circle.
' 2. Inserts Block instance.
' 3. Zooms to fit the drawing and execution stops.
' 4. Press F8 to step through the rest of the project
'    and examine the drawing after each call.
' 5. Creates temporary entities, two Circles.
' 6. Modifies temporary entities.
' 7. Adds temporary entities to Block definition and Block
'    instance.
'----------------------------------------------------------------
Option Explicit
```

```
    Sub main()
```

```
        Dim dsApp As DraftSight.Application
```

```
        'Connect to DraftSight application
        Set dsApp = GetObject(, "DraftSight.Application")
```

```
        If dsApp Is Nothing Then
            Return
        End If
```

```
        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        'Get active document
        Dim dsDoc As DraftSight.Document
        Set dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox ("There are no open documents in DraftSight.")
            Return
        End If
```

```
        Dim dsModel As DraftSight.Model
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsModel = dsDoc.GetModel()
        Set dsSketchMgr = dsModel.GetSketchManager()
```

```
        'Create Block definition with one element, a Circle
        Dim dsCircle As DraftSight.Circle
        Set dsCircle = dsSketchMgr.InsertCircle(0, 0, 0, 5)
        Dim dsEntities(0) As Object
        Dim dsEntityTypes(0) As Long
        Set dsEntities(0) = dsCircle
        dsEntityTypes(0) = dsObjectType_e.dsCircleType
        Dim dsBlkDef As DraftSight.BlockDefinition
        Set dsBlkDef = dsDoc.CreateBlockDefinition("SampleBlock", "Sample block definition", 0, 0, 0, dsEntityTypes, dsEntities, dsBlockDefinitionEntities_RemoveFromDrawing)
```

```
        dsSketchMgr.InsertBlock2 "SampleBlock", 0, 0, 0, 1, 1, 1, 0
```

```
        'Zoom to fit
        dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
```

```
        'Examine the drawing
        'to verify that a Block instance
        'was inserted
        'Press F8 to continue
        Stop
```

```
        'Create temporary entities, which are not added to drawing
```

```
        'Turn temporary entity mode on
        dsApp.TemporaryEntityMode = True
```

```
        'Create temporary Circles
        Dim dsTempCircle1 As DraftSight.Circle
        Set dsTempCircle1 = dsSketchMgr.InsertCircle(0, 0, 0, 5)
        Dim dsTempCircle2 As DraftSight.Circle
        Set dsTempCircle2 = dsSketchMgr.InsertCircle(0, 0, 0, 5)
```

```
        'Turn temporary entity mode off
        dsApp.TemporaryEntityMode = False
```

```
        'Modify Circles, which you cannot see
        Dim PointOnCurveX As Double
        PointOnCurveX = 0#
        Dim PointOnCurveY As Double
        PointOnCurveY = 0#
        Dim PointOnCurveZ As Double
        PointOnCurveZ = 0#
        dsCircle.GetClosestPointOn 2.5, 2.5, 0, PointOnCurveX, PointOnCurveY, PointOnCurveZ
        dsTempCircle1.SetCenter PointOnCurveX, PointOnCurveY, PointOnCurveZ
```

```
        dsTempCircle1.GetClosestPointOn PointOnCurveX + 2.5, PointOnCurveY + 2.5, PointOnCurveZ, PointOnCurveX, PointOnCurveY, PointOnCurveZ
        dsTempCircle2.SetCenter PointOnCurveX, PointOnCurveY, PointOnCurveZ
```

```
        'Zoom to fit
        dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
```

```
        'Add temporary Circles to Block definition
        'Block instance updates accordingly
        dsBlkDef.AddTemporaryEntity dsTempCircle1
        dsBlkDef.AddTemporaryEntity dsTempCircle2
```

```
        'Zoom to fit
        dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
```

```
    End Sub
```
