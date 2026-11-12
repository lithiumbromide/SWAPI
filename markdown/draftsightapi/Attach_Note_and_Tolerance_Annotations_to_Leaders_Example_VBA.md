---
title: "Attach Note and Tolerance Annotations to Leaders Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Attach_Note_and_Tolerance_Annotations_to_Leaders_Example_VBA.htm"
---

# Attach Note and Tolerance Annotations to Leaders Example (VBA)

This example shows how to attach Note and Tolerance annotations to Leaders.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll
' 4. Start DraftSight and open a drawing document.
' 5. Run the macro.
'
' Postconditions:
' 1. A Leader is constructed with a Note.
' 2. Click within the drawing to specify the point
'    where to attach a geometric Tolerance annotation
'    to the Leader.
' 3. The geometric Tolerance annotation is attached to
'    the Leader.
' 4. A second leader is constructed with a Note.
' 5. Click within the drawing to specify the
'    point where to attach the New Note annotation to
'    the Leader.
' 6. The New Note annotation is attached to the Leader.
' 7. The drawing is zoomed to fit.
'------------------------------------------------------------
Option Explicit
```

```
Dim dsApp As DraftSight.Application
```

```
Sub main()
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
```

```
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get active document
    Dim dsDoc As DraftSight.Document
    Set dsDoc = dsApp.GetActiveDocument
    If Not dsDoc Is Nothing Then
```

```
        'Get model space
        Dim dsModel As DraftSight.Model
        Set dsModel = dsDoc.GetModel
```

```
        'Get Sketch Manager
        Dim dsSketchManager As DraftSight.SketchManager
        Set dsSketchManager = dsModel.GetSketchManager
```

```
        'Add first Leader
        Dim leaderCoordinates(5) As Double
        leaderCoordinates(0) = 6.5
        leaderCoordinates(1) = 7.2
        leaderCoordinates(2) = 0
        leaderCoordinates(3) = 7.7
        leaderCoordinates(4) = 8.6
        leaderCoordinates(5) = 0
        Dim noteWidth As Double
        noteWidth = 1#
        Dim noteText As String
        noteText = "L1 "
        Dim dsLeader As DraftSight.Leader
        Set dsLeader = dsSketchManager.InsertLeader(leaderCoordinates, noteWidth, noteText)
```

```
        'Get command message
        Dim dsCommandMessage As DraftSight.CommandMessage
        Set dsCommandMessage = dsApp.GetCommandMessage
```

```
        'Get math utility
        Dim dsMathUtility As DraftSight.MathUtility
        Set dsMathUtility = dsApp.GetMathUtility
```

```
        'Prompt to select the point where to attach the
        'Tolerance annotation to the Leader
        Dim firstX As Double
        Dim firstY As Double
        Dim firstZ As Double
        Dim dsMathPlane As DraftSight.MathPlane
        Set dsMathPlane = dsMathUtility.CreateXYPlane
        dsCommandMessage.PromptForPoint2 "Click within the drawing to insert the geometric Tolerance", True, 0, 0, 0, firstX, firstY, firstZ, dsMathPlane
```

```
        'Create the first math point
        Dim dsFirstMathPoint As DraftSight.MathPoint
        Set dsFirstMathPoint = dsMathUtility.CreatePoint(firstX, firstY, firstZ)
```

```
        ' Attach the Tolerance annotation
        dsLeader.SetToleranceAnnotation "{\Fgdt;j}%%v{\Fgdt;n}0.7{\Fgdt;m}", dsFirstMathPoint
```

```
        'Add second Leader
        Dim leaderCoordinates2(5) As Double
        leaderCoordinates2(0) = 18
        leaderCoordinates2(1) = 29
        leaderCoordinates2(2) = 0
        leaderCoordinates2(3) = 30
        leaderCoordinates2(4) = 26
        leaderCoordinates2(5) = 0
        Dim noteWidth2 As Double
        noteWidth2 = 1#
        Dim noteText2 As String
        noteText2 = "L2 "
        Dim dsLeader2 As DraftSight.Leader
        Set dsLeader2 = dsSketchManager.InsertLeader(leaderCoordinates2, noteWidth2, noteText2)
```

```
        'Get math utility
        Dim dsMathUtility2 As DraftSight.MathUtility
        Set dsMathUtility2 = dsApp.GetMathUtility
```

```
        'Prompt to select the point where to attach the
        'New Note annotation to the Leader
        Dim secondX As Double
        Dim secondY As Double
        Dim secondZ As Double
        Dim dsMathPlane2 As DraftSight.MathPlane
        Set dsMathPlane2 = dsMathUtility.CreateXYPlane
        dsCommandMessage.PromptForPoint2 "Click within the drawing to insert a new Note", True, 0, 0, 0, secondX, secondY, secondZ, dsMathPlane2
```

```
        'Create the first math point
        Dim dsSecondMathPoint2 As DraftSight.MathPoint
        Set dsSecondMathPoint2 = dsMathUtility2.CreatePoint(secondX, secondY, secondZ)

        ' Attach the New Note annotation
        dsLeader2.SetToleranceAnnotation "New Note", dsSecondMathPoint2
```

```
        dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
```

```
    End If
```

```
End Sub
```
