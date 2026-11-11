---
title: "Create Highlight Selection Set Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Highlight_Selection_Set_Example_VBNET.htm"
---

# Create Highlight Selection Set Example (VB.NET)

This example shows how to create a highlight selection set.

```
'--------------------------------------------------------------
' Preconditions:
'  1. Create a VB.NET Windows console project.
'  2. Copy and paste this example into the VB.NET IDE.
'  3. Add a reference to:
'     install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
'  4. Add a reference to System.Windows.Forms.
'  5. Start DraftSight.
'  6. Press F5.
'
' Postconditions:
'  1. Connects to DraftSight.
'  2. Gets active document.
'  3. Gets Sketch Manager.
'  4. Inserts a Circle and an Arc.
'  5. Creates an instance of a highlight selection set.
'  6. Adds Arc to the highlight selection set.
'  7. Move the pointer over both the Arc and Circle. Only the Arc
'     is highlighted. Press F5 to continue.
'  8. Removes Arc from highlight selection set.
'  9. Adds Circle to highlight selection set.
' 10. Move the pointer over both the Arc and Circle. Only
'     the Circle is highlighted.
'--------------------------------------------------------------

Imports System
Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms

Module Module1

    Sub Main()

        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connect to DraftSight application
        dsApp = DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

        If dsApp Is Nothing Then
            Return
        End If

        'Abort any command currently running in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand()

        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        'Get Sketch Manager
        Dim dsSketchMgr As SketchManager = dsDoc.GetModel().GetSketchManager()

        'Draw a Circle and Arc
        Dim dsCircle As Circle = dsSketchMgr.InsertCircle(5.0, 5.0, 0.0, 10.0)
        Dim dsCircleArc As CircleArc = dsSketchMgr.InsertArc(7.5, 7.5, 0.0, 10.0, 2.5, 5.0)
        dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing)

        'Create highlight selection set
        Dim dsEntities As DispatchWrapper() = New DispatchWrapper(0) {}
        dsEntities(0) = New DispatchWrapper(dsCircleArc)

        Dim dsHighlightSet As HighlightSet = dsDoc.CreateHighlightSet(dsEntities)
        dsHighlightSet.Highlight = True
        dsDoc.Rebuild(dsRebuildType_e.dsRebuildType_AllViewports)

        System.Diagnostics.Debugger.Break()
        'Move pointer over the Arc and Circle
        'Only the Arc is highlighted
        'Press F5 to continue

        'Remove entities from highlight selection set
        dsHighlightSet.RemoveEntities(dsEntities)
        dsDoc.Rebuild(dsRebuildType_e.dsRebuildType_AllViewports)

        'Add Circle to highlight selection set
        dsEntities.Initialize()
        dsEntities(0) = New DispatchWrapper(dsCircle)
        dsHighlightSet.AddEntities(dsEntities)
        dsHighlightSet.Highlight = True
        dsDoc.Rebuild(dsRebuildType_e.dsRebuildType_AllViewports)

        'Move pointer over the Arc and Circle
        'Only the Circle is highlighted

    End Sub
End Module
```
