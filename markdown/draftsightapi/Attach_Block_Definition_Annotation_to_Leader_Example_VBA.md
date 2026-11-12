---
title: "Attach Block Definition Annotation to Leader Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Attach_Block_Definition_Annotation_to_Leader_Example_VBA.htm"
---

# Attach Block Definition Annotation to Leader Example (VBA)

This example shows how to attach a Block definition annotation to a Leader.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a drawing document.
' 5. Run the macro.
'
' Postconditions:
' 1. A message box pops up when the Block definition,
'    named MyBlockAnnotation, is created.
' 2. Click OK to close the message box.
' 3. A Leader is created and MyBlockAnnotation is
'    is attached to the Leader.
' 4. The drawing zooms to fit.
' 5. Examine the drawing.
'----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsSketchManager As DraftSight.SketchManager
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
```

```
    'Get active document
    Set dsDoc = dsApp.GetActiveDocument()

    If Not dsDoc Is Nothing Then
```

```
        'Get model space
        Set dsModel = dsDoc.GetModel()
```

```
        'Get Sketch Manager
        Set dsSketchManager = dsModel.GetSketchManager()
```

```
        'First Line's parameters
        Dim startX As Double
        startX = 1#
        Dim startY As Double
        startY = 1#
        Dim startZ As Double
        startZ = 0#
        Dim endX As Double
        endX = 6#
        Dim endY As Double
        endY = 1#
        Dim endZ As Double
        endZ = 0#
```

```
        'Construct a Line
        Dim dsLine As DraftSight.Line
        Set dsLine = dsSketchManager.InsertLine(startX, startY, startZ, endX, endY, endZ)
```

```
        'Second Line's parameters
        Dim start2X As Double
        start2X = 2#
        Dim start2Y As Double
        start2Y = 2#
        Dim start2Z As Double
        start2Z = 0#
        Dim end2X As Double
        end2X = 2#
        Dim end2Y As Double
        end2Y = 20#
        Dim end2Z As Double
        end2Z = 0#
```

```
        'Construct another Line
        Dim dsLine2 As DraftSight.Line
        Set dsLine2 = dsSketchManager.InsertLine(start2X, start2Y, start2Z, end2X, end2Y, end2Z)
```

```
        Dim typesArray(1) As Long
        typesArray(0) = 21
        typesArray(1) = 21
```

```
        Dim linesArray(1) As DraftSight.Line
        Set linesArray(0) = dsLine
        Set linesArray(1) = dsLine2
```

```
        Dim dsBlockDef As DraftSight.BlockDefinition
        Set dsBlockDef = dsDoc.CreateBlockDefinition("MyBlockAnnotation", "Block annotation to attach to Leader", 0, 0, 0, typesArray, linesArray, dsBlockDefinitionEntities_ConvertToBlock)        MsgBox ("Name of Block definition: " & dsBlockDef.GetName)
        MsgBox ("Name of Block definition: " & dsBlockDef.GetName
```

```
        'Add Leader
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
        'Attach Block definition to Leader,
        'which creates a Block instance
        Dim dsMathUtility As DraftSight.MathUtility
        Set dsMathUtility = dsApp.GetMathUtility
        Dim dsMathPoint As DraftSight.MathPoint
        Set dsMathPoint = dsMathUtility.CreatePoint(20, 20, 25)
        dsLeader.SetBlockAnnotation "MyBlockAnnotation", dsMathPoint
```

```
        dsApp.Zoom dsZoomRange_Fit, Nothing, Nothing
```

```
    End If

End Sub
```
