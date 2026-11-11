---
title: "Change DimensionStyle Options of Leader Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Change_DimensionStyle_Options_of_Leader_Example_VBNET.htm"
---

# Change DimensionStyle Options of Leader Example (VB.NET)

This example shows how to change the DimensionStyle arrow and text options of a specific Leader. The DimensionStyle arrow and text options of all other existing and new Leaders use the DimensionStyle options of the drawing.

```
'-----------------------------------------------------------------
' Preconditions:
' 1.  Create a VB.NET console project.
' 2.  Copy and paste this example into the VB.NET IDE.
' 3.  Add a reference to:
'     install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4.  Start DraftSight and open a document.
' 5.  Start debugging the project.

' Postconditions:
' 1.  Draws two Leaders, DSUserData and DS.
' 2.  Gets DimensionStyleUserData for DSUserData Leader.
' 3.  Gets arrow options for DSUserData Leader.
' 4.  Modifies DSUserData Leader's arrow options only.
' 5.  Zooms to fit the drawing and execution stops.
' 6.  Examine the drawing to verify that only DSUserData Leader's
'     arrow changed.
' 7.  Press F10 to step through the rest of the project
'     and examine the drawing after each call.
' 8.  Gets text options for DSUserData Leader.
' 9.  Modifies DSUserData Leader's text options only.
' 10. Inserts third Leader, DS2.
' 11. Examine the drawing to verify that DS and DS2 Leaders
'     have the same arrow and text options.
'----------------------------------------------------------------

Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices

Module Module1

    Sub Main()
        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connect to DraftSight application
        dsApp = DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

        If dsApp Is Nothing Then
            Return
        End If

        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox("There are no open documents in DraftSight.")
            Return
        End If

        'Get Sketch Manager
        Dim dsModel As Model
        Dim dsSketchMgr As SketchManager
        dsModel = dsDoc.GetModel()
        dsSketchMgr = dsModel.GetSketchManager()

        'Insert first Leader
        Dim Coordinates As Double() = New Double() {0, 0, 0, 4, 4, 0, 10, 4, 0}
        Dim Width As Double = 5.0
        Dim myNote As String = "DSUserData"
        Dim dsLeader As Leader
        dsLeader = dsSketchMgr.InsertLeader(Coordinates, Width, myNote)

        'Insert second Leader
        Dim Coordinates2 As Double() = New Double() {8, 8, 8, 8, 8, 8, 20, 8, 8}
        Dim myNote2 As String = "DS"
        Dim dsLeader2 As Leader
        dsLeader2 = dsSketchMgr.InsertLeader(Coordinates2, Width, myNote2)

        'Zoom to fit
        dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

        'Examine the drawing
        'Press F10 to step through project
        Stop

        'Get DimensionStyleUserData for DSUserData Leader
        Dim dsDimStyleUserData As DimensionStyleUserData
        dsDimStyleUserData = dsLeader.GetDimensionStyleUserData()

        'Get DimensionStyleArrowsOptions for DSUserData Leader
        Dim dsArrowsOptions As DimensionStyleArrowsOptions
        dsArrowsOptions = dsDimStyleUserData.GetDimensionStyleArrowsOptions()

        'Set arrow size for DSUserData Leader
        dsArrowsOptions.Size = 1.0

        'Set arrow type for DSUserData Leader
        dsArrowsOptions.SetLeaderArrow(dsDimensionArrowType_e.dsDimensionArrowType_Dot, "")

        'Get DimensionStyleTextOptions for DSUserData Leader
        Dim dsTextOptions As DimensionStyleTextOptions
        dsTextOptions = dsDimStyleUserData.GetDimensionStyleTextOptions()

        'Set text vertical position for DSUserData Leader
        dsTextOptions.VerticalPosition = dsDimensionTextVerticalPosition_e.dsDimensionTextVerticalPosition_Centered

        'Insert third Leader
        Dim Coordinates3 As Double() = New Double() {16, 16, 16, 16, 16, 16, 40, 16, 16}
        Dim myNote3 As String = "DS2"
        Dim dsLeader3 As Leader
        dsLeader3 = dsSketchMgr.InsertLeader(Coordinates3, Width, myNote3)

        'Zoom to fit
        dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

        'Examine the drawing to verify that DS and DS2 Leaders
        'have the same arrow and text options

    End Sub

End Module
```
