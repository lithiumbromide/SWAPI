---
title: "Create Tracker Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Tracker_Example_VBNET.htm"
---

# Create Tracker Example (VB.NET)

This example shows how to create a tracker and add a temporary entity to the tracker.

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
' 1. Creates a temporary Circle for the tracker.
' 2. Creates a tracker and adds the temporary Circle to the
'    the tracker.
' 3. Examine the pointer in the drawing to verify.
' 4. Prompts you to click in the drawing to insert a Circle.
' 5. Inserts a Circle in the drawing at the point where you clicked.
'----------------------------------------------------------------

Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System
Imports System.Windows.Forms

Module Module_1

    Public WithEvents dsTracker As Tracker

    Public dsApp As DraftSight.Interop.dsAutomation.Application
    Public dsTempCircle As Circle

    Public Sub Main()

        'Connect to DraftSight application
        dsApp = DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

        ' Abort any command currently running in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand()

        If dsApp Is Nothing Then
            Return
        End If

        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        'Get Sketch Manager
        Dim dsSketchMgr As SketchManager = dsDoc.GetModel().GetSketchManager()

        'Create temporary Circle
        dsApp.TemporaryEntityMode = True
        dsTempCircle = dsSketchMgr.InsertCircle(0, 0, 0, 10)
        dsApp.TemporaryEntityMode = False

        'Create tracker and add temporary Circle
        Dim dsTracker As Tracker = dsApp.CreateTracker()
        dsTracker.AddTemporaryEntity(dsTempCircle)

        'Prompt for point where to insert Circle
        'Before prompt, add tracker to command message
        Dim dsCmdMsg As CommandMessage = dsApp.GetCommandMessage()
        dsCmdMsg.AddTracker(dsTracker)

        Dim X As Double = 0.0
        Dim Y As Double = 0.0
        Dim Z As Double = 0.0
        AddHandler dsTracker.UpdateNotify, AddressOf dsTracker_UpdateNotify
        Dim res As Boolean = dsCmdMsg.PromptForPoint("Click to insert Circle", X, Y, Z)
        RemoveHandler dsTracker.UpdateNotify, AddressOf dsTracker_UpdateNotify

        If res = True Then
            'Set the center of the Circle where user clicked
            dsTempCircle.SetCenter(X, Y, Z)
            'Add temporary Circle to drawing
            dsSketchMgr.AddTemporaryEntity(dsTempCircle)
        End If

        'Remove tracker from command message if no longer needed
        dsCmdMsg.RemoveTracker(dsTracker)

    End Sub

    Private Sub dsTracker_UpdateNotify(ByVal CursorPosition As MathPoint) Handles dsTracker.UpdateNotify
        If CursorPosition Is Nothing Then
            Return
        End If

        Dim x As Double = 0.0, y As Double = 0.0, z As Double = 0.0
        CursorPosition.GetPosition(x, y, z)

        dsTempCircle.SetCenter(x, y, z)

    End Sub

End Module
```
