---
title: "Attach Block Definition Annotation to Leader Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Attach_Block_Definition_Annotation_to_Leader_Example_VBNET.htm"
---

# Attach Block Definition Annotation to Leader Example (VB.NET)

This example shows how to attach a Block definition annotation to a Leader.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Click Start Debugging.
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
Imports DraftSight.Interop.dsAutomation
Imports System
Imports System.Runtime.InteropServices

Module Module1

    Sub Main()
        Dim dsApp As Application
        Dim dsDoc As Document = Nothing
        Dim dsModel As Model = Nothing
        Dim dsSketchManager As SketchManager = Nothing

        'Connect to DraftSight
        dsApp = DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)
        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If (dsDoc IsNot Nothing) Then
            'Get model space
            dsModel = dsDoc.GetModel()

            'Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager()

            'First Line's parameters
            Dim startX As Double = 1.0
            Dim startY As Double = 1.0
            Dim startZ As Double = 0.0
            Dim endX As Double = 6.0
            Dim endY As Double = 1.0
            Dim endZ As Double = 0.0

            'Construct a Line
            Dim dsLine As Line = (dsSketchManager.InsertLine(startX, startY, startZ, endX, endY, endZ))

            'Second Line's parameters
            Dim start2X As Double = 2.0
            Dim start2Y As Double = 2.0
            Dim start2Z As Double = 0.0
            Dim end2X As Double = 2.0
            Dim end2Y As Double = 20.0
            Dim end2Z As Double = 0.0

            'Construct another Line
            Dim dsLine2 As Line = (dsSketchManager.InsertLine(start2X, start2Y, start2Z, end2X, end2Y, end2Z))

            Dim typesArray As Integer() = New Integer() {21, 21}
            Dim linesArray As Line() = New Line() {dsLine, dsLine2}

            Dim dsBlockDef As BlockDefinition = dsDoc.CreateBlockDefinition("MyBlockAnnotation", "Block annotation to attach to Leader", 0, 0, 0, typesArray, _
             linesArray, dsBlockDefinitionEntities_e.dsBlockDefinitionEntities_ConvertToBlock)
            MsgBox("Name of Block definition: " + dsBlockDef.GetName())

            'Add Leader
            Dim leaderCoordinates As Double() = New Double() {6.5, 7.2, 0, 7.7, 8.6, 0}
            Dim noteWidth As Double = 1.0
            Dim noteText As String = "L1 "
            Dim dsLeader As Leader = dsSketchManager.InsertLeader(leaderCoordinates, noteWidth, noteText)

            'Attach Block definition to Leader,
            'which creates a Block instance
            Dim dsMathUtility As MathUtility = dsApp.GetMathUtility()
            Dim dsMathPoint As MathPoint = dsMathUtility.CreatePoint(20, 20, 25)
            dsLeader.SetBlockAnnotation("MyBlockAnnotation", dsMathPoint)

            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)
        End If
    End Sub
End Module
```
