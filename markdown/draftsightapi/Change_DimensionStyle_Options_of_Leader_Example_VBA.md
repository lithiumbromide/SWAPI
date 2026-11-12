---
title: "Change Dimension Style Options of Leader Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Change_DimensionStyle_Options_of_Leader_Example_VBA.htm"
---

# Change Dimension Style Options of Leader Example (VBA)

This example shows how to change the DimensionStyle arrow and text options of a specific Leader. The DimensionStyle arrow and text options of all other existing and new Leaders use the DimensionStyle options of the drawing.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a drawing document.
' 5. Press F8 to step through the macro.
'
' Postconditions:
' 1.  Draws two Leaders, DSUserData and DS.
' 2.  Gets DimensionStyleUserData for DSUserData Leader.
' 3.  Gets arrow options for DSUserData Leader.
' 4.  Modifies DSUserData Leader's arrow options only.
' 5.  Zooms to fit the drawing and execution stops.
' 6.  Examine the drawing to verify that only DSUserData Leader's
'     arrow changed.
' 7.  Gets text options for DSUserData Leader.
' 8.  Modifies DSUserData Leader's text options only.
' 9.  Inserts third Leader, DS2.
' 10. Examine the drawing to verify that DS and DS2 Leaders
'     have the same arrow and text options.
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
        'Get active document
        Dim dsDoc As DraftSight.Document
        Set dsDoc = dsApp.GetActiveDocument()
```

```
        If dsDoc Is Nothing Then
            MsgBox ("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Get Sketch Manager
        Dim dsModel As DraftSight.Model
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsModel = dsDoc.GetModel()
        Set dsSketchMgr = dsModel.GetSketchManager()
```

```
        'Insert first Leader
        Dim Coordinates(8) As Double
        Coordinates(0) = 0
        Coordinates(1) = 0
        Coordinates(2) = 0
        Coordinates(3) = 4
        Coordinates(4) = 4
        Coordinates(5) = 0
        Coordinates(6) = 10
        Coordinates(7) = 4
        Coordinates(8) = 0
        Dim Width As Double
        Width = 5#
        Dim myNote As String
        myNote = "DSUserData"
        Dim dsLeader As DraftSight.Leader
        Set dsLeader = dsSketchMgr.InsertLeader(Coordinates, Width, myNote)
```

```
        'Insert second Leader
        Dim Coordinates2(8) As Double
        Coordinates2(0) = 8
        Coordinates2(1) = 8
        Coordinates2(2) = 8
        Coordinates2(3) = 8
        Coordinates2(4) = 8
        Coordinates2(5) = 8
        Coordinates2(6) = 20
        Coordinates2(7) = 8
        Coordinates2(8) = 8
        Dim myNote2 As String
        myNote2 = "DS"
        Dim dsLeader2 As DraftSight.Leader
        Set dsLeader2 = dsSketchMgr.InsertLeader(Coordinates2, Width, myNote2)
```

```
        'Zoom to fit
        dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
```

```
        'Get DimensionStyleUserData for dsUserData Leader
        Dim dsDimStyleUserData As DraftSight.DimensionStyleUserData
        Set dsDimStyleUserData = dsLeader.GetDimensionStyleUserData()
```

```
        'Get DimensionStyleArrowsOptions for DSUserData Leader
        Dim dsArrowsOptions As DraftSight.DimensionStyleArrowsOptions
        Set dsArrowsOptions = dsDimStyleUserData.GetDimensionStyleArrowsOptions()
```

```
        'Set arrow size for DSUserData Leader
        dsArrowsOptions.Size = 1#
```

```
        'Set arrow type for DSUserData Leader
        dsArrowsOptions.SetLeaderArrow dsDimensionArrowType_e.dsDimensionArrowType_Dot, ""
```

```
        'Get DimensionStyleTextOptions for DSUserData Leader
        Dim dsTextOptions As DraftSight.DimensionStyleTextOptions
        Set dsTextOptions = dsDimStyleUserData.GetDimensionStyleTextOptions()
```

```
        'Set text vertical position for DSUserData Leader
        dsTextOptions.VerticalPosition = dsDimensionTextVerticalPosition_e.dsDimensionTextVerticalPosition_Centered
```

```
        'Insert third Leader
        Dim Coordinates3(8) As Double
        Coordinates3(0) = 16
        Coordinates3(1) = 16
        Coordinates3(2) = 16
        Coordinates3(3) = 16
        Coordinates3(4) = 16
        Coordinates3(5) = 16
        Coordinates3(6) = 40
        Coordinates3(7) = 16
        Coordinates3(8) = 16
        Dim myNote3 As String
        myNote3 = "DS2"
        Dim dsLeader3 As DraftSight.Leader
        Set dsLeader3 = dsSketchMgr.InsertLeader(Coordinates3, Width, myNote3)
```

```
        'Zoom to fit
        dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
```

```
        'Examine the drawing to verify that DS and DS2 Leaders
        'have the same arrow and text options
```

```
    End Sub
```
