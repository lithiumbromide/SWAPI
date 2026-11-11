---
title: "Attach Note and Tolerance Annotations to Leaders Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Attach_Note_and_Tolerance_Annotations_to_Leaders_Example_VBNET.htm"
---

# Attach Note and Tolerance Annotations to Leaders Example (VB.NET)

This example shows how to attach Note and Tolerance annotations to Leaders.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
' 4. Start DraftSight and open a document.
' 5. Click Start Debugging.
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
Imports System.IO
Imports DraftSight.Interop.dsAutomation

Module Module1

    Dim dsApp As Application

    Sub Main()

        'Connect to DraftSight application
        dsApp = GetObject(, "DraftSight.Application")
        dsApp.AbortRunningCommand() ' Abort any command currently running in DraftSight to avoid nested commands

        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox("There are no open documents in DraftSight.")
            Return
        End If

        'Get model space
        Dim dsModel As Model = dsDoc.GetModel()

        'Get the Sketch Manager
        Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()

        'Add first Leader
        Dim leaderCoordinates As Double() = New Double() {6.5, 7.2, 0, 7.7, 8.6, 0}
        Dim noteWidth As Double = 1.0
        Dim noteText As String = "L1 "
        Dim dsLeader As Leader = dsSketchMgr.InsertLeader(leaderCoordinates, noteWidth, noteText)

        'Get command message
        Dim dsCommandMessage As CommandMessage = dsApp.GetCommandMessage()

        'Get math utility
        Dim dsMathUtility As MathUtility = dsApp.GetMathUtility()

        'Prompt to select the point where to insert the
        'Tolerance annotation to the Leader
        Dim firstX As Double = 0
        Dim firstY As Double = 0
        Dim firstZ As Double = 0
        Dim dsMathPlane As MathPlane
        dsMathUtility = dsApp.GetMathUtility()
        dsMathPlane = dsMathUtility.CreateXYPlane()
        Dim status As Boolean
        status = dsCommandMessage.PromptForPoint2("Click within the drawing to insert the geometric Tolerance", True, 0, 0, 0, firstX, firstY, firstZ, dsMathPlane)

        'Create the first math point
        Dim dsFirstMathPoint As MathPoint = dsMathUtility.CreatePoint(firstX, firstY, firstZ)

        'Attach the Tolerance annotation
        dsLeader.SetToleranceAnnotation("{\Fgdt;j}%%v{\Fgdt;n}0.7{\Fgdt;m}", dsFirstMathPoint)

        'Add second Leader
        Dim leaderCoordinates2 As Double() = New Double() {18, 29, 0, 30, 26, 0}
        Dim noteWidth2 As Double = 1.0
        Dim noteText2 As String = "L2 "
        Dim dsLeader2 As Leader = dsSketchMgr.InsertLeader(leaderCoordinates2, noteWidth2, noteText2)

        'Prompt to select the point where to insert a
        'Note annotation to the Leader
        Dim secondX As Double = 0
        Dim secondY As Double = 0
        Dim secondZ As Double = 0
        Dim dsMathPlane2 As MathPlane

        'Get math utility
        Dim dsMathUtility2 As MathUtility = dsApp.GetMathUtility()
        dsMathUtility2 = dsApp.GetMathUtility()
        dsMathPlane2 = dsMathUtility2.CreateXYPlane()
        dsCommandMessage.PromptForPoint2("Click within the drawing to insert the new Note", True, 0, 0, 0, secondX, secondY, secondZ, dsMathPlane2)

        'Create the second math point
        Dim dsSecondMathPoint As MathPoint = dsMathUtility.CreatePoint(secondX, secondY, secondZ)
```

```
        'Attach the New Note annotation
        dsLeader2.SetNoteAnnotation("New Note", dsSecondMathPoint)

        dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

    End Sub

End Module
```
