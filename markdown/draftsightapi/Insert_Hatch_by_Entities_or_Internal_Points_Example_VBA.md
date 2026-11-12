---
title: "Insert Hatch by Entities or Internal Points Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Hatch_by_Entities_or_Internal_Points_Example_VBA.htm"
---

# Insert Hatch by Entities or Internal Points Example (VBA)

This example shows how to insert a Hatch either by selecting sketch entities that form the Hatch boundary or by selecting internal points of enclosed areas of a drawing.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VBA macro in a software product in which VBA is
 '    embedded.
 ' 2. Copy and paste this example into the Visual Basic IDE.
 ' 3. Add a reference to the DraftSight type library,
 '    install_dir\bin\dsAutomation.dll.
 ' 4. Start DraftSight and open a drawing document with sketch entities.
 ' 5. Start debugging the project.
 '
 ' In the DraftSight command window, specify how the Hatch should be inserted:
 '    1. Type Entities.
 '    2. Select the sketch entities that form the boundary of the area to be hatched.
 '    3. Press Enter.
 '    -or-
 '    1. Type InternalPoints.
 '    2. Select three points that are in enclosed areas of the drawing.
 '
 ' Postconditions: A Hatch is inserted, and the drawing document
 ' is zoomed to fit.
 '----------------------------------------------------------------
 Option Explicit
 Dim dsApp As DraftSight.Application
 Dim dsDoc As DraftSight.Document
Sub Main()
     'Connect to DraftSight
     Set dsApp = GetObject(, "DraftSight.Application")
    'Get active document
     Set dsDoc = dsApp.GetActiveDocument()
     If dsDoc Is Nothing Then
         MsgBox ("There are no open documents in DraftSight.")
         Return
     End If

     'Abort any command currently running in DraftSight
     'to avoid nested commands
     dsApp.AbortRunningCommand
    'Get model space
     Dim dsModel As DraftSight.Model
     Set dsModel = dsDoc.GetModel()
    'Get sketch manager
     Dim dsSketchMgr As DraftSight.SketchManager
     Set dsSketchMgr = dsModel.GetSketchManager()
    'Get command message object
     Dim dsCommandMessage As DraftSight.CommandMessage
     Set dsCommandMessage = dsApp.GetCommandMessage()
    'Display a prompt at the command line to create Hatch by entities or by internal points
     Dim keywords(0 To 2) As String
     keywords(0) = "Entities"
     keywords(1) = "InternalPoints"
     Dim selectedKeyword As String
     selectedKeyword = ""
     Dim promptResult As Boolean
     promptResult = dsCommandMessage.PromptForKeyword("Insert Hatch by:", keywords, keywords(0), selectedKeyword)

    If promptResult Then
         'The user selected "By Entities" option
         If selectedKeyword = "_" + UCase(keywords(0)) Then
             Dim selectedEntities() As Object
             selectedEntities = SelectEntities(dsCommandMessage)
            Call InsertHatchByEntities(dsSketchMgr, selectedEntities)
         End If
        'The user selected "By Internal Points" option
         If selectedKeyword = "_" + UCase(keywords(1)) Then
             'Select three internal points
             Dim pointsCount As Integer
             pointsCount = 3
            dsCommandMessage.PrintLine ("Select three internal points for a Hatch")
            Dim internalPoints() As Double
             internalPoints = SelectPoints(dsCommandMessage, pointsCount)
            Call InsertHatchByInternalPoints(dsSketchMgr, internalPoints)
         End If
     End If
 End Sub
Sub InsertHatchByInternalPoints(dsSketchMgr As DraftSight.SketchManager, internalPoints() As Double)
     'Hatch parameters
     Dim patternName As String
     patternName = "ANSI31"
     Dim patternScale As Double
     patternScale = 1
     Dim patternAngle As Double
     patternAngle = 0
    'Insert Hatch
     Dim dsHatch As DraftSight.Hatch
     Set dsHatch = dsSketchMgr.InsertHatchByInternalPoints(internalPoints, patternName, patternScale, patternAngle)
     If Not dsHatch Is Nothing Then
         'Change color of Hatch
         Dim dsColor As DraftSight.Color
         Set dsColor = dsHatch.Color
         dsColor.SetNamedColor (dsNamedColor_e.dsNamedColor_Green)
         dsHatch.Color = dsColor
        'Zoom to fit
         dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
     Else
         MsgBox ("Hatch entity was not added to the current drawing.")
     End If
 End Sub
Function SelectPoints(dsCommandMessage As DraftSight.CommandMessage, internalPointsCount As Integer) As Double()
     Dim internalPoints(0 To 5) As Double
    'Run prompt for point
     Dim x As Double, y As Double, z As Double
     Dim i As Long
     For i = 0 To 2
         If dsCommandMessage.PromptForPoint("Specify internal point", x, y, z) Then
             internalPoints(2 * i) = x
             internalPoints(2 * i + 1) = y
         End If
     Next
    SelectPoints = internalPoints
 End Function
Sub InsertHatchByEntities(dsSketchMgr As DraftSight.SketchManager, dsEntities() As Object)
     'Hatch parameters
     Dim patternName As String
     patternName = "GRASS"
     Dim patternScale As Double
     patternScale = 1
     Dim patternAngle As Double
     patternAngle = 0
    'Insert Hatch
     Dim dsHatch As DraftSight.Hatch
     Set dsHatch = dsSketchMgr.InsertHatchByEntities(dsEntities, patternName, patternScale, patternAngle)
     If Not dsHatch Is Nothing Then
         'Change color of Hatch
         Dim dsColor As Color
         Set dsColor = dsHatch.Color
         dsColor.SetNamedColor (dsNamedColor_e.dsNamedColor_Blue)
         dsHatch.Color = dsColor
        'Zoom to fit
         dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
     Else
         MsgBox ("Hatch entity was not added to the current drawing.")
     End If
 End Sub
Function SelectEntities(dsCommandMessage As DraftSight.CommandMessage) As Object()
     Dim selectedEntities() As Object
    'Prompt for multiple selection of entities
     If dsCommandMessage.PromptForSelection(False, "Specify entities", "It is not an entity") Then
         'Get selection manager
         Dim dsSelectionMgr As DraftSight.SelectionManager
         Set dsSelectionMgr = dsDoc.GetSelectionManager()
        'Get count of selected entities
         Dim selectionType As dsSelectionSetType_e
         selectionType = dsSelectionSetType_e.dsSelectionSetType_Previous
         Dim count As Long
         count = dsSelectionMgr.GetSelectedObjectCount(selectionType)
         Debug.Print ("Number of entities selected: " & count)
         ReDim selectedEntities(0 To count - 1) As Object
         Dim index As Long
         If count > 0 Then
             For index = 0 To (count - 1)
                 Dim entityType As dsObjectType_e
                 Set selectedEntities(index) = dsSelectionMgr.GetSelectedObject(selectionType, index, entityType)
             Next
         End If
     End If
    SelectEntities = selectedEntities
 End Function
```
